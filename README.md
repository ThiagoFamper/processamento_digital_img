Este código realiza o seguinte processo:
1. Converte páginas de um arquivo PDF em imagens;
2. Usa OCR para extrair texto das imagens;
3. Aplica correção ortográfica no texto extraído;
4. Salva o texto corrigido em um arquivo txt.

Antes de rodar certifique-se de instalar as bibliotecas:
- pip install pytesseract pdf2image pillow spellchecker

E também que possue os seguintes programas baixados e adicionados ao PATH:
- [Tesseract](https://github.com/tesseract-ocr/tesseract/releases)
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases)

Como rodar:
Substitua o nome do arquivo da linha 12 para o nome do seu arquivo pdf e execute o código.
