using Microsoft.EntityFrameworkCore;
using FootballBookingApi.Models;

namespace FootballBookingApi.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
        }

        public DbSet<User> Users { get; set; } = null!;
        public DbSet<PricingConfig> PricingConfigs { get; set; } = null!;
        public DbSet<FootballField> Fields { get; set; } = null!;
        public DbSet<Booking> Bookings { get; set; } = null!;
        public DbSet<Transaction> Transactions { get; set; } = null!;
        public DbSet<Payment> Payments { get; set; } = null!;
        public DbSet<AIDemandLog> AI_DemandLogs { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<User>()
                .HasIndex(u => u.Phone)
                .IsUnique();

            modelBuilder.Entity<User>()
                .HasIndex(u => u.Email)
                .IsUnique();

            modelBuilder.Entity<Booking>()
                .HasOne(b => b.User)
                .WithMany(u => u.Bookings)
                .HasForeignKey(b => b.UserId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Booking>()
                .HasOne(b => b.Field)
                .WithMany(f => f.Bookings)
                .HasForeignKey(b => b.FieldId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Booking>()
                .HasIndex(b => new { b.FieldId, b.StartTime, b.EndTime });

            modelBuilder.Entity<Transaction>()
                .HasOne(t => t.User)
                .WithMany(u => u.Transactions)
                .HasForeignKey(t => t.UserId)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<Payment>()
                .HasOne(p => p.Booking)
                .WithOne(b => b.Payment)
                .HasForeignKey<Payment>(p => p.BookingId);

            modelBuilder.Entity<AIDemandLog>()
                .HasOne(a => a.Field)
                .WithMany(f => f.DemandLogs)
                .HasForeignKey(a => a.FieldId);

            // Seed PricingConfig Ban Đầu
            modelBuilder.Entity<PricingConfig>().HasData(
                new PricingConfig { ConfigId = 1, FieldType = 5, BasePrice = 200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
                new PricingConfig { ConfigId = 2, FieldType = 7, BasePrice = 400000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m },
                new PricingConfig { ConfigId = 3, FieldType = 11, BasePrice = 1200000, WeekendMultiplier = 1.30m, PeakHourMultiplier = 1.50m }
            );
        }
    }
}
