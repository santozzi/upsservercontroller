import requests as req
from bs4 import BeautifulSoup
import time
import os
import datetime
import urllib3
from colorama import init, Fore, Back, Style
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



def loggeo():
    nuevaSesion = sesion.get(url, verify=False, headers={'Cache-Control': 'no-cache'})
    global key_cookie
    global value_cookie
    key_cookie = sesion.cookies.keys()[0]
    value_cookie = sesion.cookies[key_cookie]
    return nuevaSesion

def onBattery():
    shutdownServer = 'xe.exe -s '+ip_servidor+' -u root -pw ems867'
    #os.system(commandOnBattery)
    os.system('calc')

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
init()

os.system('cls')
print(Fore.BLUE + titulo())

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
        onBattery()
        print(Fore.RED + estado.get_text(), '-', hora_actual, '-', fecha_actual)
    elif estado.get_text() == "On Line":
        print(Fore.GREEN + estado.get_text(), '-', hora_actual, '-', fecha_actual)
    else:
        print(Fore.YELLOW + estado.get_text(), '-', hora_actual, '-', fecha_actual)

