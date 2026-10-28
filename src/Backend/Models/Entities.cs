using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace FootballBookingApi.Models
{
    public enum UserRole
    {
        Customer = 0,
        Admin = 1
    }

    public enum BookingStatus
    {
        Pending = 0,
        Confirmed = 1,
        Cancelled = 2,
        Completed = 3
    }

    public enum PaymentMethod
    {
        MoMo = 0,
        VNPay = 1,
        ZaloPay = 2,
        Cash = 3,
        Wallet = 4
    }

    public enum PaymentStatus
    {
        Failed = 0,
        Success = 1,
        Refunded = 2
    }

    public enum DepositStatus
    {
        Pending = 0,
        Success = 1,
        Rejected = 2
    }

    public class DepositRequest
    {
        [Key]
        public Guid Id { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(100)]
        public string TransactionCode { get; set; } = string.Empty;

        public string Memo { get; set; } = string.Empty;

        public string ImageUrl { get; set; } = string.Empty;

        public DepositStatus Status { get; set; } = DepositStatus.Pending;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public DateTime? ProcessedAt { get; set; }

        public User? User { get; set; }
    }

    public class User
    {
        [Key]
        public Guid Id { get; set; } = Guid.NewGuid();

        [Required, MaxLength(50)]
        public string Username { get; set; } = string.Empty;

        [Required, MaxLength(100)]
        public string FullName { get; set; } = string.Empty;

        [Required, MaxLength(15)]
        public string Phone { get; set; } = string.Empty;

        [Required, MaxLength(100)]
        public string Email { get; set; } = string.Empty;

        public string? AvatarUrl { get; set; }

        public UserRole Role { get; set; } = UserRole.Customer;

        [Required]
        public string PasswordHash { get; set; } = string.Empty;

        [Column(TypeName = "decimal(18,2)")]
        public decimal WalletBalance { get; set; } = 2000000.00m; // Mặc định cấp sẵn 2.000.000 VNĐ cho tài khoản

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public bool IsDeleted { get; set; } = false;

        public ICollection<Booking> Bookings { get; set; } = new List<Booking>();
        public ICollection<Transaction> Transactions { get; set; } = new List<Transaction>();
    }

    public class PricingConfig
    {
        [Key]
        public int ConfigId { get; set; }

        public int FieldType { get; set; } // 5, 7, 11 người

        [Column(TypeName = "decimal(18,2)")]
        public decimal BasePrice { get; set; }

        [Column(TypeName = "decimal(4,2)")]
        public decimal WeekendMultiplier { get; set; } = 1.30m;

        [Column(TypeName = "decimal(4,2)")]
        public decimal PeakHourMultiplier { get; set; } = 1.50m;

        public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }

    public class Transaction
    {
        [Key]
        public Guid TransactionId { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(20)]
        public string Type { get; set; } = "Payment"; // 'Payment' hoặc 'Refund'

        public Guid? BookingId { get; set; }

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public User? User { get; set; }
    }

    public class FootballField
    {
        [Key]
        public Guid FieldId { get; set; } = Guid.NewGuid();

        [Required, MaxLength(100)]
        public string Name { get; set; } = string.Empty;

        public int FieldType { get; set; } = 5;

        [Column(TypeName = "decimal(18,2)")]
        public decimal BasePrice { get; set; }

        public bool Status { get; set; } = true;

        public string Location { get; set; } = string.Empty;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public ICollection<Booking> Bookings { get; set; } = new List<Booking>();
        public ICollection<AIDemandLog> DemandLogs { get; set; } = new List<AIDemandLog>();
    }

    public class Booking
    {
        [Key]
        public Guid BookingId { get; set; } = Guid.NewGuid();

        public Guid UserId { get; set; }
        public ForeignKeyAttribute? UserRef { get; set; }

        public Guid FieldId { get; set; }

        public DateTime BookingTime { get; set; } = DateTime.Now;
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal TotalPrice { get; set; }

        public BookingStatus Status { get; set; } = BookingStatus.Pending;

        public bool IsAIPriced { get; set; } = true;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        public User? User { get; set; }
        public FootballField? Field { get; set; }
        public Payment? Payment { get; set; }
    }

    public class Payment
    {
        [Key]
        public Guid PaymentId { get; set; } = Guid.NewGuid();

        public Guid BookingId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Amount { get; set; }

        [Required, MaxLength(100)]
        public string TransactionId { get; set; } = string.Empty;

        public PaymentMethod Method { get; set; } = PaymentMethod.Wallet;

        public PaymentStatus Status { get; set; } = PaymentStatus.Success;

        public DateTime PaidAt { get; set; } = DateTime.UtcNow;

        public Booking? Booking { get; set; }
    }

    public class AIDemandLog
    {
        [Key]
        public Guid LogId { get; set; } = Guid.NewGuid();

        public Guid FieldId { get; set; }

        public DateTime LogTime { get; set; } = DateTime.UtcNow;

        public int DemandScore { get; set; } = 1;

        [Column(TypeName = "decimal(4,2)")]
        public decimal SuggestedMultiplier { get; set; } = 1.0m;

        public bool IsOverridden { get; set; } = false;

        public FootballField? Field { get; set; }
    }
}
