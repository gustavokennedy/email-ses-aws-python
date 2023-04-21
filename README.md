# Envio de Email com Python usando AWS SES
Repositório com arquivo de configuração para envio de e-mail usando serviço SES da AWS com Python3 e CLI da AWS.

> OBS: Testado com Python 3.10.6 e Ubuntu 22.04.1 LTS

## 1. Para usar o envio, faça a configuração do AWS CLI primeiro

Antes da configuração, tenha anotado os  `AWS Access Key ID` e o `AWS Secret Access Key`.

```shell
aws configure
```

Informe as credenciais:

```shell
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-2
Default output format [None]: json
```
## 2. Edita o arquivo de envio

```shell
vi send.py
```

## 3. Teste e Envia

```shell
python3 send.py
```

O retorno deve ser:

```shell
Mensagem enviada com sucesso!
ID da mensagem é:
27479485827572858...
```
