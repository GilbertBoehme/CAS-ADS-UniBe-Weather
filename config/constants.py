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

DB_URI = "postgresql+psycopg2://gbo@localhost:5432/postgres"

BRONZE_TABLE_NAME = "bronze_weather"
BRONZE_TABLE_NAME = "silver_weather"
TEMP_TABLE = "temp_weather"

START_DATE = "2016-01-01"
END_DATE = "2026-01-01"

WEATHER_CODES = {
    # Clear / partly cloudy / overcast
    0: ("Clear sky", 0),
    1: ("Mainly clear", 0),
    2: ("Partly cloudy", 0),
    3: ("Overcast", 0),

    # Fog
    45: ("Fog", 1),
    48: ("Depositing rime fog", 1),

    # Drizzle (low hazard)
    51: ("Light drizzle", 0),
    53: ("Moderate drizzle", 0),
    55: ("Dense drizzle", 0),

    # Freezing drizzle (hazardous)
    56: ("Light freezing drizzle", 1),
    57: ("Dense freezing drizzle", 1),

    # Rain
    61: ("Slight rain", 0),
    63: ("Moderate rain", 1),
    65: ("Heavy rain", 1),

    # Freezing rain
    66: ("Light freezing rain", 1),
    67: ("Heavy freezing rain", 1),

    # Snow fall
    71: ("Slight snow fall", 0),
    73: ("Moderate snow fall", 0),
    75: ("Heavy snow fall", 1),

    # Snow grains
    77: ("Snow grains", 0),

    # Rain showers
    80: ("Slight rain shower", 0),
    81: ("Moderate rain shower", 0),
    82: ("Violent rain shower", 1),

    # Snow showers
    85: ("Slight snow shower", 0),
    86: ("Heavy snow shower", 1),

    # Thunderstorm
    95: ("Thunderstorm (slight/moderate)", 1),

    # Thunderstorm with hail
    96: ("Thunderstorm with slight hail", 1),
    99: ("Thunderstorm with heavy hail", 1),
}