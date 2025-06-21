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
def solicitar_notas(mensajes):
    while True:
        try:
            numero_notas = int(input(mensajes))
            if numero_notas >= 1 and numero_notas <= 999:
                return numero_notas
            else:
                print("El número de notas debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")