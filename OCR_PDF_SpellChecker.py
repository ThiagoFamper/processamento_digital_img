from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from spellchecker import SpellChecker
import os

# cria um diretório para armazenar as imagens
if not os.path.exists("paginas"):
    os.makedirs("paginas")

# converte o pdf pra imagem
imagens = convert_from_path("Mussum Ipsum.pdf")
texto_completo = ""

spell = SpellChecker(language='pt')

for i, img in enumerate(imagens):
    nome_imagem = f"paginas/pagina{i}.jpg"
    img.save(nome_imagem, "JPEG")
    print(f"Página {i} salva como imagem")

    # extrai o texto da imagem com OCR
    texto_extraido = pytesseract.image_to_string(img, lang='por')

    # divide as palavras e verifica uma por uma com o spellchecker
    palavras = texto_extraido.split()
    palavras_corrigidas = []
    for palavra in palavras:
        palavra_corrigida = spell.correction(palavra)
        if palavra_corrigida is None:
            palavra_corrigida = palavra
        palavras_corrigidas.append(palavra_corrigida)

    texto_corrigido = " ".join(palavras_corrigidas)
    texto_completo += texto_corrigido + "\n"

# salva o texto no arquivo txt
with open("texto_extraido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_completo)

print("Texto extraído e corrigido salvo em 'texto_extraido.txt'")