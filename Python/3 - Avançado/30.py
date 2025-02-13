def xor_criptografar(mensagem, chave):
    """Criptografa a mensagem usando XOR com a chave fornecida."""
    return "".join(chr(ord(c) ^ ord(chave[i % len(chave)])) for i, c in enumerate(mensagem))

def xor_descriptografar(mensagem_cifrada, chave):
    """Descriptografa a mensagem usando XOR (reversível pela mesma função)."""
    return xor_criptografar(mensagem_cifrada, chave)  # XOR é reversível

# Entrada do usuário
mensagem = input("Digite a mensagem a ser criptografada: ")
chave = input("Digite a chave para criptografia: ")

# Criptografar
mensagem_cifrada = xor_criptografar(mensagem, chave)
print(f"\nMensagem Criptografada: {mensagem_cifrada.encode('utf-8')}")  # Exibe em bytes para evitar caracteres ilegíveis

# Descriptografar
mensagem_decifrada = xor_descriptografar(mensagem_cifrada, chave)
print(f"Mensagem Descriptografada: {mensagem_decifrada}")
