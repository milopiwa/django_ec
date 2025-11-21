# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_ec',  # db name 
        'USER': 'postgres',   # user name
        'PASSWORD': 'root',   # password
        'HOST': 'localhost',
        'PORT': '5432',
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
}
}
}
