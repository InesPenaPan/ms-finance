# 💰 Microservicio de Finanzas
**Componente del Trabajo de Fin de Máster (TFM)** > *Máster en Ingeniería de Software y Sistemas Informáticos (MSSI)*

Microservicio construido con **FastAPI** que automatiza la ingesta y procesamiento de datos de Yahoo! Finance (`yfinance`). El sistema calcula indicadores clave de solvencia, liquidez y apalancamiento de empresas cotizadas, además de monitorizar el crecimiento de ingresos trimestrales y agregar noticias bursátiles en tiempo real.

## 🛠️ Stack 
El microservicio está desarrollado con las siguientes tecnologías y librerías clave:

* `FastAPI`: Framework principal utilizado para construir la API.
* `uvicorn`: Servidor ASGI de alta velocidad encargado de ejecutar la aplicación.
* `pydantic`: Utilizado para la validación de datos y la gestión de esquemas mediante modelos de Python.
* `yfinance`: Librería encargada de la extracción de datos financieros y de mercado desde la API de Yahoo! Finance.
* `NumPy`: Soporte para el procesamiento eficiente de grandes estructuras de datos y cálculos numéricos.
* `py-eureka-client`: Cliente para la integración con **Netflix Eureka**.

## 🌐 Endpoints

### Análisis de Ratios y Performance

`GET /finance/{ticker}`

Calcula ratios financieros y métricas de crecimiento a partir de los estados contables de la entidad.

* `current_ratio`: Mide la solvencia inmediata sin depender de inventarios.
* `current_ratio`: Evalúa la capacidad de cubrir deudas a corto plazo con activos líquidos.
* `debt_to_equity`: Es el indicador directo del apalancamiento financiero. 
* `quarterly_revenue_growth`: Mide la variación porcentual de ventas entre trimestres consecutivos. 
* `market_cap`: Indica el valor total de la empresa en bolsa.
* `quarterly_revenue_growth`: Mide la variación porcentual de ventas entre trimestres consecutivos.

### Agregación de Noticas en Tiempo Real

`GET /news/{ticker}`

Recupera en tiempo real noticias vinculadas al símbolo bursátil. Devulve una colección `latest_headline` donde cada noticia contiene:

* `title`: Titular de la noticia.
* `summary`: Breve extracto o resumen del contenido.
* `link`: URL directa a la fuente original.
* `publisher`: Nombre del medio de comunicación.
* `publish_date`: Fecha y hora de publicación.
* `thumbnail_url`: Enlace a la imagen destacada (si está disponible).

## ⚡ Ejecución

Navega hasta el directorio raíz del proyecto y ejecuta el siguiente comando en tu terminal:

```bash
docker compose up --build -d
```
Una vez levantado el contenedor, la API estará disponible en el puerto `8080`. Puedes verificar el funcionamiento realizando peticiones a través de tu navegador, cURL o Postman:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| Análisis de Ratios y Performance | `http://127.0.0.1:8000/finance/AAPL` |
| Agregación de Noticas en Tiempo Real | `http://127.0.0.1:8000/news/AAPL` |

**Nota:** Puedes buscar los símbolos bursátiles (ej: NVDA, TSLA, SAN.MC) en [Yahoo! Finance](https://finance.yahoo.com/).





