from PIL import Image


imagem_caminho = "naruto.jpg"


try:
    imagem = Image.open(imagem_caminho)
    print("Imagem carregada com sucesso!")
except FileNotFoundError:
    print(f"Erro: Arquivo '{imagem_caminho}' não encontrado.")
    exit()

# Converter para tons de cinza
imagem_cinza = imagem.convert("L")

print("Imagem convertida para tons de cinza e salva como 'naruto_cinza.jpg'.")

# Converter para binária (preto e branco)
threshold = 128 
imagem_binaria = imagem_cinza.point(lambda p: 255 if p > threshold else 0)

print("Imagem binarizada e salva como 'naruto_binaria.jpg'.")

# Mostrar as imagens (opcional)
imagem.show(title="Imagem Original")
imagem_cinza.show(title="Imagem em Cinza")
imagem_binaria.show(title="Imagem Binária")

