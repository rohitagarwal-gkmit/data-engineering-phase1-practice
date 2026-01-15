import csv
import os
import json
import time
import psutil

# break into batches of 500,000 rows with header in every file
BATCH_SIZE = 500000
FOLDER_PATH = "batches/"
aggerate = {}
os.makedirs(FOLDER_PATH, exist_ok=True)


def process_row():
    with open("measurements.txt", mode="r") as file:
        BATCH_NUMBER = 1

        reader = csv.reader(file)
        header = next(reader)  # Read the header row

        batch_rows = []

        for row in reader:
            batch_rows.append(row)

            if len(batch_rows) == BATCH_SIZE:
                with open(
                    f"{FOLDER_PATH}/measurements_batch_{BATCH_NUMBER}.csv",
                    mode="w",
                    newline="",
                ) as batch_file:
                    writer = csv.writer(batch_file)
                    writer.writerow(header)  # Write the header
                    writer.writerows(batch_rows)  # Write the batch rows

                BATCH_NUMBER += 1
                batch_rows = []

        # Write any remaining rows in the last batch
        if batch_rows:
            with open(
                f"{FOLDER_PATH}/measurements_batch_{BATCH_NUMBER}.csv",
                mode="w",
                newline="",
            ) as batch_file:
                writer = csv.writer(batch_file)
                writer.writerow(header)  # Write the header
                writer.writerows(batch_rows)  # Write the remaining rows


def process_data():
    for file in os.listdir(FOLDER_PATH):
        file_start = time.time()
        with open(f"{FOLDER_PATH}/{file}", mode="r") as batch_file:
            aggerate[file] = {}
            reader = csv.DictReader(batch_file, delimiter=";")

            for row in reader:
                station = row["station"]
                temp = float(row["temp"])

                if station not in aggerate[file]:
                    aggerate[file][station] = {
                        "total_temp": 0,
                        "count": 0,
                        "max_temp": 0,
                        "min_temp": 0,
                        "average_temp": 0,
                    }

                aggerate[file][station]["total_temp"] += temp
                aggerate[file][station]["count"] += 1
                aggerate[file][station]["max_temp"] = max(
                    aggerate[file][station]["max_temp"], temp
                )
                aggerate[file][station]["min_temp"] = min(
                    aggerate[file][station]["min_temp"], temp
                )
                aggerate[file][station]["average_temp"] = (
                    aggerate[file][station]["total_temp"]
                    / aggerate[file][station]["count"]
                )
        file_end = time.time()
        print(f"Processed {file} in {file_end - file_start:.2f} seconds")
        current_memory = psutil.Process().memory_info().rss / 1024 / 1024
        print(f"Current memory usage: {current_memory:.2f} MB")


if __name__ == "__main__":
    start_time = time.time()

    # print("Starting batch creation...")
    # batch_start = time.time()
    # process_row()
    # batch_end = time.time()
    # print(f"Batch creation time: {batch_end - batch_start:.2f} seconds")
    # current_memory = psutil.Process().memory_info().rss / 1024 / 1024
    # print(f"Current memory usage: {current_memory:.2f} MB")

    print("Starting data processing...")
    process_start = time.time()
    process_data()
    process_end = time.time()
    print(f"Data processing time: {process_end - process_start:.2f} seconds")
    current_memory = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Current memory usage: {current_memory:.2f} MB")

    print("Starting JSON writing...")
    json_start = time.time()
    with open("aggerate_data.json", mode="w") as json_file:
        json.dump(aggerate, json_file)
    json_end = time.time()
    print(f"JSON writing time: {json_end - json_start:.2f} seconds")
    current_memory = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Current memory usage: {current_memory:.2f} MB")

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
    print(f"Final memory usage: {current_memory:.2f} MB")
