import json
import random

mails = (
    "mail.ru",
    "inbox.ru",
    "list.ru",
    "bk.ru",
    "ya.ru",
    "yandex.com",
    "yandex.ua",
    "yandex.ru",
    "gmail.com"
)


# Get random service
def random_service(list):
    return random.choice(list)

# Create random name
def random_name():
    with open("tools/SMS/names.json", 'r') as names:
        names = json.load(names)["names"]
    return random.choice(names)

# Create random suffix for email
# %random_name%SUFFIX@%random_email%
def random_suffix(int_range = 4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)


# Create random email by name, suffix, mail
# Example: Jefferson3715@gmail.com
def random_email():
    return random_name() + random_suffix() + "@" + random.choice(mails)

# Create random password
# %random_name%%random_suffix%
def random_password():
    return random_name() + random_suffix(int_range = 10)

# Get random user agent
def random_useragent():
    with open("tools/SMS/user_agents.json", 'r') as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)