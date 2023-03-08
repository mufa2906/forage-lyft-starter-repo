from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, array_tire):
        self.array_tire = array_tire

    def needs_service(self):
        if sum(self.array_tire) >= 3:
            return True
        return False
