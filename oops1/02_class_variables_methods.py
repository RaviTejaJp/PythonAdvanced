class Office:
    Industry = "Technology"

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def change_industry(cls, name: str) -> None:
        cls.Industry = name

    def dimensions_details(self, height: float, width: float, length: float) -> None:
        # Instances variables defined
        self.height = height
        self.width = width
        self.length = length

    def __str__(self) -> str:
        return self.__class__.__name__ + "('" + self.name + "')"


openmynz_office = Office(name="Openmynz")
openmynz_office.dimensions_details(height=6, width=50, length=150)
atx_office = Office(name="ATX")
Office.dimensions_details(atx_office, height=10, width=150, length=250)

print(f"Class variable access via class - {Office.Industry}")
print(f"Class Variable access via instance - {openmynz_office.Industry}")

# instance modifying class variables
atx_office.Industry = "Video Technology"
print(f"After instance modification - {atx_office.Industry}")
print(f"After instance modification - {Office.Industry}")


Office.Industry = "Information and Technology"
print(Office.Industry)
print(openmynz_office.Industry)
