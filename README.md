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

* **Ratio Rápido** `current_ratio`: Mide la solvencia inmediata sin depender de inventarios.
* **Ratio Circulante** `current_ratio`: Evalúa la capacidad de cubrir deudas a corto plazo con activos líquidos.
* **Deuda sobre Capital** `debt_to_equity`: Es el indicador directo del apalancamiento financiero. 
* **Tracción**: `quarterly_revenue_growth`: Mide la variación porcentual de ventas entre trimestres consecutivos. 
* **Capitalización de Mercado** `market_cap`: Indica el valor total de la empresa en bolsa.
* **Tasa de crecimiento** `quarterly_revenue_growth`: Mide la variación porcentual de ventas entre trimestres consecutivos.

### Agregación de Noticas en Tiempo Real

`GET /news/{ticker}`



Este endpoint recupera los titulares de noticias más recientes directamente desde la fuente para un símbolo bursátil específico.

## ⚡ Ejuctar el servicio

### Pasos

1. **Situarse en el Directorio**: Abre tu terminal y navega hasta el directorio raíz del proyecto.

2. **Construir e iniciar**: Ejecuta el siguiente comando. La instrucción `--build` garantiza que tu imagen se construya con el código más reciente antes de iniciar el contenedor.

```bash
docker compose up --build -d
```
3. **Acceder a la API**: El microservicio estará accesible en el puerto `8080` (definido en el docker-compose.yml). Utiliza tu navegador o una herramienta como cURL o Postman para realizar las siguientes peticiones:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| Ratios Financieros | `http://127.0.0.1:8000/finance/AAPL` |
| Noticias | `http://127.0.0.1:8000/news/AAPL` |

### Ejemplos de Tickers

Utiliza los siguientes símbolos bursátiles para probar tu API:

| Ticker | Empresa |
| :--- | :--- |
| **AAPL** | Apple Inc. |
| **MSFT** | Microsoft Corp. |
| **BBVA.MC** | Banco Bilbao Vizcaya Argentaria |
| **SAN.MC** | Banco Snatander |
| **ITX.MC** | Industria de Diseño Textil (Inditex) |
| **IBE.MC** | Iberdrola |
| **TEF.MC** | Telefónica |
