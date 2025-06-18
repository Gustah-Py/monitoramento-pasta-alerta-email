# monitoramento-pasta-alerta-email
# 📁 Monitoramento de Pasta com Alerta por E-mail

Automação desenvolvida em Python para monitorar uma pasta específica e enviar *alertas por e-mail* sempre que houver *criação, modificação ou exclusão de arquivos*. Útil para controle de arquivos sensíveis ou pastas compartilhadas.

---

## 🚀 Funcionalidades

- 📌 Monitoramento em tempo real de alterações em uma pasta.
- ✉ Envio automático de e-mails com o tipo de evento detectado.
- 🔒 Útil para segurança, auditoria ou acompanhamento de pastas importantes.

---

## 🧪 Tecnologias Utilizadas

- Python 3
- [Watchdog](https://pypi.org/project/watchdog/) – para monitorar arquivos
- smtplib + email.message – para envio de e-mails
- os, time – bibliotecas padrão

---

## ⚙ Como Usar

### 1. Clonar o repositório

```bash
git clone https://github.com/Gustah-Py/monitoramento-pasta-alerta-email.git
cd monitoramento-pasta-alerta-email

## 2. Instale as dependências necessárias:

Esse comando instala as bibliotecas que o script precisa, como o watchdog.

pip install -r requirements.txt

> Se não tiver o requirements.txt, instale manualmente com:

pip install watchdog




## 3. Configure seu e-mail e a pasta que será monitorada:

No código Python (ex: monitorar_pasta.py), altere essas variáveis:

EMAIL = "seuemail@gmail.com"          # Seu e-mail Gmail
SENHA = "sua-senha-de-aplicativo"     # Senha de app do Gmail
PASTA_MONITORADA = "C:/caminho/da/pasta"

⚠ Você precisa gerar uma senha de aplicativo do Gmail se estiver usando autenticação em duas etapas.


## 4. Execute o script:

Rode o programa para iniciar o monitoramento da pasta.

python monitorar_pasta.py

O terminal vai mostrar mensagens como:

[+] Arquivo criado: relatorio.txt
[!] Alerta enviado para seuemail@gmail.com


## 5. Pronto!
Agora sempre que um arquivo for criado, alterado ou excluído na pasta, você vai receber um alerta por e-mail automático.

