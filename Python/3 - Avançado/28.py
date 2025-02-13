import re

def validar_senha(senha):
    """
    Valida uma senha forte com os seguintes critérios:
    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    - Pelo menos um caractere especial (!@#$%^&*()-+)
    """
    padrao = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if re.match(padrao, senha):
        return True
    return False

# Entrada do usuário
senha = input("Digite sua senha: ")

# Validação
if validar_senha(senha):
    print("Senha forte! ✅")
else:
    print("Senha fraca! ❌ Certifique-se de que sua senha contém:\n"
          "- Pelo menos 8 caracteres\n"
          "- Uma letra maiúscula\n"
          "- Uma letra minúscula\n"
          "- Um número\n"
          "- Um caractere especial (!@#$%^&*()-+)")
