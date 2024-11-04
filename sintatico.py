with open('tokens.txt', 'r') as file:
    content = file.read()

content = content.replace('\n', ' ').replace('\t', ' ')

formatted_content = ' '.join(content.split())

print(formatted_content)

import pandas as pd

file_path = 'comp.xlsx'  
df = pd.read_excel(file_path)  

grammar_matrix = df.fillna("").values.tolist()

for row in grammar_matrix:
    print(row)