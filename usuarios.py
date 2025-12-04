import csv

def validar_credenciales(usuario, contrasena):
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["usuario"] == usuario and row["contrasena"] == contrasena:
                    return True, row["rol"]
    except:
        print("Error al leer usuarios.csv")
        return False, None

    return False, None
