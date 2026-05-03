from module.helper_functions import load_regions, fetch_historical, insert_raw
import config.constants as C

regions = load_regions()

for region_id, region in regions.items():
    for point in region["points"]:
        print(f"Fetching {region_id} - {point['name']}")

        result = fetch_historical(
                lat=point["lat"],
                lon=point["lon"],
                start_date=C.START_DATE,
                end_date=C.END_DATE
            )

        record = {
                "provider": "open-meteo",
                "region_id": region_id,
                "point_name": point["name"],
                "lat": point["lat"],
                "lon": point["lon"],
                "start_date": C.START_DATE,
                "end_date": C.END_DATE,
                "request_url": result["request_url"],
                "http_status": result["status"],
                "payload": result["data"]
            }

        insert_raw(record)