import pdfplumber
import pandas as pd

# Função para extrair dados do PDF e organizar em um DataFrame
def extrair_dados_pdf_para_excel(pdf_path, output_excel_path):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            texto = page.extract_text()
            linhas = texto.split('\n')
            
            # Variáveis para armazenar informações de cada evento
            data = None
            horario = None
            local = None
            trilha = None
            
            # Extrair informações
            for linha in linhas:
                # Logica para identificar padrões de data, horário, local e trilha
                if 'Trilha' in linha:
                    trilha = linha
                elif 'Auditório' in linha or 'Modular' in linha:
                    local = linha
                elif ' às ' in linha:
                    horario = linha.replace(' às ', ' - ')
                elif '2024' in linha:  # Detectar linha com data
                    data = linha
                
                # Adicionar dados à lista quando todas as informações estão disponíveis
                if data and horario and local and trilha:
                    dados.append([data, horario, local, trilha])
                    data, horario, local, trilha = None, None, None, None

    # Criar DataFrame e definir colunas
    df = pd.DataFrame(dados, columns=['Data', 'Horário', 'Local', 'Trilha'])
    
    # Salvar DataFrame em um arquivo Excel
    df.to_excel(output_excel_path, index=False)
    print(f"Arquivo Excel '{output_excel_path}' gerado com sucesso com os dados extraídos do PDF.")

# Caminho do PDF e do Excel de saída
pdf_path = "1.BBDIGITALWEEK.pdf"
output_excel_path = "3.Informações_Extraídas.xlsx"

# Executar extração e salvar em Excel
extrair_dados_pdf_para_excel(pdf_path, output_excel_path)
