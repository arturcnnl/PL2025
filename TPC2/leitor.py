# nome; desc; anoCriacao; periodo; compositor; duracao; _id  - separados por ponto e vírgula
# ignorei a linha de cabeçalho e colunas desnecessárias

def ler_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    

    dados = [] 
    for linha in linhas[1:]:
        linha = linha.strip()
        campos = linha.split(';')
        if len(campos) == 7:  # garantir que tem todos os campos
            nome, desc, anoCriacao, periodo, compositor, duracao, _id = campos
            dados.append({
                'nome': nome.strip(),
                'periodo': periodo.strip(),
                'compositor': compositor.strip()
            })
    return dados

def lista_compositores(dados):
    compositores = sorted({obra['compositor'] for obra in dados})
    return compositores

def distribuicao_por_periodo(dados):
    distribuicao = {}
    for obra in dados:
        periodo = obra['periodo']
        distribuicao[periodo] = distribuicao.get(periodo, 0) + 1
    return distribuicao

def obras_por_periodo(dados):
    dicionario = {}
    for obra in dados:
        periodo = obra['periodo']
        nome = obra['nome']
        if periodo not in dicionario:
            dicionario[periodo] = []
        dicionario[periodo].append(nome)
    
    for periodo in dicionario:
        dicionario[periodo].sort()
    return dicionario

filepath = 'obras.csv'

dados = ler_csv(filepath)

# criar resultados
compositores = lista_compositores(dados)
distribuicao = distribuicao_por_periodo(dados)
obras_periodo = obras_por_periodo(dados)


print("Lista de compositores (ordenada):")
print(compositores)
print("\nDistribuição por período:")
print(distribuicao)
print("\nObras por período:")
print(obras_periodo)
