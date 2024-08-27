print("Alô Mundo \nSemana Estatistica")

"""
    Um professor precisa sortear bombons para diversos alunos.
    Esses alunos serao sorteados randonicamente.
    O numero deve corresponder ao numero do diario.

    """
import random

# looping - iteração - repetiçao - laço
while True:

    sorteio_turma  = random.randint(1,25)
    print(sorteio_turma)
    resposta = input("Deseja sortear outro numero? (s/n)").strip().lower()
    
    if (resposta != "s"):
        print("encerrando o sorteio")
        break

