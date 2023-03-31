# Faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do faturamento total da distribuidora
faturamento_total = sum(faturamento.values())

# Cálculo do percentual de representação de cada estado
percentuais = {}
for estado, faturamento_estado in faturamento.items():
    percentuais[estado] = faturamento_estado / faturamento_total * 100

# Impressão dos resultados
for estado, percentual in percentuais.items():
    print(f'O estado {estado} representou {percentual:.2f}% do faturamento total da distribuidora.')
