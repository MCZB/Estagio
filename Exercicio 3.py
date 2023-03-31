import json

# Leitura do arquivo JSON
with open('E:/Python/ESTAGIO/dados.json') as f:
    data = json.load(f)

# Cálculo do menor e maior valor de faturamento
min_faturamento = float('inf')
max_faturamento = float('-inf')

for d in data:
    valor = d['valor']
    if valor < min_faturamento:
        min_faturamento = valor
    if valor > max_faturamento:
        max_faturamento = valor

# Cálculo da média mensal
total_faturamento = sum(d['valor'] for d in data)
dias_uteis = sum(1 for d in data if d['dia'] % 7 not in [0, 6]) # desconsidera finais de semana
media_mensal = total_faturamento / dias_uteis

# Cálculo do número de dias com faturamento acima da média mensal
dias_acima_media = sum(1 for d in data if d['valor'] > media_mensal)

# Resultados
print('Menor valor de faturamento: R$ {:.2f}'.format(min_faturamento))
print('Maior valor de faturamento: R$ {:.2f}'.format(max_faturamento))
print('Número de dias com faturamento acima da média mensal: {}'.format(dias_acima_media))
