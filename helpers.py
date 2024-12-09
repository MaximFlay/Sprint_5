import random
from faker import Faker


class UserData:
    @staticmethod
    def generate_user_data():
        full_name = Faker('en_US').name()
        temp = full_name.split()
        name = temp[0]
        surname = temp[1]
        number = str(random.randint(1000, 9999))
        domain = Faker('ru_RU').domain_name()
        username_template = name + random.choice([surname, number])
        email_template = name + surname + number + '@' + domain
        password_template = str(Faker().password())
        user_data = {
            'username': username_template,
            'email': email_template,
            'password': password_template
        }
        return user_data


class Userinfo(UserData):
    userinfo = UserData.generate_user_data()
    username = str(userinfo['username'])
    email = str(userinfo['email'])
    password = str(userinfo['password'])








