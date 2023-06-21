print("Aluguel de Veiculos !")

Nome = str(input("Informe o seu nome:"))
model = str(input("Informe o carro que gostaria de alugar:"))

Dias = int(input("Sr(a){} Qual a Quantidade de dias que o carro foi alugado:".format(Nome)))
Km = float(input("Quantos KM foram rodados no total Com o veiculo:".format(model)))
pag = (Dias * 60) + (Km * 0.15)
print("Sr(a){} o total a pagar é de R${:.2f} Pelo aluguel do veiculo.".format(Nome, pag))

print("Obrigado, Volte Sempre !")
