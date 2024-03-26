import random
import string


def gerar_senha_forte(comprimento=12):
    # Define os caracteres a serem utilizados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera uma senha aleatória misturando letras, números e caracteres especiais
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

    return senha


if __name__ == "__main__":
    # Define o comprimento padrão da senha
    comprimento_senha = 12

    # Pede ao usuário para especificar o comprimento da senha desejada
    try:
        comprimento_senha = int(
            input("Digite o comprimento da senha desejada (padrão é 12): "))
    except ValueError:
        print("Entrada inválida. Usando o comprimento padrão de 12 caracteres.")

    # Gera e imprime a senha forte
    senha_forte = gerar_senha_forte(comprimento_senha)
    print("Sua senha forte é:", senha_forte)
