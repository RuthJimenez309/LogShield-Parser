# GuardRail-SAST 

Un Pipeline Local de Análisis Estático de Seguridad (SAST/SCA) automatizado en PowerShell para entornos de desarrollo Python.

## Características
- **Análisis de Código (SAST):** Uso de `Bandit` para detectar malas prácticas y fallas críticas en el código fuente (como credenciales expuestas e inyección de comandos).
- **Análisis de Dependencias (SCA):** Integración de `Safety` para auditar librerías de terceros contra bases de datos de vulnerabilidades conocidas (CVEs).
- **Automatización:** Script orquestador local en PowerShell (`.ps1`) para ejecutar auditorías en un solo comando.
- **Contenedorización:** Configuración de `Dockerfile` lista para empaquetar la aplicación de forma segura bajo el principio de Shift Left.

## Estructura del Proyecto
- `app/`: Código fuente de la aplicación (incluye simulaciones de código vulnerable para pruebas).
- `test_sast.ps1`: Automatización del pipeline de escaneo.
- `Dockerfile`: Instrucciones de empaquetado seguro.


