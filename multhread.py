import threading
import time

# Função para a primeira thread
def task1():
    for x in range(6):
        print('Thread 1 está executando')
        time.sleep(1)  # Simula uma pausa para visualizar a execução simultânea

# Função para a segunda thread
def task2():
    for x in range(6):
        print('Thread 2 está executando')
        time.sleep(1)

# Criando as threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Iniciando as threads
t1.start()
t2.start()

# Aguarda todas as threads terminarem antes de continuar
t1.join()
t2.join()

print("Ambas as threads foram concluídas")
