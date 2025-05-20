import json
import os
import logging
from datetime import datetime

BOOKING_DB = os.path.join(os.path.dirname(__file__),"../../logs/Database/booking.json")
LOG_FILE = os.path.join(os.path.dirname(__file__),"../../logs/restaurant.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def table_booking():
    name = input("Enter your name: ").strip()
    people = input("Number of people: ").strip()
    date = input("Enter booking date (YYYY-MM-DD): ").strip()
    time = input("Enter booking time (HH:MM): ").strip()

    if not people.isdigit() or int(people) <= 0:
        print("Invalid number of people.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time, "%H:%M")
    except ValueError:
        print("Invalid date or time format.")
        return

    booking = {
        "name": name,
        "people": int(people),
        "date": date,
        "time": time
    }
    bookings = []
    if os.path.exists(BOOKING_DB):
        with open(BOOKING_DB, 'r') as f:
            try:
                bookings = json.load(f)
            except json.JSONDecodeError:
                bookings = []
    bookings.append(booking)

    with open(BOOKING_DB, 'w') as f:
        json.dump(bookings, f, indent=4)

    print(" Table booked successfully!")
    logging.info(f"New booking: {booking['name']} for {booking['people']} people on {booking['date']} at {booking['time']}.")

