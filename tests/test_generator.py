import pytest 
from password_gen import generate_password

# Teste 1
def test_generate_password_default_length():
    password = generate_password()
    assert len(password) == 12
    assert any(c.islower() for c in password) # maiúscula
    assert any(c.isupper() for c in password) # minúscula
    assert any(c.isdigit() for c in password) # número
    assert any(c in "!@#$%&*" for c in password) # caractere especial

# Teste 2
def test_generate_password_custom_length():
    password = generate_password(20)
    assert len(password) == 20

# Teste 3
def test_generate_password_invalid_length():
    with pytest.raises(ValueError):
        generate_password(5) # menor que 8 tem que falhar

# Teste 4
def test_generate_password_contains_special_character():
    for _ in range(50):
        password = generate_password()
        if any(c in "!@#$%&" for c in password):
            break
    else:
        pytest.fail("Nenhuma senha continha caractere especial após as tentativas")


# Teste 5
def test_generate_password_very_long():
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2

# Teste 6    
def test_generate_password_min_length_valid():
    password = generate_password(8)
    assert len(password) == 8