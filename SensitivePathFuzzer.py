import requests
import threading
from queue import Queue
import os

# URL alvo
base_url = input("Digite a URL do alvo (ex: https://site.com/): ").strip()
if not base_url.startswith("http"):
    base_url = "http://" + base_url

# Arquivo com a wordlist (1 caminho por linha, ex: .env, backup.zip, .git/config)
wordlist_file = "wordlist.txt"

# Arquivo de saída
output_file = "resultados.txt"

# Número de threads
num_threads = 10

# Fila de arquivos para testar
fila = Queue()

# Cria diretório para salvar conteúdos
os.makedirs("arquivos_encontrados", exist_ok=True)

# Lê wordlist
with open(wordlist_file, "r") as f:
    arquivos = [linha.strip() for linha in f if linha.strip()]

# Prepara o arquivo de saída
with open(output_file, "w") as f:
    f.write("📂 Resultados do Fuzzing de Arquivos Sensíveis\n")
    f.write(f"Alvo: {base_url}\n\n")

# Adiciona todos os arquivos na fila
for arquivo in arquivos:
    url = base_url.rstrip("/") + "/" + arquivo
    fila.put((arquivo, url))

# Função para verificar os arquivos
def fuzz():
    while not fila.empty():
        nome_arquivo, url = fila.get()
        try:
            resposta = requests.get(url, timeout=5)
            if resposta.status_code == 200 and len(resposta.text) > 50:
                resultado = f"[+] Encontrado: {url} (Status: 200, Tamanho: {len(resposta.text)})"
                print(resultado)
                with open(output_file, "a") as f:
                    f.write(resultado + "\n")
                # Salvar conteúdo
                safe_name = nome_arquivo.replace("/", "_")
                with open(f"arquivos_encontrados/{safe_name}", "w", encoding="utf-8", errors="ignore") as arq:
                    arq.write(resposta.text)
            elif resposta.status_code in [401, 403]:
                resultado = f"[-] Protegido: {url} (Status: {resposta.status_code})"
                print(resultado)
                with open(output_file, "a") as f:
                    f.write(resultado + "\n")
        except Exception as e:
            erro = f"[!] Erro em {url}: {e}"
            print(erro)
            with open(output_file, "a") as f:
                f.write(erro + "\n")
        fila.task_done()

# Inicia as threads
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=fuzz)
    t.start()
    threads.append(t)

# Aguarda todas as threads terminarem
fila.join()
for t in threads:
    t.join()

print(f"\n✅ Fuzzing finalizado. Resultados em '{output_file}' e arquivos salvos na pasta 'arquivos_encontrados/'")
