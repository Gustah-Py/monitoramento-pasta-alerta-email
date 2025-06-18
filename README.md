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
