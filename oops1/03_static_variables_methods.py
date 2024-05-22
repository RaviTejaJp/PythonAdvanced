class Office:
    Industry = "Technology"

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def calculate_area(length, width):
        return length * width

    @classmethod
    def change_industry(cls, name: str) -> None:
        cls.Industry = name

    def dimensions_details(self, height: float, width: float, length: float) -> None:
        # Instances variables defined
        self.height = height
        self.width = width
        self.length = length
        self.area = self.calculate_area(width=width, length=length)
        self.area = Office.calculate_area(width=width, length=length)

    def __str__(self) -> str:
        return self.__class__.__name__ + "('" + self.name + "')"


openmynz_office = Office(name="Openmynz")
openmynz_office.dimensions_details(height=6, width=50, length=150)
atx_office = Office(name="ATX")
Office.dimensions_details(atx_office, height=10, width=150, length=250)

print(openmynz_office.__dict__)
print(atx_office.__dict__)
