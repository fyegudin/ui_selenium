from faker import Faker

faker_en = Faker('En')


class Data:
    username: str = None


def generate_data(Data):
    return Data(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        username=faker_en.email()
    )
