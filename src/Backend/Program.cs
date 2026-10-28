using FootballBookingApi.Data;
using FootballBookingApi.Services;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.ResponseCompression;
using System.IO.Compression;

var builder = WebApplication.CreateBuilder(args);

// 1. Cấu hình Controllers & JSON Serializer tối ưu hiệu năng
builder.Services.AddControllers()
    .AddJsonOptions(options =>
    {
        options.JsonSerializerOptions.PropertyNamingPolicy = System.Text.Json.JsonNamingPolicy.CamelCase;
        options.JsonSerializerOptions.DefaultIgnoreCondition = System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull;
    });

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddHttpClient();

// Tối ưu hiệu năng: Kích hoạt In-Memory Cache lưu trữ các tính toán giá AI và truy vấn lặp
builder.Services.AddMemoryCache();

// Tối ưu hiệu năng: Nén Response động (Brotli + Gzip) giúp giảm payload từ 70% - 90%
builder.Services.AddResponseCompression(options =>
{
    options.EnableForHttps = true;
    options.Providers.Add<BrotliCompressionProvider>();
    options.Providers.Add<GzipCompressionProvider>();
});
builder.Services.Configure<BrotliCompressionProviderOptions>(options =>
{
    options.Level = CompressionLevel.Fastest;
});
builder.Services.Configure<GzipCompressionProviderOptions>(options =>
{
    options.Level = CompressionLevel.Fastest;
});

// 2. Cấu hình Entity Framework Core với SQL Server
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection") 
    ?? "Server=(localdb)\\mssqllocaldb;Database=FootballBookingDB;Trusted_Connection=True;MultipleActiveResultSets=true"));

// 3. Đăng ký Business Logic Services
builder.Services.AddSingleton<IBookingService, BookingService>();
builder.Services.AddSingleton<IAIServiceClient, AIServiceClient>();
builder.Services.AddSingleton<IUserService, UserService>();

// 4. Cấu hình CORS Policy
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

// 5. Cấu hình Pipeline Middleware tối ưu hiệu năng
app.UseResponseCompression();

app.UseSwagger();
app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/swagger/v1/swagger.json", "Football Booking AI System API V1");
    c.RoutePrefix = "swagger";
});

app.UseCors("AllowAll");

// Tối ưu static files: Cache Control 1 ngày cho hình ảnh và tài nguyên tĩnh
app.UseStaticFiles(new StaticFileOptions
{
    OnPrepareResponse = ctx =>
    {
        ctx.Context.Response.Headers.Append("Cache-Control", "public, max-age=86400");
    }
});

// Middleware Bảo Trì Toàn Hệ Thống (Global Maintenance Mode)
app.Use(async (context, next) =>
{
    var bookingService = context.RequestServices.GetRequiredService<IBookingService>();
    var path = context.Request.Path.Value?.ToLower() ?? "";

    // Bỏ qua nếu hệ thống không bảo trì
    if (!bookingService.IsSystemMaintenance)
    {
        await next();
        return;
    }

    // Ngoại lệ: Cho phép tất cả các request trong AdminController (/api/admin) và các tài nguyên static
    if (path.StartsWith("/api/admin") || path.StartsWith("/swagger") || path.Contains("."))
    {
        await next();
        return;
    }

    // Ngoại lệ: Cho phép Header X-Role: Admin hoặc Query ?role=admin nếu gọi API
    if (context.Request.Headers["X-Role"].ToString().Equals("Admin", StringComparison.OrdinalIgnoreCase) ||
        context.Request.Query["role"].ToString().Equals("admin", StringComparison.OrdinalIgnoreCase))
    {
        await next();
        return;
    }

    // Tất cả request khác của Khách Hàng gửi đến API trả về 503 Service Unavailable
    context.Response.StatusCode = StatusCodes.Status503ServiceUnavailable;
    context.Response.ContentType = "application/json; charset=utf-8";
    var responseObj = new
    {
        status = 503,
        error = "Service Unavailable",
        message = "Hệ thống đang bảo trì để nâng cấp, vui lòng quay lại sau!"
    };
    await context.Response.WriteAsJsonAsync(responseObj);
});

app.UseAuthorization();
app.MapControllers();

Console.WriteLine("=================================================");
Console.WriteLine("🚀 Football Booking Backend API Server Loaded");
Console.WriteLine("🌐 Listening Port: http://localhost:5048");
Console.WriteLine("📚 Swagger Docs:   http://localhost:5048/swagger");
Console.WriteLine("=================================================");

app.Run("http://localhost:5048");
