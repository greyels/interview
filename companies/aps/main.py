import datetime
import sys
import time

from companies.aps.api import fetch_data
from companies.aps.db import EarthquakeDataInserter
from companies.aps.helpers import log_magnitudes
from companies.aps.logging_conf import logger


def get_earthquake_data(start, end, threshold):
    data = fetch_data(start, end)
    log_magnitudes(data, threshold)
    EarthquakeDataInserter().insert_features(data)


def main(mag_threshold):
    current_date = datetime.datetime.now().date()
    three_years_ago = current_date - datetime.timedelta(days=365 * 3)
    get_earthquake_data(three_years_ago, current_date, mag_threshold)

    while True:
        time.sleep(24 * 60 * 60)
        current_date = datetime.datetime.now().date()
        one_day_ago = current_date - datetime.timedelta(days=1)
        get_earthquake_data(one_day_ago, current_date, mag_threshold)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("No magnitude threshold provided! Please provide magnitude threshold as an argument.")
        sys.exit(1)  # Exit the script with an error code
    mag_threshold = sys.argv[1]
    try:
        mag_threshold = float(mag_threshold)
    except ValueError:
        logger.error(f"Provided magnitude threshold '{mag_threshold}' is not valid!")
        raise Exception
    main(mag_threshold)
