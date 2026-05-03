import os
import psycopg2
import requests
import yaml
from psycopg2.extras import Json

import config.constants as C

def get_conn():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="weather_db",
        user="postgres",
        password="YOUR_PASSWORD"
    )

def insert_raw(record):
    sql = """
        INSERT INTO bronze_weather_raw
        (provider, region_id, point_name, lat, lon, start_date, end_date, request_url, http_status, payload)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (
                record["provider"],
                record["region_id"],
                record["point_name"],
                record["lat"],
                record["lon"],
                record["start_date"],
                record["end_date"],
                record["request_url"],
                record["http_status"],
                Json(record["payload"])
            ))
        conn.commit()

def fetch_historical(lat, lon, start_date, end_date):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": C.HOURLY_VARIABLES_STR,
        "timezone": "UTC"
    }

    r = requests.get(C.BASE_URL, params=params, timeout=60)

    return {
        "request_url": r.url,
        "status": r.status_code,
        "data": r.json()
    }

def load_regions(path="config/regions.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)["regions"]