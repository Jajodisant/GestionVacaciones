import csv
from datetime import datetime

# ------------------------------
# LEER EMPLEADOS
# ------------------------------
def leer_empleados():
    empleados = []
    try:
        with open("empleados.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                empleados.append(row)
    except:
        pass
    return empleados

# ------------------------------
# GUARDAR EMPLEADO
# ------------------------------
def guardar_empleado(nombre, cargo, area, fecha_inicio):
    empleados = leer_empleados()
    nuevo_id = len(empleados) + 1

    with open("empleados.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nuevo_id, nombre, cargo, area, fecha_inicio])

    print("\nEmpleado registrado correctamente.\n")


# ------------------------------
# LISTAR EMPLEADOS
# ------------------------------
def listar_empleados():
    empleados = leer_empleados()
    if not empleados:
        print("\nNo hay empleados registrados.\n")
        return

    print("\n=== LISTA DE EMPLEADOS ===")
    for e in empleados:
        print(f"ID: {e['empleado_id']} | Nombre: {e['nombre_completo']} | Cargo: {e['cargo']} | Área: {e['area']}")
    print()

# ------------------------------
# CONSULTAR EMPLEADO
# ------------------------------
def consultar_empleado():
    emp_id = input("Ingrese ID del empleado: ")
    empleados = leer_empleados()

    for e in empleados:
        if e["empleado_id"] == emp_id:
            print("\n=== INFORMACIÓN DEL EMPLEADO ===")
            print(f"Nombre: {e['nombre_completo']}")
            print(f"Cargo: {e['cargo']}")
            print(f"Área: {e['area']}")
            print(f"Fecha inicio contrato: {e['fecha_inicio_contrato']}\n")
            return

    print("\nEmpleado no encontrado.\n")
