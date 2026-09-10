import pyautogui
import time
import sys
import io
#para incluir o acento no terminal 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#contagem de 1 até 10 que aguarde 0.5 segundo antes de mostrar o próximo
for i in range(1,11):
    pyautogui.alert(f'Número gerado: {i}')
    print(f'Número gerado: {i}')
    time.sleep(0.5) #aguardar meio segundo 



