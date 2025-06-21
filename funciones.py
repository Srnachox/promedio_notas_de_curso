from funciones import solicitar_nota, calcular_promedio
# programa principal desde aqui
notas = []
total_notas = solicitar_nota('Ingresa cantidad de notas: ')
for i in range(5):
    nota = solicitar_nota()
    notas.append(nota)
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio:.0f}")