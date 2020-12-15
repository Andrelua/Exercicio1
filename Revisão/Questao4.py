meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
media = 0
temperatura = []
for i in range(12):
    temperatura.append(float(input(f"Temperatura do mês {i+1}º: ")))

media = sum(temperatura) / 12

maiorMedia = []
mesesEscolhido = []

for i in range(12):
    if temperatura[i] > media:
        maiorMedia.append(temperatura[i])
        mesesEscolhido.append(meses[i])

print(f"\nMédia anual: {media:.2f}\n")
print("Meses acima da média de temperatura: ")

for i in range(len(maiorMedia)):
    print(f"{mesesEscolhido[i]} - {maiorMedia[i]}")
