BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

HOURLY_VARIABLES_STR = ",".join([
    "temperature_2m",
    "apparent_temperature",
    "relative_humidity_2m",
    "precipitation",
    "rain",
    "snowfall",
    "cloud_cover",
    "visibility",
    "pressure_msl",
    "wind_speed_10m",
    "wind_gusts_10m",
    "wind_direction_10m",
    "weather_code",
    "snow_depth"
])

START_DATE = "2000-01-01"
END_DATE = "2026-01-01"