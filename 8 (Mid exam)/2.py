class Hall:
    def __init__(self, hall_no, rows, cols) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.hall_list.append(self)
        # print(f'Hall {hall_num} added')

class Star_Cinema(Hall):
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


# beauty = Star_Cinema(5)
# Star_Cinema.entry_hall(beauty)

aviruchi = Hall(5, 10, 5)

print(f'Hall No: {aviruchi.hall_no}, Columns: {aviruchi.cols}, Rows: {aviruchi.rows}')