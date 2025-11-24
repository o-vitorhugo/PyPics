from pypics.funcoes import (
    preto_e_branco,
    rotacionar,
    redimensionar,
    espelhar_horizontal,
    blur_simples
)
import os

# Pastas
originais = "imagens_originais"
processadas = "imagens_processadas"

# Criar pasta de saída se não existir
os.makedirs(processadas, exist_ok=True)

# Extensões válidas
extensoes = (".jpg", ".jpeg", ".png")

print("Procurando imagens...")

# Listar imagens da pasta de entrada
imagens = [img for img in os.listdir(originais) if img.lower().endswith(extensoes)]

if not imagens:
    print("Nenhuma imagem encontrada em /imagens_originais")
    exit()

for imagem in imagens:
    nome, ext = os.path.splitext(imagem)
    caminho_entrada = os.path.join(originais, imagem)

    # Gerar caminhos de saída
    saida_pb = os.path.join(processadas, f"{nome}_pb{ext}")
    saida_rot = os.path.join(processadas, f"{nome}_rot90{ext}")
    saida_red = os.path.join(processadas, f"{nome}_red{ext}")
    saida_esp = os.path.join(processadas, f"{nome}_esp{ext}")
    saida_blur = os.path.join(processadas, f"{nome}_blur{ext}")

    preto_e_branco(caminho_entrada, saida_pb)
    rotacionar(caminho_entrada, saida_rot, 90)
    redimensionar(caminho_entrada, saida_red, 300)
    espelhar_horizontal(caminho_entrada, saida_esp)
    blur_simples(caminho_entrada, saida_blur)

    print(f"- {imagem} processada!")

print("\n✓ Processamento concluído! Verifique a pasta imagens_processadas.")