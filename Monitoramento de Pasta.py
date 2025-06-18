import time
import smtplib
from email.message import EmailMessage
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Função para enviar o e-mail
def enviar_email_alerta(mensagem):
    email_origem = 'seuemail@gmail.com'
    senha = 'sua_senha_de_app'  # senha de app do Gmail
    email_destino = 'destinatario@gmail.com'

    msg = EmailMessage()
    msg.set_content(mensagem)
    msg['Subject'] = '🚨 Alerta: Atividade detectada na pasta'
    msg['From'] = email_origem
    msg['To'] = email_destino

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_origem, senha)
        smtp.send_message(msg)
        print("⚠ Alerta enviado por e-mail!")

# Classe para detectar mudanças
class MonitorDePasta(FileSystemEventHandler):
    def on_modified(self, event):
        enviar_email_alerta(f"Arquivo modificado: {event.src_path}")

    def on_created(self, event):
        enviar_email_alerta(f"Arquivo criado: {event.src_path}")

    def on_deleted(self, event):
        enviar_email_alerta(f"Arquivo deletado: {event.src_path}")

# Caminho da pasta a ser monitorada
pasta_monitorada = r'C:\Users\SeuUsuario\Desktop\PastaMonitorada'  # Troque pelo seu caminho

# Inicia a observação
observer = Observer()
observer.schedule(MonitorDePasta(), path=pasta_monitorada, recursive=False)
observer.start()

print(f"⏳ Monitorando a pasta: {pasta_monitorada}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()