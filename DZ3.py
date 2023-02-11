class people:
    def __init__(self, name='people'):
        self.name = name

class auto:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, people):
        if len(self.passengers) < self.capacity:
            self.passengers.append(people)
        else:
            print('no free seats')

    def print_all_passengers(self):
        if self.passengers != []:
            print(f"There are {len(self.passengers)} passengers in {self.brand}")
            for pas in self.passengers:
                print(pas.name)
            else:
                print(f"no passengers in {self.brand}")
