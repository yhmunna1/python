
class Gadget:
    def __init__(self, brand, price, color,) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Running laptop: {self.brand}'

class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'learning python and practicing'
    
class Phone(Gadget):
    def __init__(self, dual_sim) -> None:
        self.dual_sim = dual_sim
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass
