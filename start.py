"""Avvia LetzyOS"""

import os
import time

def on():
    """Accende LetzyOS"""
    os.system("clear" if os.name == "posix" else "cls")
    print("Montando filesystem :/tmp/*")
    print("Aprendo LTemp...")
    print("Aprendo LetzyUserInterface...")
    time.sleep(1)
    print("Aprendo SigtermServiceLand...")
    print("Montando filesystem: :/network/*...")
    print("Aprendo SigtermServiceMSG...")
    time.sleep(3)
    print("Montando filesystem: /letzy/*...")
    time.sleep(0.7)
    print("Aprendo CmdRunCommands...")
    print("Aprendo /letzy/core/cmd...")
    print("Aprendo CmdTermRecognize...")
    time.sleep(2)
    print("Connessione come 'user'...")
    time.sleep(0.5)
    
    os.system("clear" if os.name == "posix" else "cls")
    
    
    
    

    
    
    
