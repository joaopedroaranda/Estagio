import json
"""Aqui estamos importando no arquivo para dentro do projeto"""
with open('dados_faturamento.json', 'r') as file:
    data = json.load(file)

dados_faturamento = data['faturamento_estados']
""" """
soma_faturamentos = sum(registros['Valor'] for registros in dados_faturamento)

porcentagens = [
    {'Estado': registro['Estado'], 'Porcentagem': (registro['Valor'] / soma_faturamentos) * 100}
    for registro in dados_faturamento
]

for item in porcentagens:
    print(f"Estado: {item['Estado']}, Porcentagem: {item['Porcentagem']:.2f}%")