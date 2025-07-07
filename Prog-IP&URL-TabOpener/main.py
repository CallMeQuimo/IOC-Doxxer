import webbrowser

##Función
def sitiosIOC(ioc, vt, ipbd):

    if(vt=="s"):#VT
        webbrowser.open(f"https://www.virustotal.com/gui/search/{ioc}")

    if(ipbd=="s"):#IPBD
        webbrowser.open(f"https://www.abuseipdb.com/check/{ioc}")

    print(f"\nSe abrieron los sitios para: {ioc}")

# Entrada por consola
if __name__ == "__main__":
    cuant = int(input("¿Cuántos IOC quieres analizar?"))
    rules = input("¿Quieres cambiar las páginas abiertas por cada IOC? (s/n)").lower()
    ran = 0
    while(ran < cuant):
        if(ran==0 or rules=="s"):
            vt = input("Usar VT? (s/n)").lower()
            ipbd = input("Usar IPBD? (s/n)").lower()
        ioc = input(f"Ingresá una IP o URL sospechosa #{ran+1}: ").strip()
        sitiosIOC(ioc, vt, ipbd)
        ran+=1