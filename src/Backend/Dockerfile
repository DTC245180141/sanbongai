# ==============================================================================
# DOCKERFILE FOR FOOTBALL BOOKING BACKEND WEB API (.NET 10)
# ==============================================================================
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

COPY ["FootballBookingApi.csproj", "./"]
RUN dotnet restore "FootballBookingApi.csproj"

COPY . .
RUN dotnet publish "FootballBookingApi.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_URLS=http://+:5048
ENV ASPNETCORE_ENVIRONMENT=Production

EXPOSE 5048
ENTRYPOINT ["dotnet", "FootballBookingApi.dll"]
