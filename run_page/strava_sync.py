import argparse
import json

from config import JSON_FILE, SQL_FILE
from generator import Generator


# for only run type, we use the same logic as garmin_sync
def run_strava_sync(client_id, client_secret, refresh_token, only_ride=False):
    generator = Generator(SQL_FILE)
    generator.set_strava_config(client_id, client_secret, refresh_token)
    # if you want to refresh data change False to True
    generator.only_ride = only_ride
    generator.sync(False)

    activities_list = generator.load()
    with open(JSON_FILE, "w") as f:
        json.dump(activities_list, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="strava client id")
    parser.add_argument("client_secret", help="strava client secret")
    parser.add_argument("refresh_token", help="strava refresh token")
    parser.add_argument(
        "--only-ride",
        dest="only_ride",
        action="store_true",
        help="if is only for cycling",
    )
    options = parser.parse_args()
    run_strava_sync(
        options.client_id,
        options.client_secret,
        options.refresh_token,
        only_ride=options.only_ride,
    )
