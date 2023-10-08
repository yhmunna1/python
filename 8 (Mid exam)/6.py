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
            print(f'Your id {id} is not found')
            return
        for row, col in seat_list:
            if 0 <= row < self.rows and 0 <= col < self.cols and self.seats[id][row][col] == 'free':
                self.seats[id][row][col] = 'booked'
                print(f'Seat ({row}, {col}) booked for show {id}')
            else:
                print(f"Seat Number Row-{row}, Column-{col} isn't available.")
    
    def view_show_list(self):
        print('Shows running in this hall:')
        for id, movie_name, time in self.show_list:
            print(f'Movie Name: {movie_name}, Show ID: {id}, Time: {time}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f'Your id {id} is not found')
            return
        print(f'Available seats for the show with ID {id}:')
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 'free':
                    print(f'Seat ({row} {col})')

class Star_Cinema(Hall):
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)



opera_house = Hall(5, 10, 5)

opera_house.entry_show(121, 'Fast X', '4PM')
opera_house.entry_show(122, 'John Wick', '5PM')
opera_house.entry_show(123, 'Spider Man', '6PM')
opera_house.entry_show(124, 'Oppenheimer', '7PM')
opera_house.entry_show(125, 'Mission Impossible', '8PM')


print('1. View All Show Today')
print('2. View Available Seats')
print('3. Book Ticket')
print('4. Exit')
print('Enter Option:')
n = int(input())

if n == 1:
    opera_house.view_show_list()

elif n == 2:
    print('Enter Show ID:')
    s = int(input())
    opera_house.view_available_seats(s)

elif n == 3:
    print('Enter Show ID:')
    book = int(input())
    print('Number of Ticket:')
    ticket = int(input())
    print('Enter Seat Row:')
    row_ticket = int(input())
    print('Enter Seat Column:')
    column_ticket = int(input())

    opera_house.book_seats(book, [(row_ticket, column_ticket)])
elif n== 4:
    pass
else:
    print('Your option in invalid')