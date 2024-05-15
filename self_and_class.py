'''Use of self within the class'''

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def weekly_pay(self):
        return self.pay / 52
    def monthly_pay(self, weeks_in_month):
        return (self.pay / 52) * weeks_in_month
    # this very intentionally is meant to break
    def will_break(weeks_in_month):
        return self.pay / 52 * weeks_in_month

donnie = Employee("donnie", 52000)
print(donnie.weekly_pay())
print(donnie.monthly_pay(4))
#notice that self is REQUIRED
print(donnie.will_break(4))
    
