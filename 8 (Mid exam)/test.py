class Hall:
    def __init__(self, hall_no, rows, cols) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats = [["free" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f"Error: Show with id {id} not found.")
            return

        for row, col in seat_list:
            if (
                0 <= row < self.rows
                and 0 <= col < self.cols
                and self.seats[id][row][col] == "free"
            ):
                self.seats[id][row][col] = "booked"
                print(f"Booked seat: Row {row}, Column {col}")
            else:
                print(f"Seat Row {row}, Column {col} is not available or already booked.")

class Star_Cinema(Hall):
    hall_list = []

# Creating an instance of Hall
aviruchi = Hall(5, 10, 5)
print(f'Hall No: {aviruchi.hall_no}, Columns: {aviruchi.cols}, Rows: {aviruchi.rows}')

# Adding a show to the hall
aviruchi.entry_show(123, "Jawan", "7PM")

# Printing show_list and seats for the hall
print(aviruchi.show_list)
print(aviruchi.seats)

# Booking seats for the show with id 123
aviruchi.book_seats(123, [(0, 0), (0, 1), (1, 1)])
aviruchi.book_seats(123, [(0, 0), (0, 1), (1, 1)])  # Attempting to book the same seats again
