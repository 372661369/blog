from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', '372661369@qq.com',['24810281@qq.com'], fail_silently=False)