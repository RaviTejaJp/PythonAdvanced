from faker import Faker


class FakeDataGenerator:
    def __init__(self, locale="en_US"):
        self.fake = Faker(locale)

    def generate_personal_info(self):
        return {
            "name": self.fake.name(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "ssn": self.fake.ssn(),
            "date_of_birth": self.fake.date_of_birth(),
        }

    def generate_contact_info(self):
        return {
            "phone_number": self.fake.phone_number(),
            "address": self.fake.address(),
            "email": self.fake.email(),
        }

    def generate_business_info(self):
        return {
            "company": self.fake.company(),
            "job": self.fake.job(),
            "bs": self.fake.bs(),
        }

    def generate_internet_data(self):
        return {
            "url": self.fake.url(),
            "ipv4": self.fake.ipv4(),
            "email": self.fake.email(),
        }

    def generate_date_time_data(self):
        return {
            "date": self.fake.date(),
            "time": self.fake.time(),
            "date_time": self.fake.date_time(),
        }

    def generate_text_data(self):
        return {
            "text": self.fake.text(),
            "sentence": self.fake.sentence(),
            "paragraph": self.fake.paragraph(),
        }

    def generate_misc_data(self):
        return {
            "uuid4": self.fake.uuid4(),
            "color_name": self.fake.color_name(),
            "currency_name": self.fake.currency_name(),
        }

    def generate_all_data(self):
        return {
            "personal_info": self.generate_personal_info(),
            "contact_info": self.generate_contact_info(),
            "business_info": self.generate_business_info(),
            "internet_data": self.generate_internet_data(),
            "date_time_data": self.generate_date_time_data(),
            "text_data": self.generate_text_data(),
            "misc_data": self.generate_misc_data(),
        }


# Example usage
fake_data_gen = FakeDataGenerator()

# Generate all kinds of fake data
all_data = fake_data_gen.generate_all_data()

# Print the generated data
for category, data in all_data.items():
    print(f"--- {category.replace('_', ' ').title()} ---")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()
