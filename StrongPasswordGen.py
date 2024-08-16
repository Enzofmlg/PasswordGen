import secrets
import string

def generate_secure_password(length=12):
    # Conjunto de caracteres para a senha
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Garantir que a senha tenha pelo menos um de cada tipo de caractere
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    
    # Completar a senha com caracteres aleatórios
    password += [secrets.choice(alphabet) for _ in range(length - 4)]
    
    # Embaralhar os caracteres para garantir a aleatoriedade
    secrets.SystemRandom().shuffle(password)
    
    # Converter a lista de caracteres em uma string
    return ''.join(password)

# Gerar uma senha de 12 caracteres
password = generate_secure_password(12)
print("Generated password:", password)
