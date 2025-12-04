import csv

def generar_reporte():
    mes = input("Mes (1-12): ")
    anio = input("Año (YYYY): ")

    salida = f"reporte_vacaciones_{anio}_{mes.zfill(2)}.csv"

    try:
        with open("vacaciones.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            aprobadas = [
                r for r in reader
                if r["estado"] == "APROBADA" and r["mes"] == mes and r["anio"] == anio
            ]
    except:
        print("Error abriendo vacaciones.csv")
        return

    if not aprobadas:
        print("\nNo hay solicitudes aprobadas para ese periodo.\n")
        return

    with open(salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=aprobadas[0].keys())
        writer.writeheader()
        writer.writerows(aprobadas)

    print(f"\nReporte generado: {salida}\n")
