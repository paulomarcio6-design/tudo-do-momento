from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.contact import ContactMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

contact_bp = Blueprint('contact', __name__)

def send_email(to_email, subject, body):
    """Enviar e-mail (função auxiliar)"""
    # Nota: Configurar SMTP posteriormente com credenciais reais
    # Por enquanto, apenas simula o envio
    try:
        # Configurações de e-mail (a serem configuradas)
        # smtp_server = "smtp.gmail.com"
        # smtp_port = 587
        # sender_email = "contato@tudodomomentopresentes.com.br"
        # sender_password = "senha"
        
        # msg = MIMEMultipart()
        # msg['From'] = sender_email
        # msg['To'] = to_email
        # msg['Subject'] = subject
        # msg.attach(MIMEText(body, 'html'))
        
        # with smtplib.SMTP(smtp_server, smtp_port) as server:
        #     server.starttls()
        #     server.login(sender_email, sender_password)
        #     server.send_message(msg)
        
        print(f"E-mail simulado enviado para {to_email}")
        print(f"Assunto: {subject}")
        print(f"Corpo: {body}")
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")
        return False

@contact_bp.route('/contact', methods=['POST'])
def submit_contact():
    """Receber e processar mensagem de contato"""
    try:
        data = request.json
        
        # Validar dados
        if not all(key in data for key in ['name', 'email', 'subject', 'message']):
            return jsonify({
                'success': False,
                'error': 'Todos os campos são obrigatórios'
            }), 400
        
        # Salvar mensagem no banco de dados
        contact_message = ContactMessage(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        
        db.session.add(contact_message)
        db.session.commit()
        
        # Enviar e-mail de notificação para a loja
        email_body = f"""
        <html>
        <body>
            <h2>Nova mensagem de contato recebida</h2>
            <p><strong>Nome:</strong> {data['name']}</p>
            <p><strong>E-mail:</strong> {data['email']}</p>
            <p><strong>Assunto:</strong> {data['subject']}</p>
            <p><strong>Mensagem:</strong></p>
            <p>{data['message']}</p>
        </body>
        </html>
        """
        
        send_email(
            'contato@tudodomomentopresentes.com.br',
            f"Nova mensagem: {data['subject']}",
            email_body
        )
        
        # Enviar e-mail de confirmação para o cliente
        confirmation_body = f"""
        <html>
        <body>
            <h2>Obrigado por entrar em contato!</h2>
            <p>Olá {data['name']},</p>
            <p>Recebemos sua mensagem e responderemos em breve.</p>
            <p><strong>Sua mensagem:</strong></p>
            <p>{data['message']}</p>
            <br>
            <p>Atenciosamente,</p>
            <p><strong>Tudo do Momento Presentes</strong></p>
        </body>
        </html>
        """
        
        send_email(
            data['email'],
            'Confirmação de recebimento - Tudo do Momento Presentes',
            confirmation_body
        )
        
        return jsonify({
            'success': True,
            'message': 'Mensagem enviada com sucesso! Responderemos em breve.'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@contact_bp.route('/contact/messages', methods=['GET'])
def get_messages():
    """Obter todas as mensagens de contato (admin)"""
    try:
        messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'messages': [msg.to_dict() for msg in messages],
            'total': len(messages)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@contact_bp.route('/contact/messages/<int:message_id>/read', methods=['PUT'])
def mark_as_read(message_id):
    """Marcar mensagem como lida"""
    try:
        message = ContactMessage.query.get(message_id)
        if not message:
            return jsonify({'success': False, 'error': 'Mensagem não encontrada'}), 404
        
        message.is_read = True
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Mensagem marcada como lida'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

