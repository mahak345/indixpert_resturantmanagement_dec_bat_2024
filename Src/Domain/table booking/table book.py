from datetime import datetime, timedelta

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_booked = False
        self.booking_time = None
    
    def book_table(self, booking_time):
        if not self.is_booked or (self.booking_time and self.booking_time <= datetime.now()):
            self.is_booked = True
            self.booking_time = booking_time
            print(f"Table {self.table_number} successfully booked for {booking_time}.")
        else:
            print(f"Table {self.table_number} is already booked for the next 2 hours.")
    
    def cancel_booking(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Table {self.table_number} booking has been canceled.")
        else:
            print(f"Table {self.table_number} is not booked.")

class BookingSystem:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def check_availability(self, table_number, booking_time):
        table = self.tables[table_number - 1]
        if not table.is_booked:
            table.book_table(booking_time)
        else:
            print(f"Table {table_number} is not available for the selected time.")
        
    def cancel_reservation(self, table_number):
        table = self.tables[table_number - 1]
        table.cancel_booking()

def main():
    booking_system = BookingSystem(5)

    while True:
        print("\nTable Booking System")
        print("1. Book a table")
        print("2. Cancel a reservation")
        print("3. Exit")
        choice = input("Please enter your choice (1/2/3): ")

        if choice == '1':
            table_number = int(input("Enter the table number you want to book: "))
            if table_number < 1 or table_number > 5:
                print("Invalid table number. Please choose a table between 1 and 5.")
                continue
            booking_time_str = input("Enter the booking time (HH:MM): ")
            try:
                now = datetime.now()
                booking_time = datetime.strptime(booking_time_str, "%H:%M").replace(
                    year=now.year, month=now.month, day=now.day)
                if booking_time < now:
                    booking_time += timedelta(days=1)  # If time is in the past, schedule for the next day
                booking_system.check_availability(table_number, booking_time)
            except ValueError:
                print("Invalid time format. Please use HH:MM format.")
        
        elif choice == '2':
            table_number = int(input("Enter the table number to cancel: "))
            if table_number < 1 or table_number > 5:
                print("Invalid table number. Please choose a table between 1 and 5.")
                continue
            booking_system.cancel_reservation(table_number)
        
        elif choice == '3':
            print("Thank you for using the Table Booking System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
