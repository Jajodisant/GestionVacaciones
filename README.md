## Título
### Subtítulo
Este es un ejemplo de texto que da entrada a una lista genérica de elementos:
- Elemento 1
- Elemento 2
- Elemento 3
Este es un ejemplo de texto que da entrada a una lista numerada:
1. Elemento 1
2. Elemento 2
3. Elemento 3
Al texto en Markdown puedes añadirle formato como **negrita** o *cursiva* de una manera muy sencilla.


## PeopleOps Vacation Console
### Datos del estudiante
**Nombre completo:** Jainer Pabón
**Clan:** Turing

### Descripción general
PeopleOps Vacation Console es una aplicación de consola desarrollada en Python que permite gestionar empleados y sus vacaciones en la empresa. La aplicación permite registrar empleados, solicitar vacaciones, aprobar o rechazar solicitudes, consultar historial y generar reportes mensuales en formato CSV. Todos los datos se guardan de forma persistente en archivos CSV.

## Cómo ejecutar el programa?
 - Abrir la carpeta del proyecto en la terminal.  
 - Ejecutar el programa principal:<br>
      ***python main.py***
 - Iniciar sesión con el usuario administrador:<br>
      ***Usuario: admin***<br>
      ***Contraseña: admin123***
   
**Archivo principal:** main.py <br>
**Versión de Python recomendada:** 3.8 o superior <br>
**Archivos CSV necesarios:** 
 - usuarios.csv <br>
 - empleados.csv <br>
 - vacaciones.csv <br>

 ## Estructura del proyecto
 CRUDScope/ <br>
│ <br>
├── main.py            # Menú principal e inicio de sesión <br>
├── usuarios.py        # Validación de credenciales <br>
├── empleados.py       # Registro, listado y consulta de empleados <br>
├── vacaciones.py      # Solicitudes, aprobación/rechazo y cálculo de días <br>
├── reportes.py        # Generación de reportes mensuales en CSV <br>
│ <br>
├── usuarios.csv       # Datos de usuarios del sistema <br>
├── empleados.csv      # Datos de empleados registrados <br>
├── vacaciones.csv     # Solicitudes de vacaciones <br>
├── reporte_vacaciones_2025_03.csv  # Ejemplo de reporte <br>
│ <br>
└── README.md


