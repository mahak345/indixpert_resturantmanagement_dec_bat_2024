from datetime import datetime, timedelta

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.bookings = []

    def is_available(self, new_time):
        for booking in self.bookings:
            if abs((booking - new_time).total_seconds()) < 2 * 3600:
                return False
        return True

    def book_table(self, booking_time):
        if self.is_available(booking_time):
            self.bookings.append(booking_time)
            print(f"Table {self.table_number} successfully booked for {booking_time.strftime('%Y-%m-%d %H:%M')}.")
        else:
            print (f"Table {self.table_number} is not available within 2 hours of {booking_time.strftime('%H:%M')}.")

    def cancel_booking(self, booking_time):
        for i, booked_time in enumerate(self.bookings):
            if booked_time == booking_time:
                del self.bookings[i]
                print(f"Booking at {booking_time.strftime('%H:%M')} for table {self.table_number} has been canceled.")
                return
        print(f"No booking found at {booking_time.strftime('%H:%M')} for table {self.table_number}.")

class BookingSystem:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def check_availability(self, table_number, booking_time):
        table = self.tables[table_number - 1]
        table.book_table(booking_time)

    def cancel_reservation(self, table_number, booking_time):
        table = self.tables[table_number - 1]
        table.cancel_booking(booking_time)
