import csv
import os


def save_to_csv(data, filename):
    os.makedirs("data", exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "title", "price", "url", "image", "status"
        ])

        writer.writeheader()

        for row in data:
            writer.writerow(row)