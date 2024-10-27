import pdfplumber

# Função para extrair e visualizar dados do PDF para análise
def visualizar_dados_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            texto = page.extract_text()
            linhas = texto.split('\n')
            print(f"\n--- Página {page_number + 1} ---\n")
            for i, linha in enumerate(linhas[:20]):  # Exibindo as primeiras 20 linhas de cada página para análise
                print(f"Linha {i + 1}: {linha}")

# Caminho do PDF
pdf_path = "1.BBDIGITALWEEK.pdf"

# Executar visualização de dados
visualizar_dados_pdf(pdf_path)
