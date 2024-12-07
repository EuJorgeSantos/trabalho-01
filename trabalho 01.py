# Obter o salário do usuário
salario = float(input("Digite o salário: R$ "))

# Definir a taxa de inflação
inflacao = 0.038

# Calcular o reajuste com base na faixa salarial
if salario <= 280:
    percentual_reajuste = 0.20
elif 280 < salario <= 700:
    percentual_reajuste = 0.15
elif 700 < salario <= 1500:
    percentual_reajuste = 0.10
else:
    percentual_reajuste = 0.05

# Calcular o salário reajustado
salario_reajustado = salario + (salario * percentual_reajuste)

# Calcular o valor do reajuste
valor_reajuste = salario * percentual_reajuste

# Calcular o reajuste real, considerando a inflação
reajuste_real = valor_reajuste - (valor_reajuste * inflacao)

# Exibir os resultados
print("\nDetalhes do Salário:")
print(f"1. Salário antes do reajuste: R$ {salario:.2f}")
print(f"2. Percentual de aumento aplicado : {percentual_reajuste * 100:.0f}%")
print(f"3. Valor do aumento: R$ {valor_reajuste:.2f}")
print(f"4. Novo salário após o aumento: R$ {salario_reajustado:.2f}")
print(f"5. Valor do aumento real, após a inflação: R$ {reajuste_real:.2f}")