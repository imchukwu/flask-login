from datetime import timedelta

DEBUG = True
# DEBUG_TB_INTERCEPT_REDIRECTS = False
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG


SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordevelopment'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'imchukwu@gmail.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'search4iyke@gmail.com'
MAIL_PASSWORD = 'comp6252'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy.
db_uri = 'postgresql://postgres:password@postgres:5432/ids'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'search4iyke@gmail.com'
SEED_ADMIN_PASSWORD = 'password'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
