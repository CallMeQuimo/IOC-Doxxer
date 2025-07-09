# IOC-Doxxer

Script interactivo para abrir automáticamente herramientas de análisis como VirusTotal y AbuseIPDB a partir de IOCs (IPs o URLs).

## Uso

1. Ejecutá el script:
2. Ingresá una o varias IP/Links
3. El programa abrirá VirusTotal y AbuseIPBD en tu navegador predeterminado en busca de lo que ingresaste

## Estructura

- `main.py` → Entrada principal
- `backend/functions.py` → Funciones de validación y apertura
- `frontend/` → Interfaz gráfica (futuro)

## Dependencias

- Python 3.10+
- Módulos: `re`, `webbrowser`, `ipaddress`

(No requiere instalar nada externo)

## Estado

🔨 En desarrollo — versión prototipo funcional por consola.
