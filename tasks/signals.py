import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if os.environ.get('CREATE_SUPERUSER'):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'Admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'nachogonzalez1132@gmail.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin1')

        if not User.objects.filter(username=username).exists():
            print('Creando superusuario...')
            User.objects.create_superuser(username=username, email=email, password=password)
            print('Superusuario creado con éxito.')
        else:
            print('El superusuario ya existe.')
