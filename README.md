
# 🔍 SensitivePathFuzzer

O **SensitivePathFuzzer** é uma ferramenta desenvolvida em Python para identificar arquivos e diretórios sensíveis em aplicações web. Usando uma wordlist e requisições multithreaded, a ferramenta testa caminhos comuns para encontrar arquivos deixados inadvertidamente em servidores — como `.env`, `backup.zip`, `.git/config` e outros.

## 🧠 Objetivo

O principal objetivo do `SensitivePathFuzzer` é apoiar atividades de **pentest** e **análise de segurança**, revelando arquivos potencialmente confidenciais que estejam acessíveis via web sem autenticação.

---

## ⚙️ Funcionalidades

- Entrada de URL alvo via terminal.
- Leitura de uma wordlist de caminhos comuns.
- Execução multithread para acelerar o processo.
- Verificação de status HTTP das requisições.
- Armazenamento de arquivos válidos encontrados.
- Geração de log com os resultados da varredura.

---

## 🛠 Requisitos

- Python 3.x
- Biblioteca `requests`

### 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/adrielck/SensitivePathFuzzer.git
cd SensitivePathFuzzer
pip install requests
```

---

## ▶️ Como usar

1. Crie ou edite a `wordlist.txt` com os nomes dos arquivos/diretórios desejados (um por linha).
2. Execute o script:

```bash
python script.py
```

3. Insira a URL alvo (exemplo: `https://exemplo.com/`).
4. Os resultados serão salvos em:

- `resultados.txt`: log de arquivos encontrados/protegidos.
- `arquivos_encontrados/`: diretório com os conteúdos acessíveis baixados.

---

## 📂 Estrutura do Projeto

```
├── script.py                    # Script principal
├── wordlist.txt                 # Wordlist de caminhos a testar
├── resultados.txt               # Resultado da execução
└── arquivos_encontrados/        # Conteúdos de arquivos encontrados
```

---

## 📌 Exemplo de uso

Entrada:

```
Digite a URL do alvo (ex: https://site.com/): https://sitealvo.com/
```

Saída esperada:

```
[+] Encontrado: https://sitealvo.com/.env (Status: 200, Tamanho: 321)
[-] Protegido: https://sitealvo.com/.git/config (Status: 403)
[!] Erro em https://sitealvo.com/backup.zip: Connection timed out
```

---

## ⚠️ Aviso Legal

> Esta ferramenta deve ser utilizada **apenas em ambientes controlados** ou com **autorização explícita**. O uso não autorizado pode violar leis locais e políticas de segurança. Use com responsabilidade.

---

## 👨‍💻 Autor

Adrielck  
Desenvolvedor Python com foco em segurança ofensiva e automação de testes.

---

## 📬 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir *issues* ou enviar *pull requests* com melhorias, sugestões de funcionalidades ou correções de bugs.




