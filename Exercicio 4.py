# Para calcular o tempo de percurso do carro, podemos utilizar a fórmula: tempo = distância / velocidade. Assim, o tempo que o carro levou para chegar ao ponto de cruzamento é:

# tempo_carro = 50 / 110 = 0,4545 horas

# Como o caminhão leva 5 minutos a mais para passar em cada um dos pedágios, podemos adicionar 10 minutos ao tempo total de percurso do caminhão. Portanto, o tempo que o caminhão levou para chegar ao ponto de cruzamento é:

# tempo_caminhao = 50 / 80 + 10/60 = 0,8125 horas

# Agora que temos o tempo de percurso de cada veículo, podemos calcular a distância percorrida por cada um até o ponto de cruzamento, utilizando a mesma fórmula: distância = tempo x velocidade. Assim, a distância percorrida pelo carro é:

# distancia_carro = 0,4545 x 110 = 49,9995 km

# E a distância percorrida pelo caminhão é:

# distancia_caminhao = 0,8125 x 80 = 65 km




# Distância entre Ribeirão Preto e Franca
distancia_total = 100

# Distância do ponto de cruzamento até cada cidade
distancia_cruzamento = distancia_total / 2

# Velocidade do carro e caminhão (em km/h)
velocidade_carro = 110
velocidade_caminhao = 80

# Tempo que o carro levou para chegar ao ponto de cruzamento
tempo_carro = distancia_cruzamento / velocidade_carro

# Tempo que o caminhão levou para chegar ao ponto de cruzamento
tempo_caminhao = distancia_cruzamento / velocidade_caminhao + 10 / 60  # adicionar tempo dos pedágios

# Distância percorrida pelo carro até o ponto de cruzamento
distancia_carro = tempo_carro * velocidade_carro

# Distância percorrida pelo caminhão até o ponto de cruzamento
distancia_caminhao = tempo_caminhao * velocidade_caminhao

# Verificar qual veículo está mais próximo da cidade de Ribeirão Preto
if distancia_carro < distancia_caminhao:
    print("O carro está mais próximo da cidade de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo da cidade de Ribeirão Preto.")
