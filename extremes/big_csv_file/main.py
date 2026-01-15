import json

with open("aggerate_data.json", mode="r") as json_file:
    aggerate_data = json.load(json_file)
    aggerate_by_station = {}

    for file in aggerate_data:
        for station in aggerate_data[file]:
            if station not in aggerate_by_station:
                aggerate_by_station[station] = {
                    "total_temp": 0,
                    "count": 0,
                    "max_temp": float("-inf"),
                    "min_temp": float("inf"),
                }
            aggerate_by_station[station]["total_temp"] += aggerate_data[file][station][
                "total_temp"
            ]
            aggerate_by_station[station]["count"] += aggerate_data[file][station][
                "count"
            ]
            aggerate_by_station[station]["max_temp"] = max(
                aggerate_by_station[station]["max_temp"],
                aggerate_data[file][station]["max_temp"],
            )
            aggerate_by_station[station]["min_temp"] = min(
                aggerate_by_station[station]["min_temp"],
                aggerate_data[file][station]["min_temp"],
            )


with open("final_aggregated_data.json", mode="w") as output_file:
    aggerate_by_station = {
        station: {**data, "average_temp": data["total_temp"] / data["count"]}
        for station, data in aggerate_by_station.items()
    }
    aggerate_by_station = {
        station: {**data, "mean_temp": (data["max_temp"] + data["min_temp"]) / 2}
        for station, data in aggerate_by_station.items()
    }

    json.dump(aggerate_by_station, output_file, indent=4)
