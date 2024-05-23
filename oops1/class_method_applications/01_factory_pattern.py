"""Used in some places in our codebase - factory design pattern"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    def __str__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month}, {self.day})"


date = Date.from_string("2023-05-23")
print(date)
