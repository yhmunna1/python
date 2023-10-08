
class Hall:
    def __init__(self, hall_no) -> None:
        self.hall_no = hall_no
        print(f'Hall {hall_no} added')

class Star_Cinema(Hall):
    hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


beauty = Star_Cinema(5)
Star_Cinema.entry_hall(beauty)