from usuarios import validar_credenciales
from empleados import guardar_empleado, listar_empleados, consultar_empleado
from vacaciones import registrar_solicitud, aprobar_rechazar, historial_empleado
from reportes import generar_reporte

def pantalla_login():
    print("=== PeopleOps Vacation Console ===")
    intentos = 0

    while intentos < 3:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        ok, rol = validar_credenciales(usuario, contrasena)

        if ok:
            print("\nACCESO CONCEDIDO\n")
            return

        intentos += 1
        print("Credenciales incorrectas.\n")

    print("Demasiados intentos. Saliendo...")
    exit()


def menu_empleados():
    while True:
        print("\n=== GESTIÓN DE EMPLEADOS ===")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Consultar empleado")
        print("4. Volver")

        op = input("Seleccione: ")

        if op == "1":
            nombre = input("Nombre completo: ")
            cargo = input("Cargo: ")
            area = input("Área: ")
            fecha = input("Fecha inicio contrato (YYYY-MM-DD): ")
            guardar_empleado(nombre, cargo, area, fecha)

        elif op == "2":
            listar_empleados()

        elif op == "3":
            consultar_empleado()

        elif op == "4":
            break


def menu_vacaciones():
    while True:
        print("\n=== VACACIONES ===")
        print("1. Registrar solicitud")
        print("2. Aprobar/Rechazar")
        print("3. Historial por empleado")
        print("4. Volver")

        op = input("Seleccione: ")

        if op == "1":
            registrar_solicitud()
        elif op == "2":
            aprobar_rechazar()
        elif op == "3":
            historial_empleado()
        elif op == "4":
            break


def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión empleados")
        print("2. Gestión vacaciones")
        print("3. Reportes")
        print("4. Salir")

        op = input("Seleccione: ")

        if op == "1":
            menu_empleados()
        elif op == "2":
            menu_vacaciones()
        elif op == "3":
            generar_reporte()
        elif op == "4":
            print("Saliendo...")
            break


def main():
    pantalla_login()
    menu_principal()


if __name__ == "__main__":
    main()
