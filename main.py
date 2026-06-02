def calcular_nota_disciplina(notas):
    """Calcula a média simples a partir de uma lista de notas."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_situacao(media, presenca):
    """Define a situação do aluno com base nos critérios de corte."""
    MEDIA_MINIMA = 6.0
    PRESENCA_MINIMA = 75
    
    if media >= MEDIA_MINIMA and presenca >= PRESENCA_MINIMA:
        return "APROVADO"
    elif presenca < PRESENCA_MINIMA:
        return "REPROVADO POR FALTA"
    else:
        return "REPROVADO POR NOTA"


def cadastrar_disciplinas(quantidade):
    """
    Coleta os dados do usuário, aplica validações 
    e retorna uma lista de dicionários das disciplinas.
    """
    historico = []
    
    for i in range(1, quantidade + 1):
        print(f"\n[ Cadastro da {i}ª Disciplina ]")
        disciplina = {}
        disciplina['nome'] = input("Nome da disciplina: ")
        
        # Validação de Notas
        while True:
            try:
                n1 = float(input(f"Digite a 1ª nota de {disciplina['nome']}: "))
                n2 = float(input(f"Digite a 2ª nota de {disciplina['nome']}: "))
                if 0 <= n1 <= 10 and 0 <= n2 <= 10:
                    disciplina['notas'] = [n1, n2]
                    break
                print("Erro: Notas devem ser entre 0 e 10.")
            except ValueError:
                print("Erro: Digite um número válido para as notas.")

        # Validação de Presença
        while True:
            try:
                presenca = int(input("Porcentagem de presença (0-100): "))
                if 0 <= presenca <= 100:
                    disciplina['presenca'] = presenca
                    break
                print("Erro: Presença deve ser entre 0 e 100%.")
            except ValueError:
                print("Erro: Digite um número inteiro válido para a presença.")

        # Utilizando as funções de cálculo criadas
        disciplina['media'] = calcular_nota_disciplina(disciplina['notas'])
        disciplina['situacao'] = verificar_situacao(disciplina['media'], disciplina['presenca'])

        historico.append(disciplina)
        
    return historico


def gerar_relatorio_final(historico_escolar):
    """Processa os dados cadastrados e exibe o relatório formatado na tela."""
    print("\n" + "=" * 60)
    print(f"{'DISCIPLINA':<20} | {'MÉDIA':<7} | {'PRESENÇA':<10} | {'SITUAÇÃO'}")
    print("-" * 60)

    soma_medias_geral = 0

    for d in historico_escolar:
        soma_medias_geral += d['media']
        print(f"{d['nome']:<20} | {d['media']:<7.1f} | {d['presenca']:>7}%  | {d['situacao']}")

    # Processamento extra: Média Geral do Semestre
    total_disciplinas = len(historico_escolar)
    media_geral = soma_medias_geral / total_disciplinas if total_disciplinas > 0 else 0

    print("-" * 60)
    print(f"MÉDIA GERAL DO SEMESTRE: {media_geral:.2f}")
    print("=" * 60)


# FLUXO PRINCIPAL DO PROGRAMA (MAIN)
if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA ACADÊMICO MODULARIZADO")
    print("=" * 50)
    
    while True:
        try:
            TOTAL_DISCIPLINAS = int(input("Quantas disciplinas deseja cadastrar neste semestre? "))
            if TOTAL_DISCIPLINAS > 0:
                break
            else:
                print("Erro: Digite um número maior que zero.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
    
    # 1. Executa a função de cadastro
    dados_alunos = cadastrar_disciplinas(TOTAL_DISCIPLINAS)
    
    # 2. Executa a função que exibe o relatório
    gerar_relatorio_final(dados_alunos)
