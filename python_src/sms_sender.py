# -*- coding: utf-8 -*-
from twilio.rest import Client


def send_sms(to_number):
    account_sid = 'ACdf255c5db2239e5616b057e2b1024c45'
    auth_token = 'eeb7bc044903daa4ba55e4a8610cd54e'
    client = Client(account_sid, auth_token)
    from_number = '+18149147506'
    try:
        message = 'Bem-vindo à Nova Direita! A sua filiação foi efectuada com sucesso. Dentro de instantes receberá um Email com os dados para pagamento das suas quotas. Agradecemos a sua colaboração e esperamos que a sua experiência na ND seja positiva e gratificante.'
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        return f'SMS sent successfully. Message SID: {message.sid}'
    except Exception as err:
        return f'Erro ao enviar SMS: {err}'
