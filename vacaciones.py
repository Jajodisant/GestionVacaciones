import csv
from datetime import datetime, timedelta
from empleados import leer_empleados

# ------------------------------
# LEER TODAS LAS SOLICITUDES
# ------------------------------
def leer_solicitudes():
    datos = []
    try:
        with open("vacaciones.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                datos.append(row)
    except:
        pass
    return datos

# ------------------------------
# CALCULAR MESES COMPLETOS
# ------------------------------
def meses_trabajados(fecha_inicio):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    hoy = datetime.now()
    diferencia = (hoy.year - inicio.year) * 12 + (hoy.month - inicio.month)
    return max(0, diferencia)

# ------------------------------
# CALCULAR DÍAS ENTRE FECHAS SIN DOMINGOS
# ------------------------------
def dias_sin_domingos(inicio, fin):
    actual = inicio
    dias = 0
    while actual <= fin:
        if actual.weekday() != 6:  # 6 = domingo
            dias += 1
        actual += timedelta(days=1)
    return dias

# ------------------------------
# DÍAS USADOS
# ------------------------------
def dias_usados(empleado_id):
    solicitudes = leer_solicitudes()
    usados = 0
    for s in solicitudes:
        if s["empleado_id"] == empleado_id and s["estado"] == "APROBADA":
            usados += int(s["dias_calculados"])
    return usados

# ------------------------------
# REGISTRAR SOLICITUD
# ------------------------------
def registrar_solicitud():
    empleados = leer_empleados()
    if not empleados:
        print("\nNo hay empleados registrados.\n")
        return

    emp_id = input("Ingrese ID del empleado: ")

    empleado = None
    for e in empleados:
        if e["empleado_id"] == emp_id:
            empleado = e
            break

    if not empleado:
        print("\nEmpleado no encontrado.\n")
        return

    # Validar mínimo 6 meses
    meses = meses_trabajados(empleado["fecha_inicio_contrato"])
    if meses < 6:
        print("\nEl empleado NO cumple los 6 meses mínimos.\n")
        return

    # Disponibilidad de días
    acumulados = meses * 1.5
    usados = dias_usados(emp_id)
    disponibles = acumulados - usados

    print(f"\nDías disponibles: {disponibles}")

    # Fechas
    f_inicio = input("Fecha inicio vacaciones (YYYY-MM-DD): ")
    f_fin = input("Fecha fin vacaciones (YYYY-MM-DD): ")

    inicio = datetime.strptime(f_inicio, "%Y-%m-%d")
    fin = datetime.strptime(f_fin, "%Y-%m-%d")

    dias = dias_sin_domingos(inicio, fin)

    if dias > disponibles:
        print("\nNo tiene días suficientes.\n")
        return

    mes = inicio.month
    anio = inicio.year

    # Guardar
    with open("vacaciones.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, empleado["nombre_completo"], f_inicio, f_fin, dias, "PENDIENTE", mes, anio])

    print("\nSolicitud registrada correctamente.\n")


# ------------------------------
# APROBAR / RECHAZAR
# ------------------------------
def aprobar_rechazar():
    solicitudes = leer_solicitudes()
    pendientes = [s for s in solicitudes if s["estado"] == "PENDIENTE"]

    if not pendientes:
        print("\nNo hay solicitudes pendientes.\n")
        return

    print("\n=== SOLICITUDES PENDIENTES ===")
    for idx, s in enumerate(pendientes):
        print(f"{idx+1}. {s['empleado_id']} - {s['nombre_empleado']} - {s['fecha_inicio_vacaciones']}")

    opc = int(input("\nSeleccione una solicitud: ")) - 1

    if opc < 0 or opc >= len(pendientes):
        print("\nOpción inválida.\n")
        return

    decision = input("Aprobar (A) o Rechazar (R): ").upper()

    for s in solicitudes:
        if s == pendientes[opc]:
            s["estado"] = "APROBADA" if decision == "A" else "RECHAZADA"

    # Guardar cambios
    with open("vacaciones.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=solicitudes[0].keys())
        writer.writeheader()
        writer.writerows(solicitudes)

    print("\nSolicitud actualizada correctamente.\n")


# ------------------------------
# HISTORIAL
# ------------------------------
def historial_empleado():
    emp_id = input("ID del empleado: ")
    solicitudes = leer_solicitudes()

    print("\n=== HISTORIAL ===")
    for s in solicitudes:
        if s["empleado_id"] == emp_id:
            print(s)
    print()
