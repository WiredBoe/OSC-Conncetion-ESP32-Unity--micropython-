
import network
import socket
import time

# Activa la interfaz de estación (STA) y escanea las redes WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
nets = sta_if.scan()

# Imprime los nombres de las redes WiFi y sus señales de intensidad
for i, net in enumerate(nets):
    ssid = net[0].decode("utf-8")
    rssi = net[3]
    print("%d: SSID: %s, RSSI: %d" % (i, ssid, rssi))

# Pide al usuario que seleccione la red WiFi a la que se quiere conectar
index = int(input("Selecciona el número de la red WiFi a la que te quieres conectar: "))
if index < 0 or index >= len(nets):
    print("Índice de red inválido. Saliendo...")
    import sys
    sys.exit()
ssid = nets[index][0].decode("utf-8")

# Pide al usuario que ingrese la contraseña de la red WiFi
password = input("Ingresa la contraseña de la red WiFi: ")

# Conéctate a la red WiFi seleccionada
print("Conectándose a la red WiFi %s..." % ssid)
sta_if.connect(ssid, password)
while not sta_if.isconnected():
    pass
print("Conexión exitosa. Dirección IP: %s" % sta_if.ifconfig()[0])