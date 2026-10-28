using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Extensions.Caching.Memory;

namespace FootballBookingApi.Services
{
    public interface IAIServiceClient
    {
        AIPricingResult GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice);
        Task<AIPricingResult> GetAiOptimalPriceAsync(Guid fieldId, DateTime bookingTime, decimal basePrice);
    }

    public class AIPricingResult
    {
        public string status { get; set; } = "success";
        public string field_id { get; set; } = string.Empty;
        public decimal base_price { get; set; }
        public decimal dynamic_price { get; set; }
        public decimal multiplier { get; set; }
        public List<string> reasons { get; set; } = new();
        public int hour { get; set; }
        public int day_of_week { get; set; }
    }

    public class AIServiceClient : IAIServiceClient
    {
        private readonly HttpClient _httpClient;
        private readonly IMemoryCache _cache;

        public AIServiceClient(HttpClient httpClient, IMemoryCache cache)
        {
            _httpClient = httpClient;
            _cache = cache;
        }

        public AIPricingResult GetAiOptimalPrice(Guid fieldId, DateTime bookingTime, decimal basePrice)
        {
            return GetAiOptimalPriceAsync(fieldId, bookingTime, basePrice).GetAwaiter().GetResult();
        }

        public async Task<AIPricingResult> GetAiOptimalPriceAsync(Guid fieldId, DateTime bookingTime, decimal basePrice)
        {
            // Tối ưu hiệu năng: Cache kết quả định giá AI trong 5 phút để loại bỏ độ trễ mạng khi nhiều user tải trang
            string cacheKey = $"ai_price_{fieldId}_{bookingTime:yyyyMMddHH}_{basePrice}";
            if (_cache.TryGetValue(cacheKey, out AIPricingResult? cachedResult) && cachedResult != null)
            {
                return cachedResult;
            }

            AIPricingResult? result = null;
            try
            {
                // Chuyển đổi DayOfWeek từ C# (Sunday = 0, Monday = 1, ..., Saturday = 6)
                // sang chuẩn Python weekday (Monday = 0, ..., Saturday = 5, Sunday = 6)
                int pythonDayOfWeek = bookingTime.DayOfWeek == DayOfWeek.Sunday ? 6 : (int)bookingTime.DayOfWeek - 1;

                var payload = new
                {
                    field_id = fieldId.ToString(),
                    base_price = basePrice,
                    hour = bookingTime.Hour,
                    day_of_week = pythonDayOfWeek
                };

                using var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
                using var response = await _httpClient.PostAsync("http://localhost:5050/api/predict-price", content);

                if (response.IsSuccessStatusCode)
                {
                    var jsonStr = await response.Content.ReadAsStringAsync();
                    result = JsonSerializer.Deserialize<AIPricingResult>(jsonStr);
                }
            }
            catch (Exception)
            {
                // Fallback nếu AI Microservice không hoạt động
            }

            if (result == null)
            {
                // Logic Fallback dự phòng
                decimal multiplier = 1.0m;
                var reasons = new List<string>();
                if (bookingTime.DayOfWeek == DayOfWeek.Saturday || bookingTime.DayOfWeek == DayOfWeek.Sunday)
                {
                    multiplier += 0.30m;
                    reasons.Add("Phụ thu Cuối tuần (Fallback +30%)");
                }
                if (bookingTime.Hour >= 18 && bookingTime.Hour <= 21)
                {
                    multiplier += 0.50m;
                    reasons.Add("Khung giờ cao điểm 18h-21h (Fallback +50%)");
                }

                result = new AIPricingResult
                {
                    status = "fallback",
                    field_id = fieldId.ToString(),
                    base_price = basePrice,
                    dynamic_price = Math.Round(basePrice * multiplier, 0),
                    multiplier = multiplier,
                    reasons = reasons.Count > 0 ? reasons : new List<string> { "Giá niêm yết tiêu chuẩn" },
                    hour = bookingTime.Hour,
                    day_of_week = (int)bookingTime.DayOfWeek
                };
            }

            // Lưu vào RAM Cache trong 5 phút
            _cache.Set(cacheKey, result, TimeSpan.FromMinutes(5));
            return result;
        }
    }
}
