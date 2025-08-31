from src.password_gen.generator import generate_password

def main():
    print("---- Gerador de senhas ----")
    try:
        length = int(input("Digite o tamanho da senha (mínimo 8 caracteres): "))
        password = generate_password(length)
        print(f"Sua senha gerada é: {password}")
    except ValueError as e:
        print(f"Erro: {e} Tente novamente")

if __name__ == "__main__":
    main()