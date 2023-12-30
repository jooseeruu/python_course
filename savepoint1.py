def separar_numeros(edades):
    pares = []
    impares = []

    for i in edades:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    return pares, impares

def contar_numeros(lista):
    contador = 0
    for i in lista:
        contador = contador + 1
    return contador

edades = [23, 45, 66, 47, 38, 52, 19, 75, 24, 33] 

pares, impares = separar_numeros(edades)
contador_pares = contar_numeros(pares)
contador_impares = contar_numeros(impares)

print(f"En la lista impar hay {contador_impares} números")
print(f"En la lista par hay {contador_pares} números")
print(f"La lista de impares es: {impares}")
print(f"La lista de pares es: {pares}")
