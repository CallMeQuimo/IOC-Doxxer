import webbrowser
import ipaddress
import re

# Abrir herramientas web
def opVT(ioc):
    webbrowser.open(f"https://www.virustotal.com/gui/search/{ioc}")
def opIPBD(ioc):
    webbrowser.open(f"https://www.abuseipdb.com/check/{ioc}")

# Filtrar datos
def trimURL(ioc):
    return re.sub(r"^https?://", "", ioc)

# Validación de datos
def validLink(ioc):
    patron = re.compile(
        r"^(https?://)?"            # Opcional: http:// o https://
        r"([a-zA-Z0-9.-]+)"         # Dominio
        r"\.[a-zA-Z]{2,}"           # .com, .org, etc
        r"(/.*)?$"                  # Rutas específicas
    )
    return bool(patron.match(ioc))
def validIP(ioc):
    try:
        ipaddress.ip_address(ioc)
        return True
    except ValueError:
        return False
def validIOC(ioc):
    while not (validLink(ioc) or validIP(ioc)):
        ioc = input("El IOC ingresado no es legible, ingresa de nuevo:").lower().strip()
    return trimURL(ioc)