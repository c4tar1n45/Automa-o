from reportlab.pdfgen import canvas

c = canvas.Canvas("exemplo.pdf")
c.drawString(100, 750, "Olá, este é um exemplo de PDF gerado com ReportLab!")
#A função drawString(x, y, texto) insere uma frase no local desejado, sendo que os valores de x e y 
# definem a posição na página (em pontos, onde 1 ponto = 1/72 polegada).

c.save()