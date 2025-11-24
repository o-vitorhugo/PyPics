from PIL import Image, ImageFilter

def preto_e_branco(entrada: str, saida: str) -> None:
    """
    Converte a imagem para preto e branco e salva em 'saida'.
    """
    img = Image.open(entrada)
    pb = img.convert("L")
    pb.save(saida)   

def rotacionar(entrada: str, saida: str, graus: int) -> None:
    """
    Rotaciona a imagem em 'graus' e salva em 'saida'. Ajusta as dimensões automaticamente.
    Para rotações não múltiplas de 90°, força PNG para manter transparência.
    """
    img = Image.open(entrada).convert("RGBA")  # garante canal alfa
    
    rot = img.rotate(graus, expand=True)
    
    if graus % 90 == 0:
        if saida.lower().endswith(".jpg") or saida.lower().endswith(".jpeg"):
            # JPEG não suporta alfa, converte para RGB
            rot = rot.convert("RGB")
    else:
        # rotações livres -> fundo transparente
        if not saida.lower().endswith(".png"):
            saida = saida.rsplit(".", 1)[0] + ".png"

    rot.save(saida)
    
def redimensionar(entrada: str, saida: str, tamanho: int) -> None:
    """
    Redimensiona a imagem para um quadrado de 'tamanho' x 'tamanho', mantendo proporção e cortando o excesso do centro.
    """
    img = Image.open(entrada)
    largura, altura = img.size

    # Determinar qual lado é maior e cortar centralizado
    if largura > altura:
        excesso = (largura - altura) // 2
        img_cortada = img.crop((excesso, 0, excesso + altura, altura))
    else:
        excesso = (altura - largura) // 2
        img_cortada = img.crop((0, excesso, largura, excesso + largura))

    img_final = img_cortada.resize((tamanho, tamanho))
    img_final.save(saida)

def espelhar_horizontal(entrada: str, saida: str) -> None:
    """
    Espelha a imagem horizontalmente e salva em 'saida'.
    """
    img = Image.open(entrada)
    esp = img.transpose(Image.FLIP_LEFT_RIGHT)
    esp.save(saida)

def blur_simples(entrada: str, saida: str) -> None:
    """
    Aplica um desfoque simples (blur) na imagem e salva em 'saida'.
    """
    img = Image.open(entrada)
    blur = img.filter(ImageFilter.BLUR)
    blur.save(saida)