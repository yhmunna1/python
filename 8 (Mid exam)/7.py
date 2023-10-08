class Hall:
    def __init__(self, hall_no, rows, cols) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.hall_list.append(self)
        # print(f'Hall {hall_num} added')

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats = [["free" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f'Your id {id} is not found')
            return
        for row, col in seat_list:
            if 0 <= row < self.rows and 0 <= col < self.cols and self.seats[id][row][col] == 'free':
                self.seats[id][row][col] = 'booked'
                print(f'Booked: Row-{row}, Column-{col}')
            else:
                print(f"Seat Number Row-{row}, Column-{col} isn't available.")
    
    def view_show_list(self):
        for id, movie_name, time in self.show_list:
            print(f'ID: {id}, Movie: {movie_name}, Time: {time}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f'Your id {id} is not found')
            return
        print(f'Available seats for the show with ID {id}:')
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 'free':
                    print(f'Row {row}, Column {col}')

class Star_Cinema(Hall):
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Star_Cinema(Hall):
    hall_list = []

class Counter:
    def __init__(self, cinema):
        self.cinema = cinema

    def view_all_shows(self):
        for hall in Star_Cinema.hall_list:
            hall.view_show_list()

    def view_available_seats(self, hall_no, show_id):
        hall = None
        for h in Star_Cinema.hall_list:
            if h.hall_no == hall_no:
                hall = h
                break

        if hall:
            hall.view_available_seats(show_id)
        else:
            print(f'Hall with number {hall_no} not found.')

    def book_tickets(self, hall_no, show_id, seat_list):
        hall = None
        for h in Star_Cinema.hall_list:
            if h.hall_no == hall_no:
                hall = h
                break

        if hall:
            hall.book_seats(show_id, seat_list)
        else:
            print(f'Hall with number {hall_no} not found.')


# Star_Cinema.entry_hall(beauty)

beauty = Hall(1, 8, 4)
aviruchi = Hall(2, 10, 5)


aviruchi.entry_show(101, "Jawan", "7PM")
aviruchi.entry_show(102, "Spider Man", "10PM")
aviruchi.entry_show(103, "Mission Impossible", "9PM")
# print(aviruchi.show_list)

counter = Counter(Star_Cinema)
counter.view_all_shows()

counter.view_available_seats(2, 101)

counter.book_tickets(2, 101, [(0,0)])

counter.view_available_seats(2, 101)

counter.book_tickets(2, 101, [(0,0)])

# aviruchi.book_seats(124, [(1, 2)])
# print(aviruchi.seats)

# aviruchi.view_show_list()
# aviruchi.view_available_seats(124)

print('1. View All Show Today')
print('2. View Available Seats')
print('3. Book Ticket')
print('4. Exit')
n = int(input())

print(n)