def inverter_palavras(texto):
    palavras = texto.split()
    palavras_invertidas = palavras[::-1]
    return ' '.join(palavras_invertidas)

def extrair_estado(pilha):
    estado_atual = ''
    pilha_str = ''.join(pilha)
    
    inicio = pilha_str.find('<')
    fim = pilha_str.find('>', inicio)
    
    if inicio != -1 and fim != -1:
        estado_atual = pilha_str[inicio:fim + 1] 
    
    return estado_atual


import pandas as pd

file_path = 'tabela_comp.xlsx'  
df = pd.read_excel(file_path, header=None)

grammar_matrix = df.fillna("").astype(str).values.tolist()

estado_atual = '<prog>'

with open('tokens.txt', 'r') as file:
    content = file.read()

lexico = content.replace('\n', ' ').replace('\t', ' ').split()

#print("Tokens:", lexico)

primeira_linha = grammar_matrix[0]  
primeira_coluna = [linha[0] for linha in grammar_matrix]  


pilha = ""

for token in lexico:
    estado_index = primeira_coluna.index(estado_atual)
    token_index = primeira_linha.index(token)
    
    elemento = grammar_matrix[estado_index][token_index]

    if(elemento == 'ERRO'):
        print("ERRO DETECTADO")
        break

    lexico.remove(token)
    
    pilha += inverter_palavras(elemento)
    estado_atual = extrair_estado(pilha)

    print(estado_atual)

