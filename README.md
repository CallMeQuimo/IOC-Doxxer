# IOC-Doxxer!

**Versión:** 0.4
**Autor:** Quimey Leguizamón
**Descripción:**  
IOC-Doxxer! es una app gráfica desarrollada en Python que busca analizar IPs o URLs sospechosas en servicios OSINT, con un enfoque en facilidad de uso, legibilidad del código y escalabilidad futura.

## Características

- Interfaz gráfica (Tkinter) intuitiva y liviana.
- Validación de entradas (IPs y URLs simples, sin ofuscación).
- Acceso directo a herramientas OSINT con un solo clic.
- Soporte para múltiples motores de análisis (por ahora VT y AbuseIPDB).
- Placeholder dinámico en el campo de entrada.
- Planeado: Más motores, historial local, mejoras de diseño, etc.

## 📂 Estructura del proyecto
proyecto/
├── backend/
│ └── functions.py # Lógica de validación y análisis
├── frontend/
│ └── gui.py # Interfaz gráfica (Tkinter)
├── main.py # Entry point (lanza la GUI)
├── README.md # Este archivo
├── .gitignore # Ignorar archivos innecesarios (.pyc, dist/, etc.)

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Librerías estándar: `tkinter`, `webbrowser`, `ipaddress`, `re`

_No se requieren librerías externas ni instalación adicional._