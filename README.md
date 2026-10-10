# 🌳 Análise de Regressão Linear Aplicada à Dendrometria

Este repositório contém o projeto de análise estatística desenvolvido para a disciplina de **Modelagem e Inferência Estatística** do curso de **Tecnologia em Ciência de Dados**. 

O objetivo principal é avaliar a aplicabilidade de modelos de **Regressão Linear Simples e Múltipla** na predição da altura de árvores (`altura_m`) a partir do seu diâmetro (`diametro_cm`) e espécie (`especie`)[cite: 1, 2].

---

## 📌 Contexto do Projeto

Na engenharia florestal e dendrometria, mensurar a altura de árvores em campo costuma ser uma tarefa trabalhosa e propensa a erros operacionais. Por outro lado, a medição do diâmetro à altura do peito (DAP) é rápida e precisa. A modelagem estatística permite prever a altura a partir do diâmetro e de fatores taxonômicos (espécie), otimizando a coleta de dados e o manejo florestal.

Neste projeto, respondemos à seguinte questão central:
> *É possível aplicar os conceitos de regressão linear em qualquer cenário? Quais são as restrições e como validar o modelo para predição da altura das árvores?*

---

## 🔬 Metodologia e Avaliação de Premissas

A aplicação de regressões lineares exige a verificação rigorosa de quatro premissas fundamentais (hipóteses do modelo OLS - *Ordinary Least Squares*):

1. **Linearidade:** A relação entre as variáveis explicativas e a variável dependente deve ser linear.
2. **Independência das observações:** Os resíduos não devem apresentar autocorrelação.
3. **Homocedasticidade:** A variância dos resíduos deve ser constante ao longo dos valores previstos[cite: 1].
4. **Normalidade dos Resíduos:** Os erros devem seguir uma distribuição normal[cite: 1].

---

## 📊 Principais Resultados e Discussão

* **Dataset:** 105 observações de árvores (`arvore2.xlsx`) contendo informações de diâmetro, altura e espécie[cite: 1].
* **Modelo de Regressão Múltipla:**
  * **Variável Dependente ($y$):** `altura_m`[cite: 1, 2]
  * **Variáveis Explicativas ($X$):** `diametro_cm`, `especie`[cite: 1, 2]
  * **Coeficiente de Determinação ($R^2$):** A regressão múltipla alcançou um $R^2 \approx 69,95\%$, superando o modelo simples ($R^2 \approx 57\%$) e demonstrando que a espécie desempenha um papel fundamental no ajuste da taxa de crescimento e forma[cite: 1].

### Resposta Acadêmica / Síntese Teórica
> A regressão linear pode ser aplicada neste cenário, mas não deve ser utilizada de forma indiscriminada sem a verificação prévia de suas condições[cite: 1]. Na análise realizada, a inclusão da espécie como variável categórica/explicativa melhorou significativamente o ajuste do modelo em relação à regressão simples[cite: 1]. O modelo é adequado, contudo, a validação gráfica dos resíduos e testes de homocedasticidade e normalidade devem ser conduzidos rigorosamente antes do uso prático para estimativas em campo[cite: 1].

---

## 💻 Estrutura do Código (`regressao_arvore.py`)

O script realiza o carregamento da base de dados, computa métricas descritivas essenciais e ajusta o modelo OLS utilizando a biblioteca `statsmodels`:

```python
import pandas as pd
import statsmodels.api as sm

# 1. Carregamento dos Dados
df = pd.read_excel('arvore2_regressoes.xlsx', sheet_name='Plan2')

# 2. Métricas Gerais (Big Numbers)
total_arvores = len(df)
media_diametro = df['diametro_cm'].mean()
media_altura = df['altura_m'].mean()

# 3. Modelagem de Regressão Múltipla (OLS)
X = sm.add_constant(df[['especie', 'diametro_cm']])
y = df['altura_m']

modelo = sm.OLS(y, X).fit()
print(modelo.summary())
```[cite: 2]

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado[cite: 2], além das bibliotecas necessárias:

```bash
pip install pandas statsmodels openpyxl
