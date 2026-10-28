@echo off
chcp 65001 > nul
title HỆ THỐNG ĐẶT SÂN BÓNG ICTU PITCHAI - KHỞI ĐỘNG ĐA DỊCH VỤ
echo ==============================================================================
echo 🚀 ĐỒ ÁN TỐT NGHIỆP: HỆ THỐNG ĐẶT SÂN BÓNG AI & VÍ TIỀN VIRTUAL WALLET
echo 🏫 TRƯỜNG ĐẠI HỌC CNTT & TT THÁI NGUYÊN (ICTU) - NHÓM 02
echo ==============================================================================
echo.

echo [1/3] Đang khởi chạy AI Microservice (Python Flask - Port 5050)...
start "PitchAI - AI Microservice (Port 5050)" cmd /k "cd /d %~dp0src\AIService && python app.py"

timeout /t 3 /nobreak > nul

echo [2/3] Đang khởi chạy Backend Web API (.NET 10 - Port 5048)...
start "PitchAI - Backend API (Port 5048)" cmd /k "cd /d %~dp0src\Backend && dotnet run"

timeout /t 3 /nobreak > nul

echo [3/3] Đang mở giao diện Khách hàng & Quản trị viên...
start "" "%~dp0src\Frontend\index.html"
start "" "http://localhost:5048/swagger"

echo.
echo ==============================================================================
echo ✅ TẤT CẢ CÁC DỊCH VỤ ĐÃ ĐƯỢC KHỞI ĐỘNG THÀNH CÔNG!
echo 🌐 Giao diện Khách hàng: file://%~dp0src/Frontend/index.html
echo 📚 Tài liệu Swagger API: http://localhost:5048/swagger
echo 🤖 AI Microservice Health: http://localhost:5050/health
echo ==============================================================================
echo.
pause
