import requests as req
from bs4 import BeautifulSoup
import time
import os
import datetime
import urllib3
from colorama import init, Fore, Back, Style
from wakeonlan import send_magic_packet

# Dirección MAC del dispositivo que deseas encender
mac_address = 'E0:69:95:57:27:72'
mac_server1_a = '1C:98:EC:52:D9:BC'
mac_server2 = '9C:DC:71:AF:52:10'
mac_server3 = '94:18:82:16:65:F4'

tiempo_espera_antes_de_prender = 15*60
def wakeOnLan(mac):
    send_magic_packet(mac)

tiempo_de_espera = 10
url = 'https://localhost:6547/logon/j_security_check/?j_username=Sergio&j_password=12345678Aa.'
status_url = 'https://localhost:6547/status'
ip_servidor = '192.168.1.53'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
commandOnBattery = 'C:\\Proyectos\\default.cmd'

sesion = req.session()

apc =sesion.get(url, verify=False, headers={'Cache-Control': 'no-cache'})

key_cookie = sesion.cookies.keys()[0]
value_cookie = sesion.cookies[key_cookie]
ruta = "C:/\"Program Files (x86)\"/Citrix/XenCenter/"
commandBaseXe =os.path.dirname(ruta)+'/xe.exe -s '+ip_servidor+' -u root -pw ems867 '
imagenXe = 'fe4e6727-81e0-7f57-98d9-1bb386d03705'
XenServerCiclo1 = '3bbba09d-5ae7-4d38-977c-934202a6c965'
XenServerCiclo2 = 'dccf4482-5b41-4c99-a9bb-76f5916a4df4'
XenServerCiclo3 = 'a8c4bd5d-cb79-4985-abb2-480440f9aeb8'

shutdownImage = commandBaseXe + 'vm-shutdown uuid=' + imagenXe + ' force=true'




startImage = commandBaseXe + 'vm-start uuid=' + imagenXe + ' force=true'
host_list = commandBaseXe + 'host-list'
def loggeo():
    nuevaSesion = sesion.get(url, verify=False, headers={'Cache-Control': 'no-cache'})
    global key_cookie
    global value_cookie
    key_cookie = sesion.cookies.keys()[0]
    value_cookie = sesion.cookies[key_cookie]
    return nuevaSesion


def getStatus():
    return sesion.get(status_url, cookies={key_cookie: value_cookie}, verify=False)


def titulo():
    return """
#   /$$   /$$/$$$$$$$  /$$$$$$                                                          
#  | $$  | $| $$__  $$/$$__  $$                                                         
#  | $$  | $| $$  \ $| $$  \__/                                                         
#  | $$  | $| $$$$$$$|  $$$$$$                                                          
#  | $$  | $| $$____/ \____  $$                                                         
#  | $$  | $| $$      /$$  \ $$                                                         
#  |  $$$$$$| $$     |  $$$$$$/                                                         
#   \______/|__/      \______/                                                          
#    /$$$$$$                                                                            
#   /$$__  $$                                                                           
#  | $$  \__/ /$$$$$$  /$$$$$$ /$$    /$$/$$$$$$  /$$$$$$                               
#  |  $$$$$$ /$$__  $$/$$__  $|  $$  /$$/$$__  $$/$$__  $$                              
#   \____  $| $$$$$$$| $$  \__/\  $$/$$| $$$$$$$| $$  \__/                              
#   /$$  \ $| $$_____| $$       \  $$$/| $$_____| $$                                    
#  |  $$$$$$|  $$$$$$| $$        \  $/ |  $$$$$$| $$                                    
#   \______/ \_______|__/         \_/   \_______|__/                                    
#    /$$$$$$                     /$$                      /$$/$$                        
#   /$$__  $$                   | $$                     | $| $$                        
#  | $$  \__/ /$$$$$$ /$$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$| $| $$ /$$$$$$  /$$$$$$       
#  | $$      /$$__  $| $$__  $|_  $$_/  /$$__  $$/$$__  $| $| $$/$$__  $$/$$__  $$      
#  | $$     | $$  \ $| $$  \ $$ | $$   | $$  \__| $$  \ $| $| $| $$$$$$$| $$  \__/      
#  | $$    $| $$  | $| $$  | $$ | $$ /$| $$     | $$  | $| $| $| $$_____| $$            
#  |  $$$$$$|  $$$$$$| $$  | $$ |  $$$$| $$     |  $$$$$$| $| $|  $$$$$$| $$            
#   \______/ \______/|__/  |__/  \___/ |__/      \______/|__|__/\_______|__/            
#  
# -> Powered by: Sergio José Antozzi 
 
 """
def disableHost(host):
    os.system( commandBaseXe + 'host-disable uuid=' + host)
def shutdownHost(host):
    os.system(commandBaseXe + 'host-shutdown uuid='+host +' force=true')

def onBattery():
    disableHost(XenServerCiclo1)
    print('Deshabilitando XenServerCiclo1')
    disableHost(XenServerCiclo2)
    print('Deshabilitando XenServerCiclo2')
    disableHost(XenServerCiclo3)
    print('Deshabilitando XenServerCiclo3')
    shutdownHost(XenServerCiclo1)
    print('Apagando XenServerCiclo1')
    shutdownHost(XenServerCiclo2)
    print('Apagando XenServerCiclo2')
    shutdownHost(XenServerCiclo3)
    print('Apagando XenServerCiclo3')


init()
os.system('cls')
#wakeOnLan(mac_address)

#print(os.system(host_list))
#print(os.system(shutdownCiclo1))
#os.system('cls')
print(Fore.BLUE + titulo())

estadoOnLine = True
while True:
    time.sleep(tiempo_de_espera)
    fecha_actual = datetime.date.today()
    hora_actual = datetime.datetime.now().time()
    apc = getStatus()
    soup = BeautifulSoup(apc.text, 'html.parser')
    estado = soup.find(id='value_DeviceStatus')

    if estado == None:
        print('none')
        apc = loggeo()
    elif estado.get_text() == "On Battery":
        if estadoOnLine:
            onBattery()
        estadoOnLine=False
        print(Fore.RED + estado.get_text(), '-', hora_actual, '-', fecha_actual)
    elif estado.get_text() == "On Line":

        print(Fore.GREEN + estado.get_text(), '-', hora_actual, '-', fecha_actual)
        if estadoOnLine==False:
            time.sleep(tiempo_espera_antes_de_prender)
            if estado.get_text() == "On Line":
                wakeOnLan(mac_server1_a)
                wakeOnLan(mac_server2)
                wakeOnLan(mac_server3)
                estadoOnLine=True
    else:
        print(Fore.YELLOW + estado.get_text(), '-', hora_actual, '-', fecha_actual)


