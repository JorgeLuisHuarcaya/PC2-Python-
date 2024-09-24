alumnos = []
n = int(input("¿Cuántos alumnos deseas ingresar?: "))

for i in range(n):
    nombre = input("Nombre del alumno: ")
    notas = [float(input(f"Ingrese la nota {j+1} para {nombre}: ")) for j in range(3)]
    alumnos.append({"Alumno": nombre, "Notas": notas})

print("Listado de alumnos:")
for alumno in alumnos:
    print(alumno)