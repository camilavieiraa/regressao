import pandas as pd
import statsmodels.api as sm

# Carregar os dados
df = pd.read_excel('arvore2_regressoes.xlsx', sheet_name='Plan2')

# 1. Big Numbers
total_arvores = len(df)
media_diametro = df['diametro_cm'].mean()
media_altura = df['altura_m'].mean()

# 2. Regressão Múltipla
X = sm.add_constant(df[['especie', 'diametro_cm']])
y = df['altura_m']

modelo = sm.OLS(y, X).fit()
print(modelo.summary())