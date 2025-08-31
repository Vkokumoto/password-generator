import random
import string

def generate_password(length: int = 12) -> str:
    if length < 8:
        raise ValueError("A senha precisa ter pelo menos 8 caracteres.")
    
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%&*")

    if length > 4:
        others = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%&*") for _ in range (length - 4))
    else:
        others = ''    
    
    password = lower + upper + digit + special + others

    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)