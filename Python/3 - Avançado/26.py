import threading
import time

def contagem_regressiva(nome, inicio):
    """Executa uma contagem regressiva a partir do valor especificado."""
    for i in range(inicio, -1, -1):
        print(f"{nome}: {i}")
        time.sleep(1)  # Aguarda 1 segundo entre as contagens

# Criando duas threads para as contagens regressivas
thread1 = threading.Thread(target=contagem_regressiva, args=("Contagem 10", 10))
thread2 = threading.Thread(target=contagem_regressiva, args=("Contagem 20", 20))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguarda a finalização das duas threads
thread1.join()
thread2.join()

print("Ambas as contagens regressivas terminaram!")
