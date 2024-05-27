class Person:
    def identity(self):
        print(f"I am an Indian")


class Keralite(Person):
    def identity(self):
        print(f"I am an Keralite")


class Karnataka(Person):
    def identity(self):
        print(f"I am a kannadiga")


class Banglorean(Karnataka, Keralite):
    def identity(self):
        print(f"I am a kannadiga")


class Hyderabadian(Banglorean):
    def identity(self):
        print(f"I am a Hyderabadian")


print(Banglorean.__mro__)
print(Hyderabadian.__mro__)
print(Hyderabadian.mro())
