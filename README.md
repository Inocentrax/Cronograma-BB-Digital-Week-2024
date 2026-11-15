# BB Digital Week 2024 — do PDF à planilha

Extração de programação de eventos de PDF para Excel com Python, pdfplumber e pandas; etapa de dados de uma agenda web.

**Status:** Projeto de automação · revisão da extração pendente.

[← Catálogo de projetos e estudos](https://github.com/Inocentrax/portfolio-dados)

---

Um fluxo criado para tornar a programação do BB Digital Week 2024 mais fácil de consultar: extrair texto de PDF, reconhecer datas/horários/locais/trilhas e exportar uma planilha.

## Fluxo

`PDF → extração de texto → reconhecimento de campos → Excel → revisão manual`

A interface que consulta os eventos está em [Site-BB-digital-Week-2024](https://github.com/Inocentrax/Site-BB-digital-Week-2024).

## Como executar

```bash
python -m pip install -r requirements.txt
python "2.Informações_Extraídas.py"
```

Execute a partir da raiz. A saída de novas execuções vai para `outputs/`, preservando as planilhas históricas. Para inspecionar o texto reconhecido:

```bash
python Teste_Arquivos.py
```

## Arquivos

| Arquivo | Papel |
|---|---|
| [1.BBDIGITALWEEK.pdf](1.BBDIGITALWEEK.pdf) | Documento de entrada |
| [2.Informações_Extraídas.py](2.Informa%C3%A7%C3%B5es_Extra%C3%ADdas.py) | Extração e exportação |
| [3.Informações_Extraídas.xlsx](3.Informa%C3%A7%C3%B5es_Extra%C3%ADdas.xlsx) | Saída histórica da extração |
| [4.Eventos Organizados.xlsx](4.Eventos%20Organizados.xlsx) | Versão organizada para consulta |
| [Teste_Arquivos.py](Teste_Arquivos.py) | Inspeção das primeiras linhas de cada página |

## Próximos passos

- [ ] Conferir quantos eventos são recuperados e quantos se perdem nas regras.
- [ ] Tratar cabeçalhos repetidos, eventos quebrados entre páginas e datas ambíguas.
- [ ] Validar ordem cronológica e intervalos de horário.
- [ ] Documentar diferenças entre a extração e a planilha revisada.

É um registro histórico de 2024, sem atualização automática da programação.
