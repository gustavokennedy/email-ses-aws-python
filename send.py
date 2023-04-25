import boto3
from botocore.exceptions import ClientError

# By Gustavo Kennedy Renkel

SENDER = "Overall.Cloud <contato@overall.cloud>"

# Destinatário
RECIPIENT = "renkelkennedy@gmail.com"

# Região do envio na AWS - Ohio
AWS_REGION = "us-east-2"

# Assunto
SUBJECT = "Teste Python SES"

# Corpo do E-mail
BODY_TEXT = ("Enviando email com SES, Python e CLI AWS\r\n"
             "Esse email foi enviado com Amazon SES usando "
             "AWS SDK para Python (Boto)."
            )

# Corpo em HTML
BODY_HTML = """<html>
<head></head>
<body>
  <h1>ALERTA!</h1>
  <p>Item bugado</p>
  <p><a href="#">Acesse o item para verificar.</a></p>

        <p>Mensagem enviada automática.</p>
        <p><i>Não responda!</i></p>
</body>
</html>
            """

# Decode do Charset
CHARSET = "UTF-8"

# Cria o recurso SES e especifica a região
client = boto3.client('ses',region_name=AWS_REGION)

# Try para enviar email
try:
    #Especifica o conteúdo do email
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # Se não usar o Configuration_Set comentar ou deletar a linha seguinte
        #ConfigurationSetName=CONFIGURATION_SET,
    )
# Mostra erro se o envio deu errado
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Mensagem enviada com sucesso!\nID da mensagem é:"),
    print(response['MessageId'])
