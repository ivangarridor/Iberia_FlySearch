
# Proyecto de Automatización de Búsqueda de Vuelos - Iberia

Este proyecto automatiza la introducción de datos de vuelos en la página web de Iberia, utilizando Selenium para interactuar con la interfaz y Pytest para ejecutar las pruebas. Los informes se generan con Allure, proporcionando reportes detallados de cada ejecución de prueba.

## Requisitos

- **Python 3.x**: Asegúrate de tener Python instalado en tu máquina.
- **Dependencias**: Las dependencias necesarias están especificadas en `requeriments.txt`. Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install -r requeriments.txt
```

## Estructura del Proyecto

- **data/**: Contiene el archivo `Iberia_Flight_Data.xlsx`, el cual proporciona los datos de vuelo utilizados en las pruebas.
- **drivers/**: Incluye los drivers necesarios para Selenium.
- **pages/**: Implementa el patrón Page Object Model (POM) para representar las diferentes páginas de la web de Iberia.
- **reports/**: Directorio donde se almacenarán los informes generados por Allure.
- **tests/**: Contiene los scripts de prueba, organizados usando Pytest.
- **utils/**: Funciones auxiliares para la gestión de datos y reportes.

## Ejecución de las Pruebas

Para ejecutar las pruebas, sigue estos pasos:

1. **Configura el entorno virtual** (opcional, pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/MacOS
    .\venv\Scripts\activate  # En Windows
    ```

2. **Instala las dependencias**:
    ```bash
    pip install -r requeriments.txt
    ```

3. **Ejecuta las pruebas con Pytest**:
    ```bash
    pytest --alluredir=reports/allure-results -s (con el "-s" mostraremos en la terminal todos los pasos realizados con un formato customizado)
    ```

4. **Genera el reporte de Allure**:
    Para generar el reporte y visualizarlo en el navegador, usa el siguiente comando:
    ```bash
    allure serve reports/allure-results
    ```

Esto abrirá un servidor local donde podrás ver los resultados detallados de las pruebas en un formato interactivo. Dentro de este reporte hay una pequeña opción de "logs" en la que al pulsarla se desplegarán todos los pasos detallados

## Descripción de las Pruebas

El proyecto incluye pruebas que verifican la correcta navegación e interacción con la página web de Iberia. Las pruebas están organizadas siguiendo el patrón Page Object Model (POM), lo que facilita la mantenibilidad del código.

- **test_search.py**: Incluye pruebas para la búsqueda de vuelos en la web de Iberia.
- Las pruebas utilizan el archivo `Iberia_Flight_Data.xlsx` como fuente de datos de entrada.

## Notas Adicionales

- El archivo `webdriver-manager` se encarga de gestionar los drivers necesarios para Selenium, por lo que no es necesario descargarlos manualmente.

