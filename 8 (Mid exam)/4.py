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

class Star_Cinema(Hall):
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


# beauty = Star_Cinema(5)
# Star_Cinema.entry_hall(beauty)
aviruchi = Hall(5, 10, 5)
print(f'Hall No: {aviruchi.hall_no}, Columns: {aviruchi.cols}, Rows: {aviruchi.rows}')


aviruchi.entry_show(124, "Jawan", "7PM")
print(aviruchi.show_list)
# print(aviruchi.seats)

# aviruchi.book_seats(124, [(0,0), (0,1), (1,1)])
aviruchi.book_seats(124, [(1, 2)])
aviruchi.book_seats(124, [(1, 2)])
# print(aviruchi.seats)