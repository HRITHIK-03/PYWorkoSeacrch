
INSTALLED_APPS = [
    # ...
    'djongo',
    'PyWork',  #Django app name
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': 'database',  # 
    }
}
