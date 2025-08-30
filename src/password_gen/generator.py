import random
import string

def generate_password(length: int = 12) -> str:
    if length < 8:
        raise ValueError("A senha precisa ter pelo menos 8 caracteres.")
    
    # lembrando: string.ascii_letters (todas as letras maiúsculas e minúsculas) e string.digits (zero a nove)
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    password = "".join(random.choice(chars) for _ in range(length))
    return password