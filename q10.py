salario_bruto = 5000
desconto_inss =  salario_bruto * 0.15
desconto_ir = salario_bruto * 0.10
imposto = desconto_inss + desconto_ir


salario_liquido = salario_bruto - imposto
print(salario_liquido)
