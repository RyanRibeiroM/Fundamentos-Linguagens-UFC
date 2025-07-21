import os
import shutil

PASTA_ORIGEM = "origem"
PASTA_DESTINO = "destino"

MAPEAMENTO_EXTENSOES = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".pptx": "Apresentacoes",
    ".xlsx": "Planilhas",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".svg": "Imagens",
    ".zip": "Arquivos Compactados",
    ".rar": "Arquivos Compactados",
    ".7z": "Arquivos Compactados",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
    ".mp3": "Musicas",
    ".mp4": "Videos",
}

def organizar_arquivos():
    relatorio = {
        "movidos": 0,
        "ignorados": 0,
        "categorias": set()
    }
    
    arquivos_ignorados = []

    for nome_arquivo in os.listdir(PASTA_ORIGEM):
        caminho_completo_origem = os.path.join(PASTA_ORIGEM, nome_arquivo)

        if os.path.isdir(caminho_completo_origem):
            continue

        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        if extensao in MAPEAMENTO_EXTENSOES:
            nome_pasta_destino = MAPEAMENTO_EXTENSOES[extensao]
            caminho_pasta_destino = os.path.join(PASTA_DESTINO, nome_pasta_destino)

            if not os.path.exists(caminho_pasta_destino):
                os.makedirs(caminho_pasta_destino)
                print(f"Pasta '{nome_pasta_destino}' criada.")

            caminho_completo_destino = os.path.join(caminho_pasta_destino, nome_arquivo)
            shutil.move(caminho_completo_origem, caminho_completo_destino)
            print(f"Movendo '{nome_arquivo}' para '{nome_pasta_destino}'...")

            relatorio["movidos"] += 1
            relatorio["categorias"].add(nome_pasta_destino)
        else:
            relatorio["ignorados"] += 1
            arquivos_ignorados.append(nome_arquivo)

    print("\n--- Organização Concluída! ---")
    print(f"Total de arquivos movidos: {relatorio['movidos']}")
    print(f"Total de arquivos ignorados: {relatorio['ignorados']}")
    if relatorio["categorias"]:
        print(f"Categorias utilizadas: {', '.join(sorted(list(relatorio['categorias'])))}")
    if arquivos_ignorados:
        print(f"Arquivos ignorados (extensão não mapeada): {', '.join(arquivos_ignorados)}")


if __name__ == "__main__":
    if not os.path.exists(PASTA_ORIGEM):
        os.makedirs(PASTA_ORIGEM)
        print(f"Pasta '{PASTA_ORIGEM}' criada. Adicione arquivos nela para testar.")
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO)
        print(f"Pasta '{PASTA_DESTINO}' criada.")
    
    organizar_arquivos()