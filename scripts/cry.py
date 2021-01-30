from cryptography.fernet import Fernet as cryp
from os.path import exists
from os import remove
import sys
import os

def encra(fileadr):
    if exists(addr('data/wrvRbZBXYn')):
        remove(addr('data/wrvRbZBXYn'))
    if exists(addr('data/jhCFjYEeAscSdkZX')):
        remove(addr('data/jhCFjYEeAscSdkZX'))

    with open(addr(fileadr),'rb') as f:
        dt = f.read()

    c = cryp.generate_key()
    with open(addr('data/wrvRbZBXYn'), 'wb') as f:
        f.write(c)
    cryptor = cryp(c)

    with open(addr('data/jhCFjYEeAscSdkZX'),'wb') as f:
        f.write(cryptor.encrypt(dt))
    return

def decra():
    with open(addr('data/jhCFjYEeAscSdkZX'),'rb') as f:
        dt = f.read()
    with open(addr('data/wrvRbZBXYn'), 'rb') as f:
        c = f.read()
    f = cryp(c)
    dc = f.decrypt(dt)
    with open(addr('data/.fKfIASBfFufCPItc'),'wb') as f:
        f.write(dc)
    return

def addr(relativo):
    try:
        end = sys._MEIPASS
    except Exception:
        end = os.path.abspath('.')
    return os.path.join(end, relativo)
