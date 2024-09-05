import json
"""Aqui estamos importando no arquivo para dentro do projeto"""
with open('dados.json', 'r') as file:
    dados_faturmento = json.load(file)

lista_valores = []
"""Estamos acessando cada elemento do arquivo e armazendo somente os valores dentro de uma lista"""
for registro in dados_faturmento:
        lista_valores.append(registro['valor'])


menor_valor = min(lista_valores)
maior_valor = max(lista_valores)
media_mensal = sum(lista_valores) / len(lista_valores)
dias_acima_da_media = sum(1 for valor in lista_valores if valor > media_mensal)

print(f'O menor valor de faturamento: {menor_valor:.2f}')
print(f'O maior valor de faturamento: {maior_valor:.2f}')
print(f'Media de faturamento do mês: {media_mensal:.2f}')
print(f'Número de dias que o faturamento foi maior que a médias: {dias_acima_da_media} dias')




