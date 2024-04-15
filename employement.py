class Employees:
    def __init__(self, name , last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_requests(self, days):
        return "May i take leave for " + str(days) + " days."


paras = Supervisors("Paras ", "P", "apple")

badal = Chefs("Badal ", "B")

barsha = Chefs("Barsha ", "B")

print(badal.leave_requests(4))
print(paras.password)
print(barsha.last)