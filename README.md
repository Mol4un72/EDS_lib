Як підключити EDS_auth до вашого проєкту:

    Встановіть пакет: pip install . (або з PyPI).

    Додайте в settings.py:
    Python

    INSTALLED_APPS = [..., 'EDS_auth']
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'EDS_auth.backend.EDSBackend',
    ]

    Виконайте міграції: python manage.py migrate.

    При реєстрації юзера використайте from EDS_auth.utils import generate_user_keys, щоб створити ключі та зберегти публічний ключ у user.eds_profile.public_key.