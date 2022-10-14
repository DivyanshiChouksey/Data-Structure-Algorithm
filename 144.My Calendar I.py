# My Calendar I


class MyCalendar:
    def __init__(self):
        self.calender = []

    def book(self, start, end):
        for s, e in self.calender:
            if s < end and start < e:
                return False
        self.calender.append((start, end))
        return True


obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(40, 50))
print(obj.book(20, 30))
