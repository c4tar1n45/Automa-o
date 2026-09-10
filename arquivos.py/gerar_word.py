from docx import Document
doc = Document('relatorio_mensal.docx')
doc.add_heading('Relatório Mensal', level=1)
doc.add_paragraph('Este é o relatório mensal gerado automaticamente com python-docx.')

table = doc.add_table(rows=2, cols=3) #Cria uma tabela com 2 linhas e 3 colunas.
table.cell(0, 0).text = 'Produto'  #Define o conteúdo da célula
table.cell(0, 1).text = 'Quantidade'
table.cell(0, 2).text = 'Preço'

doc.add_paragraph('Relatório salvo em excel para consulta detalhada.')
doc.save('relatorio_mensal.docx')