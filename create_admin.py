import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings') # Verifique se sua pasta chama 'setup'
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
email = 'admin@capitalx.com.br'
password = 'admin' # TROQUE POR UMA SENHA SUA

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario '{username}' criado com sucesso!")
else:
    print(f"Superusuario '{username}' ja existe.")