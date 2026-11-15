# BB Digital Week 2024 - Extração de Dados de Eventos

## Descrição 📄
Pouco tempo antes do inicio do **BB Digital Week 2024**, um evento cheio de palestras, workshops e painéis de discussão, vi a necessidade de organizar dados de diversos eventos, com horários e datas bagunçados no formato PDF, queria ver tudo organizado e me preparar. Este script Python foi criado para extrair e organizar automaticamente esses dados, facilitando a visualização e análise das informações em uma planilha Excel estruturada. Ideal para eventos com várias atividades e uma programação extensa!

## Contexto 📅
Dado o volume de informações desorganizadas no PDF oficial da BB Digital Week, meu objetivo foi criar uma maneira fácil de extrair dados, como título do evento, horário, local e trilha temática, e organizá-los em uma tabela clara e bem estruturada. Isso ajuda a visualizar a programação completa do evento de forma prática e eficiente.

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

### Problema com Extração e Formato de Data

Durante o desenvolvimento do código para extrair os eventos do **BB Digital Week 2024**, enfrentamos desafios ao processar datas e horários. Como o PDF continha datas em formatos variados, houve dificuldades na conversão e na ordenação cronológica. 

Para resolver isso, o código foi ajustado para:

1. **Detecção Automática de Formatos de Data**: Usamos `pd.to_datetime` com `errors='coerce'` para lidar com formatos inconsistentes, evitando falhas e garantindo flexibilidade na conversão.
2. **Tratamento de Horários como Strings**: Mantivemos os horários como texto para preservar intervalos no formato "14h00 às 14h50", sem tentar interpretá-los como dados numéricos ou temporais.

Esses ajustes simplificam a extração, embora a formatação possa necessitar de revisão ao exportar para o Excel.


## Requisitos 🛠️
1. Python 3.6 ou superior
2. Bibliotecas necessárias:
   ```bash
   pip install pdfplumber pandas openpyxl
