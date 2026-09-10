#Imagine que você está desenvolvendo um bot para um aplicativo de previsão do tempo. Seu bot deverá:

#Perguntar ao usuário a temperatura atual (em graus Celsius).

#Classificar essa temperatura em uma das faixas:

#Muito Frio: abaixo de 10 °C

#Frio: entre 10 °C e 18 °C

#Agradável: entre 18 °C e 26 °C

#Quente: entre 26 °C e 35 °C

#Muito Quente: acima de 35 °C

#Dica: Teste o bot com diferentes valores (por exemplo: 5 °C, 15 °C, 22 °C, 30 °C, 40 °C) para verificar se as mensagens exibidas estão corre

import pyautogui

temperatura = pyautogui.prompt('Qual é a temperatura atual? ')
temperatura = int(temperatura)


if temperatura < 10:
    pyautogui.alert('A temperatura está muito frio.')
elif 10 < temperatura < 18:
    pyautogui.alert('A temperatura está fria.')
elif 18 < temperatura < 26:
    pyautogui.alert('A temperatura está agradável.')
elif 26 < temperatura < 35:
    pyautogui.alert('A temperatura está quente.')
else: 
    temperatura > 35
    pyautogui.alert('A temperatura está muto quente.')


