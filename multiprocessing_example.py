import multiprocessing
import time

# Função para o primeiro processo
def task1():
    for x in range(6):
        print('Processo 1 está executando')
        time.sleep(1)  # Simula uma pausa para visualizar a execução simultânea

# Função para o segundo processo
def task2():
    for x in range(6):
        print('Processo 2 está executando')
        time.sleep(1)

if __name__ == "__main__":
    # Criando os processos
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # Iniciando os processos
    p1.start()
    p2.start()

    # Aguardando a conclusão dos processos
    p1.join()
    p2.join()

    print("Ambos os processos foram concluídos")
