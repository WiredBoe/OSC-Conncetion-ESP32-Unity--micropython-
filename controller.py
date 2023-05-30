import machine
import time
from uosc.client import Bundle, Client, create_message

# Definir los pines GPIO Sensor de Distancia
trig_pin1 = machine.Pin(13, machine.Pin.OUT)
echo_pin1 = machine.Pin(12, machine.Pin.IN)

trig_pin2 = machine.Pin(14, machine.Pin.OUT)
echo_pin2 = machine.Pin(27, machine.Pin.IN)

# Configuración de los pines para los sensores táctiles
pin_touch1 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
pin_touch2 = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)

# Función para medir la distancia
def measure_distance(trig_pin, echo_pin):
    # Enviar pulso al sensor
    trig_pin.value(0)
    time.sleep_us(2)
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    # Medir la duración del eco
    duration = machine.time_pulse_us(echo_pin, 1, 3000)

    # Calcular la distancia en cm
    distance = duration / 58

    return int(distance)  # Convertir distancia a entero

# Set the IP address and port of the OSC server (the device receiving the messages)
ip = "192.168.60.95"
port = 8001

# Create an OSC client
osc = Client(ip, port)

# Bucle principal
while True:
    # Medir la distancia del primer sensor
    distance1 = measure_distance(trig_pin1, echo_pin1)
    print("Distancia del sensor 1:", distance1, "cm")

    # Medir la distancia del segundo sensor
    distance2 = measure_distance(trig_pin2, echo_pin2)
    print("Distancia del sensor 2:", distance2, "cm")
    
    # Leemos el estado de los sensores táctiles
    touch1 = not pin_touch1.value()
    touch2 = not pin_touch2.value()
    
    # Imprimimos el estado de los sensores táctiles
    print("Sensor 1:", touch1)
    print("Sensor 2:", touch2)
    
    # Esperamos un segundo antes de volver a leer los sensores
    time.sleep(0.1)
    
    # You can also send multiple messages in a bundle
    bundle = Bundle(
        create_message("/tounity/slider1", distance1),
        create_message("/tounity/slider2", distance2),
    )
    osc.send(bundle)
    print("Bundle sent:", bundle)
    
    if touch1:
        osc.send(create_message("/tounity/jump", 0))
    else:
        osc.send(create_message("/tounity/jump", 3))

    if touch2:
        osc.send(create_message("/tounity/luz", 1))
    else:
        osc.send(create_message("/tounity/luz", 0))
    print("Buttons sent")
    
    #esperamos a enviar el mensaje
    time.sleep(0.1)
    