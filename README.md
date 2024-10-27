# BB Digital Week 2024 - Extração de Dados de Eventos

![BB Digital Week](https://example.com/banner.jpg) <!-- Substitua pelo link de um banner relevante, se houver -->

## Descrição 📄
Durante a **BB Digital Week 2024**, um evento cheio de palestras, workshops e painéis de discussão, vimos a necessidade de organizar dados de diversos eventos, com horários e datas bagunçados no formato PDF. Este script Python foi criado para extrair e organizar automaticamente esses dados, facilitando a visualização e análise das informações em uma planilha Excel estruturada. Ideal para eventos com várias atividades e uma programação extensa!

## Contexto 📅
Dado o volume de informações desorganizadas no PDF oficial da BB Digital Week, nosso objetivo era criar uma maneira fácil de extrair dados, como título do evento, horário, local e trilha temática, e organizá-los em uma tabela clara e bem estruturada. Isso ajuda a visualizar a programação completa do evento de forma prática e eficiente.

## Funcionalidades ✨
- **Extração Automática de Dados**: Extraímos todas as informações sobre cada evento, incluindo **data**, **horário**, **local** e **trilha**.
- **Organização e Estruturação em Excel**: Os dados são salvos em uma planilha Excel organizada para fácil visualização.
- **Compatível com Arquivos PDF Complexos**: Adaptado para lidar com múltiplas páginas e formatos de texto variados, garantindo que todas as informações sejam capturadas.

## Estrutura do Projeto 📂

- `1.BBDIGITALWEEK.pdf`: Arquivo PDF original do evento BB Digital Week 2024, contendo a programação completa.
- `2.BBDIGITALWEEK.py`: Script Python para extração e organização dos dados.
- `3.Informações_Extraídas.xlsx`: Arquivo Excel gerado com os dados extraídos e organizados.

## Tecnologias Utilizadas 💻
- **Python**: Linguagem principal para automação.
- **pdfplumber**: Biblioteca para leitura e extração de textos de PDFs.
- **pandas**: Biblioteca para manipulação e exportação de dados em formato de planilha.

## Requisitos 🛠️
1. Python 3.6 ou superior
2. Bibliotecas necessárias:
   ```bash
   pip install pdfplumber pandas openpyxl
