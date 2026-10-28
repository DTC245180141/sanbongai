using System;
using System.Net.Http;
using FootballBookingApi.Services;
using Microsoft.Extensions.Caching.Memory;
using Xunit;

namespace FootballBookingApi.Tests
{
    public class AIServiceClientTests
    {
        private readonly AIServiceClient _client;
        private readonly IMemoryCache _memoryCache;
        private readonly Guid _sampleFieldId = Guid.NewGuid();

        public AIServiceClientTests()
        {
            _memoryCache = new MemoryCache(new MemoryCacheOptions());
            // HttpClient pointing to invalid port so it immediately triggers the resilient Fallback Engine
            var httpClient = new HttpClient { Timeout = TimeSpan.FromMilliseconds(500) };
            _client = new AIServiceClient(httpClient, _memoryCache);
        }

        [Fact]
        public void GetAiOptimalPrice_WeekdayNormalHours_AppliesBaseMultiplier()
        {
            // Wednesday at 10:00 (Weekday, normal morning hours)
            var bookingTime = new DateTime(2026, 9, 23, 10, 0, 0, DateTimeKind.Utc); // Wednesday
            decimal basePrice = 150000m;

            var result = _client.GetAiOptimalPrice(_sampleFieldId, bookingTime, basePrice);

            Assert.NotNull(result);
            Assert.Equal(1.0m, result.multiplier);
            Assert.Equal(150000m, result.dynamic_price);
        }

        [Fact]
        public void GetAiOptimalPrice_WeekendNormalHours_AddsWeekendSurcharge()
        {
            // Sunday at 10:00 (Weekend morning: +30%)
            var bookingTime = new DateTime(2026, 9, 27, 10, 0, 0, DateTimeKind.Utc); // Sunday
            decimal basePrice = 150000m;

            var result = _client.GetAiOptimalPrice(_sampleFieldId, bookingTime, basePrice);

            Assert.NotNull(result);
            Assert.Equal(1.30m, result.multiplier);
            Assert.Equal(195000m, result.dynamic_price);
            Assert.Contains(result.reasons, r => r.Contains("Cuối tuần"));
        }

        [Fact]
        public void GetAiOptimalPrice_WeekdayPeakHours_AddsPeakSurcharge()
        {
            // Wednesday at 19:00 (Peak hour 18h-21h: +50%)
            var bookingTime = new DateTime(2026, 9, 23, 19, 0, 0, DateTimeKind.Utc); // Wednesday
            decimal basePrice = 150000m;

            var result = _client.GetAiOptimalPrice(_sampleFieldId, bookingTime, basePrice);

            Assert.NotNull(result);
            Assert.Equal(1.50m, result.multiplier);
            Assert.Equal(225000m, result.dynamic_price);
            Assert.Contains(result.reasons, r => r.Contains("cao điểm"));
        }

        [Fact]
        public void GetAiOptimalPrice_WeekendPeakHours_CombinesBothSurcharges()
        {
            // Saturday at 20:00 (Weekend + Peak: 1.0 + 0.3 + 0.5 = 1.8x)
            var bookingTime = new DateTime(2026, 9, 26, 20, 0, 0, DateTimeKind.Utc); // Saturday
            decimal basePrice = 150000m;

            var result = _client.GetAiOptimalPrice(_sampleFieldId, bookingTime, basePrice);

            Assert.NotNull(result);
            Assert.Equal(1.80m, result.multiplier);
            Assert.Equal(270000m, result.dynamic_price);
            Assert.Equal(2, result.reasons.Count);
        }
    }
}

