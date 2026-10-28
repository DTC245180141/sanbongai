-- ============================================================================
-- DỰ ÁN: HỆ THỐNG QUẢN LÝ ĐẶT SÂN BÓNG TỰ ĐỘNG TÍCH HỢP AI
-- DATABASE SCHEMA DESIGN (SQL SERVER) - CẬP NHẬT WALLET & TRANSACTIONS
-- ============================================================================

CREATE DATABASE FootballBookingDB;
GO

USE FootballBookingDB;
GO

-- 1. Bảng Users (Tài khoản người dùng, Admin & Ví tiền WalletBalance)
CREATE TABLE Users (
    Id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    FullName NVARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Role INT NOT NULL DEFAULT 0, -- 0: Customer, 1: Admin
    PasswordHash NVARCHAR(MAX) NOT NULL,
    WalletBalance DECIMAL(18,2) NOT NULL DEFAULT 2000000.00 CHECK (WalletBalance >= 0),
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    IsDeleted BIT NOT NULL DEFAULT 0
);

-- 2. Bảng PricingConfig (Cấu hình giá niêm yết & Hệ số AI Dynamic Pricing)
CREATE TABLE PricingConfig (
    ConfigId INT PRIMARY KEY IDENTITY(1,1),
    FieldType INT NOT NULL UNIQUE, -- 5, 7, 11
    BasePrice DECIMAL(18,2) NOT NULL CHECK (BasePrice > 0),
    WeekendMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.30,
    PeakHourMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.50,
    UpdatedAt DATETIME2 NOT NULL DEFAULT GETDATE()
);

-- 3. Bảng Fields (Thông tin Sân bóng)
CREATE TABLE Fields (
    FieldId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    Name NVARCHAR(100) NOT NULL,
    FieldType INT NOT NULL, -- 5: Sân 5 người, 7: Sân 7 người, 11: Sân 11 người
    BasePrice DECIMAL(18,2) NOT NULL CHECK (BasePrice > 0),
    Status BIT NOT NULL DEFAULT 1, -- 1: Active, 0: Maintenance
    Location NVARCHAR(255) NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE()
);

-- 4. Bảng Bookings (Giao dịch đặt sân cốt lõi)
CREATE TABLE Bookings (
    BookingId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    UserId UNIQUEIDENTIFIER NOT NULL,
    FieldId UNIQUEIDENTIFIER NOT NULL,
    BookingTime DATETIME2 NOT NULL,
    StartTime DATETIME2 NOT NULL,
    EndTime DATETIME2 NOT NULL,
    TotalPrice DECIMAL(18,2) NOT NULL CHECK (TotalPrice >= 0),
    Status INT NOT NULL DEFAULT 1, -- 0: Pending, 1: Confirmed, 2: Cancelled, 3: Completed
    IsAIPriced BIT NOT NULL DEFAULT 1,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Bookings_Users FOREIGN KEY (UserId) REFERENCES Users(Id),
    CONSTRAINT FK_Bookings_Fields FOREIGN KEY (FieldId) REFERENCES Fields(FieldId),
    CONSTRAINT CHK_Booking_Time CHECK (EndTime > StartTime)
);

CREATE INDEX IX_Bookings_FieldId_StartTime ON Bookings(FieldId, StartTime, EndTime);
CREATE INDEX IX_Bookings_UserId ON Bookings(UserId);

-- 5. Bảng Transactions (Lịch sử giao dịch ví WalletBalance)
CREATE TABLE Transactions (
    TransactionId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    UserId UNIQUEIDENTIFIER NOT NULL,
    Amount DECIMAL(18,2) NOT NULL,
    Type VARCHAR(20) NOT NULL, -- 'Payment' (Thanh toán) hoặc 'Refund' (Hoàn tiền)
    BookingId UNIQUEIDENTIFIER NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Transactions_Users FOREIGN KEY (UserId) REFERENCES Users(Id)
);

-- 6. Bảng Payments (Lưu vết giao dịch thanh toán)
CREATE TABLE Payments (
    PaymentId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    BookingId UNIQUEIDENTIFIER NOT NULL UNIQUE,
    Amount DECIMAL(18,2) NOT NULL,
    TransactionId VARCHAR(100) NOT NULL,
    PaymentMethod INT NOT NULL, -- 0: MoMo, 1: VNPay, 2: ZaloPay, 3: Wallet
    Status INT NOT NULL DEFAULT 1, -- 0: Failed, 1: Success, 2: Refunded
    PaidAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT FK_Payments_Bookings FOREIGN KEY (BookingId) REFERENCES Bookings(BookingId)
);

-- 7. Bảng AI_DemandLogs
CREATE TABLE AI_DemandLogs (
    LogId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    FieldId UNIQUEIDENTIFIER NOT NULL,
    LogTime DATETIME2 NOT NULL,
    DemandScore INT NOT NULL DEFAULT 1,
    SuggestedMultiplier DECIMAL(4,2) NOT NULL DEFAULT 1.0,
    IsOverridden BIT NOT NULL DEFAULT 0,
    CONSTRAINT FK_AIDemandLogs_Fields FOREIGN KEY (FieldId) REFERENCES Fields(FieldId)
);
