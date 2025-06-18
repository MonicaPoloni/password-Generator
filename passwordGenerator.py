import random
from time import sleep

listaNomes1 = ['feliz', 'grande', 'verde',]
listaNomes2 = ["casa", "sol", "livro",]
simbolos = ['!', '@', '#', '$', '%', '&', '*']

regraSenhas = {
    'baixo': {
        'num_palavras': 3,
        'incluir_numeros': False,
        'incluir_simbolos': False
    },
    'medio': {
        'num_palavras': 4,
        'incluir_numeros': True,
        'incluir_simbolos': False
    },
    'alto': {
        'num_palavras': 5,
        'incluir_numeros': True,
        'incluir_simbolos': True
    }
}
# Menu:
rodando = True
while rodando:
    sleep(0.2)
    print('\n----- GERADOR DE SENHAS -----')
    print('1. Gerar Senha')
    print('2. Sair')
    print('----------------------------')
    opcao = int(input('Escolha uma opção [1 | 2]: '))


    if opcao == 1:
        sleep(0.5)
        print('\n--- GERAR SENHA ---')
        nivelDif = input('Qual o nível de dificuldade?: [BAIXO | MÉDIO | ALTO]: ').lower()

        # Verifica se o nível existe no dicionário
        if nivelDif in regraSenhas:
            # Se existe, obtém as regras específicas para este nível
            regrasAtuais = regraSenhas[nivelDif]
            partesDaSenha = []
            # Loop para adicionar o número de palavras 'num_palavras'
            for _ in range(regrasAtuais['num_palavras']):
                # Escolhe entre listaNomes1 e listaNomes2
                if random.choice([True, False]):
                    partesDaSenha.append(random.choice(listaNomes1).title())
                else:
                    partesDaSenha.append(random.choice(listaNomes2).title())
            # Verifica se deve incluir números
            if regrasAtuais['incluir_numeros']:
                # Gera um número aleatório (entre 0 e 9) e o adiciona como string
                numeroAleatorio = str(random.randint(0, 9))
                partesDaSenha.append(numeroAleatorio)
            # Verifica se deve incluir símbolos 'incluir_simbolos'
            if regrasAtuais['incluir_simbolos']:
                # Escolhe um símbolo aleatório da sua lista 'simbolos'
                simbolo_aleatorio = random.choice(simbolos)
                partesDaSenha.append(simbolo_aleatorio)
            # Embaralha todas as partes
            random.shuffle(partesDaSenha)
            # Junta todas as partes da lista em uma única string, usando o '-' para separae
            senha_final = "-".join(partesDaSenha)
             # Exibe a senha gerada
            print(f'\nSua senha [{nivelDif.upper()}] é: {senha_final}')
            sleep(1)

        else:
            print('Nível de dificuldade inválido. Tente BAIXO, MÉDIO ou ALTO.')
            sleep(1)
    elif opcao == 2:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Digite apenas 1 ou 2.')