class ORMModelMeta(type):
    def __new__(cls, name, bases, dct):
        if "table_name" not in dct:
            dct["table_name"] = name.lower()  # Default table name based on class name
        return super().__new__(cls, name, bases, dct)


class User(metaclass=ORMModelMeta):
    table_name = "users"  # Override default table name


class Student(metaclass=ORMModelMeta):
    pass


# Now User class can be used in an ORM-like fashion with a table_name attribute
print(User.table_name)  # Outputs: 'users'
print(Student.table_name)  # Outputs: 'student'
