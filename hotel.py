andar = 20

for n_andar in range(1,andar+2):
#    print("Numero do Andar é", n_andar)
    if(n_andar == 13): continue

    print("Andar N°",n_andar)

print("-------->")

# Ordem decrescente
for n_andar in range(andar+1,0,-1):

    if(n_andar == 13): continue

    print("Andar N°",n_andar)

print("-------->")


contador = 1

while contador < 22:
    if contador == 13:
        contador += 1
    print("Andar N°",contador)
    
    contador += 1

print("-------->")

# Ordem decrescente com While

contador = 21

while contador > 0:
    if contador == 13:
        contador -= 1
    print("Andar N°",contador)
    
    contador -= 1
    

        