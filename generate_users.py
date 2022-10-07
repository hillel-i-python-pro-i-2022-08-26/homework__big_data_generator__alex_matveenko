import random
from typing import Iterator, Protocol, TypeAlias

from faker import Faker

fake = Faker()

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def validate(users: list[UserProtocol], amount: int) -> None:
    logins = set(map(lambda user: user.login, users))
    if amount != (amount_of_logins := len(logins)):
        raise ValueError(f'Not enough of unique items. Required: "{amount}". Provided: "{amount_of_logins}"')


def generate_users(amount: int) -> Iterator[UserProtocol]:
    login: set[str] = set()
    password: set[str] = set()
    # Generate_info__start
    while len(login) != amount or len(password) != amount:
        fake_name = f"{fake.profile()['username']}_{fake.name().split()[1].lower()}"
        fake_password = f"{fake.password()}{random.randint(1, 9999)}"
        # Generate_info__stop

        login.add(fake_name)
        password.add(fake_password)

    for name, pas in zip(login, password):
        yield Person(login=name, password=pas)


def main():
    amount = 100_000
    users = list(generate_users(amount=amount))
    validate(users=users, amount=amount)


if __name__ == "__main__":
    main()
