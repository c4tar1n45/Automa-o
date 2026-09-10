import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
    'Cargo': ['Engenheira', 'Médico', 'Professor', 'Advogado']
}

df = pd.DataFrame(dados)
df.to_excel('dados.xlsx', index=False)
