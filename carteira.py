numero_rodas = 4
peso_bruto = 3550
pessoas = 4

if numero_rodas <= 3:
    print("Habiltação A")
elif numero_rodas == 4 and peso_bruto <= 3500:
    print("Habilitação B")
elif numero_rodas >= 4 and peso_bruto <= 3600:
    print("Habilitação C")
elif numero_rodas >= 4 and pessoas > 8:
    print("Habilitação D")
else:
    print("Habilitação D")