# Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Esta aplicación permite procesar y generar reportes de transacciones financieras. El usuario puede cargar un archivo con transacciones y obtener un reporte con eL `balance final`, el `conteo de transacciones` y la `transacción de mayor monto`. 

- **Balance Final:**  
  Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

- **Conteo de Transacciones:**  
  Número total de transacciones para cada tipo ("Crédito" y "Débito").

- **Transacción de Mayor Monto:**  
  Identificar el ID y el monto de la transacción con el valor más alto.

## Instrucciones

1. **Repositorio Base:**  

   Clona el repositorio base:  
   ```
   git clone git@github.com:carlaclefig/banking-transactions.git

   cd banking-transactions
   ```
2. **Requisitos:**

   Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el proyecto:

   - **Python 3.7+**: La aplicación está desarrollado en Python. 
   
   Si no tienes Python instalado, puedes obtenerlo desde [python.org](https://www.python.org/downloads/).

   - Que el archivo de datos `data.csv` se encuentre en la raiz del proyecto

3. **Ejecución la aplicación:**
   
   ```
   python main.py
   ```

   La aplicación te solicitará el nombre del archivo que tiene las transacciones (`data.csv`) y te permitirá seleccionar opciones para generar el reporte o salir.

4. **Salida del Programa:** 

   La aplicación debe mostrar el reporte final en la terminal.  
   Ejemplo de salida:

   ```
   Reporte de Transacciones
   ---------------------------------------------
   Balance Final: 325.00
   Transacción de Mayor Monto: ID 3 - 200.00
   Conteo de Transacciones: Crédito: 3 Débito: 2
   ```

## Enfoque y Solución
   La solución está estructurada de manera modular para facilitar el mantenimiento y la extensión. Se optó por una interfaz de línea de comandos sencilla que permite al usuario interactuar fácilmente con el sistema.

1. **Cargar datos**

   El archivo de entrada  (`data.csv`) es procesado por la función `ingest_data` en `ingest_data.py`, que carga las transacciones en una lista.

2. **Clase Transaccion**

   En `transaction.py`, se define la clase `Transaction`, que tiene los atributos:

   - `id`: Identificador único de la transacción.
   - `amount`: Monto de la transacción.
   - `type`: Tipo de transacción (crédito o débito).

   Los tipos se definen en la enumeración `TransactionType`, con dos valores: `CREDIT` y `DEBIT`.

3. **Operaciones sobre las transacciones**

   En `transaction_operations.py`, la función `show_report` realiza los cálculos para generar el reporte:

   - **Balance Final:** Diferencia entre los montos de crédito y débito.
   - **Conteo de Transacciones:** Número de transacciones por tipo.
   - **Transacción de Mayor Monto:** La transacción con el monto más alto.
   - Finalmente, genera y muestra un reporte estructurado.

4. **Interacción con el Usuario**
   
   La aplicación es interactiva y presenta un menú con las siguientes opciones:

   - Opción 1: Muestra un reporte detallado de las transacciones procesadas.
   - Opción 0: Sale del programa.

## Estructura del proyecto
   ```
   /proyecto
├── data.csv                     # Archivo con las transacciones a procesar. 
├── ingest_data.py               # Función para cargar los datos desde un archivo de entrada.
├── main.py                      # Archivo principal donde se ejecuta la lógica del programa.
├── transaction.py               # Definición de la clase Transaction y tipos de transacción (crédito, débito).
├── transaction_operations.py    # Contiene la función `show_report`, que procesa las transacciones y genera el reporte.
└── README.md                    # Este archivo con la documentación del proyecto.
```