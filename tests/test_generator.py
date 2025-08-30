import pytest 
from password_gen import generate_password

def test_generate_password_default_length():
    password = generate_password()
    assert len(password) == 12
    assert any(c.islower() for c in password) # maiúscula
    assert any(c.isupper() for c in password) # minúscula
    assert any(c.isdigit() for c in password) # número
    assert any(c in "!@#$%&*" for c in password) # caractere especial

def test_generate_password_custom_length():
    password = generate_password(20)
    assert len(password) == 20

def test_generate_password_invalid_length():
    with pytest.raises(ValueError):
        generate_password(5) # menor que 8 tem que falhar