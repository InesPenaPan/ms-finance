# 💰 Microservicio de Finanzas
**Componente del Trabajo de Fin de Máster (TFM)** > *Máster en Ingeniería de Software*

Microservicio construido con **FastAPI** que automatiza la ingesta y procesamiento de datos de Yahoo! Finance (`yfinance). El sistema calcula indicadores clave de solvencia, liquidez y apalancamiento de empresas cotizadas, además de monitorizar el crecimiento de ingresos trimestrales y agregar noticias bursátiles en tiempo real.


## 💻 Funcionalidades Principales

El microservicio expone dos endpoints principales:

### 1. Obtener Ratios Financieros y Crecimiento (`/finance/{ticker}`)

Este endpoint procesa la información de los estados financieros de una empresa, para ofrecer métricas comparativas:

#### Liquidez y Solvencia

* **Ratio Circulante** `current_ratio`: Mide la capacidad de la empresa para cubrir sus pasivos a corto plazo usando todos sus activos circulantes.

* **Ratio Rápido** `quick_ratio`: Mide la capacidad de pago más inmediata, excluyendo el inventario de los activos circulantes.

* **Deuda a Capital** `debt_to_equity`: Mide el apalancamiento financiero. Indica la proporción de la financiación de la empresa que proviene de la deuda frente al capital propio.


#### Performance

* **Capitalización de Mercado** `market_cap`: Es el valor total de las acciones en circulación de la empresa en el mercado.

#### Crecimiento
* **Tasa de crecimiento** `quarterly_revenue_growth`: Mide el cambio porcentual en los ingresos totales (Total Revenue) de una empresa de un trimestre al trimestre inmediatamente anterior. Es el indicador clave de si el negocio está acelerando o desacelerando su capacidad para generar ventas.

### 2. Obtener Noticias Bursátiles (`/news/{ticker}`)

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
