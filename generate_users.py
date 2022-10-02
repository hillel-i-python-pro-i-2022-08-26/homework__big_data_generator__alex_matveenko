import random
from typing import Iterator

from faker import Faker

fake = Faker()


# Version_use_set_for_generate
def big_data_generator__set(number: int) -> Iterator:
    username: set[str] = set()
    user_password: set[str] = set()
    while len(username) != number and len(user_password) != number:
        fake_name = (
            f"{fake.name().split()[0].lower()}_{random.randint(1, 9999)}_"
            f"{fake.name().split()[1].lower()}_{random.randint(1, 9999)} "
        )
        fake_password = f"{fake.password()}{random.randint(0, 1000)}{fake.password()}"
        username.add(fake_name)
        user_password.add(fake_password)
    for count, (name, password) in enumerate(zip(username, user_password), start=1):
        yield f"{count}. Login: {name}. Pass: {password}"


# Version_use_list_for_generate_and_count_repeats
def big_data_generator__list(number: int) -> Iterator:
    username: list[str] = []
    user_password: list[str] = []
    repeat_names: int = 0
    repeat_password: int = 0
    for login in range(number):
        login = f"{fake.first_name().lower()}_{random.randint(1, 9999)}_{fake.name().split()[1].lower()}"
        if login in username:
            login += f"{random.randint(1, 9999)}"
            repeat_names += 1
        username.append(login)
    for password in range(number):
        password = f"{fake.password()}{random.randint(0, 1000)}"
        if password in user_password:
            password += f"{fake.password().reverse}{random.randint(0, 1000)}"
            repeat_password += 1
        user_password.append(password)

    for item, (name, password) in enumerate(zip(username, user_password), start=1):
        yield f"{item}.Login:{name}. Pass:{password}\nLogin repeat:{repeat_names}.Password repeat:{repeat_password}"


# Organize_output_for_set_version
def output_data__set(amount: int) -> str:
    data = big_data_generator__set(amount)
    return "\n".join([f"{item}" for item in data])


# Organize_output_for_list_version
def output_data__list(amount: int) -> str:
    data = big_data_generator__list(amount)
    return "\n".join([f"{item}" for item in data])


if __name__ == "__main__":
    # Version with set
    print(output_data__set(1), end="\n\n")  # Add "end" for readability
    # Version with list(much longer)
    print(output_data__list(1))
