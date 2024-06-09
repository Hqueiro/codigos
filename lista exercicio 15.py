# exercicio onde pede todos dados e descontos do holerite

ganho_por_hora = float(input(" informe o seu ganho por hora :"))
horas_no_mes = float(input(" horas trabalhadas no mes :"))
renda_mensal = ganho_por_hora*horas_no_mes
imposto_de_renda = 0.11 * renda_mensal
inss = 0.08*renda_mensal
sindicato = 0.05*renda_mensal

salario_bruto = renda_mensal
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)

print(f" O salário bruto é {salario_bruto}")

print(f" desconto do INSS (8%): R$ {inss}")

print(f"Desconto sindicato é (5%): R$ {sindicato}")

print(f"Desconto imposto de renda (11%): R$ {imposto_de_renda} ")

print(f" Salario liquido : R$ {salario_liquido}")