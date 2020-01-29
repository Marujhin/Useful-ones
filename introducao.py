import pandas as pd
import matplotlib.pyplot as plt

consumo = pd.read_csv("a11_CONSUMO.csv")

plt.plot(consumo.data, consumo.consumo)
plt.title("Dados de todos meses")
plt.xlabel("Data")
plt.ylabel("Consumo")
plt.xticks(consumo.data, rotation = "vertical")
plt.grid(True)
plt.show()


primeiros_10 = consumo[0:10]
plt.plot(primeiros_10.data, primeiros_10.consumo)
plt.title("Dados dos primeiros 10 meses")
plt.xlabel("Data")
plt.ylabel("Consumo")
plt.xticks(primeiros_10.data, rotation = "vertical")
plt.grid(True)
plt.show()


ultimos_10 = consumo[143:153]
plt.plot(ultimos_10.data, ultimos_10.consumo)
plt.title("Dados dos últimos 10 meses")
plt.xlabel("Data")
plt.ylabel("Consumo")
plt.xticks(ultimos_10.data, rotation = "vertical")
plt.grid(True)
plt.show()


consumo.boxplot()
plt.title("Boxplot com todos os meses")
plt.grid(True)
plt.show()

primeiros_30 = consumo[0:30]
plt.plot(primeiros_30.data, primeiros_30.consumo)
plt.title("Dados dos primeiros 30 meses")
plt.xlabel("Data")
plt.ylabel("Consumo")
plt.xticks(primeiros_30.data, rotation = "vertical")
plt.grid(True)
plt.show()