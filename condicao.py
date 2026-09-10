import pyautogui

pyautogui.alert('alerta com pyautogui!')

idade = pyautogui.prompt('Informe a sua idade: ')

idade = int(idade)

if idade < 18:
    pyautogui.alert('Você é menor de idade!')
else: 
    pyautogui.alert('Você é maior de idade!')