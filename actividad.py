#Actividad pt1
def solicitar_nota():
    while True:
        try:
            nota = float(input("Ingrese una nota entre 0 y 10: "))
            if  nota >= 1 and nota <= 7:
                return nota
            else:
                print("La nota debe estar entre 1 y 7.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
def calcular_promedio(lista):
    sumatoria = 0
    for nota in lista:
        sumatoria += nota
    return sumatoria / len(lista) 
# programa principal desde aqui
notas = []
for i in range(5):
    nota = solicitar_nota()
    notas.append(nota)
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio:.2f}")

