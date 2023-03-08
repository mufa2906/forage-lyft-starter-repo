from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, array_tire):
        self.array_tire = array_tire

    def needs_service(self):
        for tire in self.array_tire:
            if tire >= 0.9:
                return True
        return False
