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
├── main.py                   # Menú principal e inicio de sesión <br>
├── usuarios.py               # Validación de credenciales <br>
├── empleados.py              # Registro, listado y consulta de empleados <br>
├── vacaciones.py             # Solicitudes, aprobación/rechazo y cálculo de días <br>
├── reportes.py               # Generación de reportes mensuales en CSV <br>
│ <br>
├── usuarios.csv              # Datos de usuarios del sistema <br>
├── empleados.csv             # Datos de empleados registrados <br>
├── vacaciones.csv            # Solicitudes de vacaciones <br>
│ <br>
└── README.md

## Reglas de cálculo
 - Cada mes completo trabajado acumula 1.5 días de vacaciones.
 - Para solicitar vacaciones, el empleado debe tener al menos 6 meses completos en la empresa.
 - Los domingos no cuentan como días de vacaciones.
 - Los días disponibles se calculan como: <br>
      ***Días disponibles = (Meses completos × 1.5) − Días ya usados en solicitudes aprobadas***

## Limitaciones y mejoras futuras
  1. Actualmente la contraseña se guarda en texto plano en usuarios.csv. En el futuro se puede mejorar usando hashing seguro.
  2. La aplicación no maneja múltiples roles de usuario más allá del administrador.
  3. Validaciones de fechas y errores de usuario podrían mejorarse para evitar entradas incorrectas.
  4. Se puede agregar interfaz gráfica para mayor facilidad de uso.
  5. Integración con base de datos real para reemplazar CSV y permitir consultas más rápidas y confiables.
