# EDS_auth (Electronic Digital Signature Auth)
Це універсальна Django-бібліотека для авторизації користувачів за допомогою Електронного Цифрового Підпису (ЕЦП). 
Альтернативний спосіб входу у профіль за ЕЦП (Публічний/Приватний ключі).
------

# Особливості
Автоматичне створення профілів: Кожен новий користувач автоматично отримує EDS-профіль. (Публічний ключ, який прив'язаний до профілю в моделі)
Безпека: Сервер зберігає лише Публічний ключ. Приватний ключ (ключ) зберігається тільки у користувача. Тобто потрібна реалізація завантаження ключа клієнту, який зареєструвався, щоб у подальшому він мав змогу увійти в свій профіль за допомогою приватного ключа.
------

# Встановлення
1. pip install .
---
2. Додати в налаштування (settings.py):

INSTALLED_APPS = [
    ...,
    'EDS_auth',
]
---
3. Налаштування бекенда авторизації (settings.py):

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Стандартний вхід (пароль)
    'EDS_auth.backend.EDSBackend',               # Вхід за ЕЦП
]
---
4.Застосування міграцій:

Створіть необхідні таблиці в базі даних для зберігання публічних ключів:

python manage.py migrate
------

# Використання

Приклад реалізації Реєстрації (у вашому views.py)

```python
# Ваші_додатки/views.py
from django.http import HttpResponse
from EDS_auth.utils import generate_user_keys

def register_view(request):
    # 1. Створюємо юзера (профіль створиться автоматично)
    user = User.objects.create_user(username=request.POST['username'])
    
    # 2. Генеруємо пару ключів (публічний і приватний)
    private_pem, public_pem = generate_user_keys()
    
    # 3. Зберігаємо публічний ключ у профіль
    user.eds_profile.public_key = public_pem
    user.eds_profile.save()
    
    # 4. Віддаємо приватний ключ користувачу як файл
    response = HttpResponse(private_pem, content_type='application/x-pem-file')
    response['Content-Disposition'] = 'attachment; filename="my_private_key.pem"'
    return response
```

!!!
Бажана модифікація форми реєстрації, тобто попередження про завантаження приватного ключа користувачу на пристрій, реалізація завантаження - ваша рощробка
!!!

Приклад реалізації Авторизації (у вашому views.py):

Для входу викличте стандартну функцію authenticate, передавши туди логін, дані та підпис.

Python

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    # Отримуємо підпис (наприклад, завантажений файл або текст з форми)
    signature = request.FILES['signature_file'].read()
    data = b"some_original_data" # Дані, які були підписані

    user = authenticate(
        request, 
        username=request.POST['username'], 
        data=data, 
        signature=signature
    )

    if user:
        login(request, user)
        return redirect('dashboard')
    return HttpResponse("Помилка підпису!", status=401)
```