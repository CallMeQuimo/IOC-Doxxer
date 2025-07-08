import webbrowser
import ipaddress
import re

#Abrir herramientas web
def opVT(ioc):
    webbrowser.open(f"https://www.virustotal.com/gui/search/{ioc}")
def opIPBD(ioc):
    webbrowser.open(f"https://www.abuseipdb.com/check/{ioc}")

# Validación de datos
def validURL(ioc):
    patron = re.compile(r"^https?://[^\s/$.?#].[^\s]*$")
    return bool(patron.match(ioc))
def validIP(ioc):
    try:
        ipaddress.ip_address(ioc)
        return True
    except ValueError:
        return False
def validIOC(ioc):
    v = False
    while not v:
        if(validURL(ioc) or validIP(ioc)):
            v = True
        else:
            ioc = input("El IOC ingresado no es legible, ingresa de nuevo:")

    return ioc