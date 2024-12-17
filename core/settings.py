import datetime
import os

# https://django-environ.readthedocs.io/en/latest/getting-started.html#installation
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env(
    # django
    DJANGO_ADMINS=(list, []),
    DJANGO_ALLOWED_HOSTS=(
        list,
        [
            "127.0.0.1",
            "localhost",
            "0.0.0.0",
            "elektroservice-koenig.de",
            "www.elektroservice-koenig.de",
            "www.koenig39.de",
            "koenig39.de",
        ],
    ),
    DJANGO_STATIC_ROOT=(str, "staticfiles"),
    DJANGO_MEDIA_ROOT=(str, "media"),
    DJANGO_SECURE_HSTS_SECONDS=(int, 2592000),
    DJANGO_SESSION_COOKIE_SECURE=(bool, False),
    # Emailing
    DJANGO_DEFAULT_FROM_EMAIL=(
        str,
        "",
    ),
    DJANGO_HELLO_EMAIL=(str, ""),
    DJANGO_BACKOFFICE_EMAIL=(str, ""),
    # Sentry
    DJANGO_SENTRY_DSN=(str, ""),
    DJANGO_SENTRY_ENVIRONMENTS=(str, "local"),
    DEBUG=(bool, False),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
environ.Env.read_env()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")
ADMINS = tuple([tuple(admins.split(":")) for admins in env.list("DJANGO_ADMINS")])
MANAGERS = ADMINS

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]
# Application definition
INSTALLED_APPS = [
    # "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_extensions",
    "app",
    "axes",
    "django_db_logger",
    "django_mysql",  # docs https://django-mysql.readthedocs.io/en/latest/index.html
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    # "querycount.middleware.QueryCountMiddleware",  # query count
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    "axes.middleware.AxesMiddleware",
]

SITE_ID = 1

CSRF_COOKIE_SECURE = False
ROOT_URLCONF = "core.urls"

# Security envs
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env.bool("DJANGO_SECURE_HSTS_SECONDS")
if SECURE_HSTS_SECONDS > 0:
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True
# Security middleware settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = SESSION_COOKIE_SECURE

# Use X-Forwarded-Proto Header to determine SSL status (useful for API docs)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Csrf middleware settings
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE

# Referrer-Policy middleware
REFERRER_POLICY = "same-origin"
URL_PROTOCOL = "https://" if SESSION_COOKIE_SECURE else "http://"

# CSP config
CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "localhost:8000",
    "unpkg.com",
    "https://maps.googleapis.com",
    "https://fonts.googleapis.com",
    "https://fonts.gstatic.com",
    "https://maps.gstatic.com",
    "https://cdn.jsdelivr.net",
)

# Cross-site request forgery
CSRF_USE_SESSIONS = True

# Axes config
LOGIN_TIMEDELTA = 15 * 60
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 3
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = datetime.timedelta(0, LOGIN_TIMEDELTA)
AXES_DISABLE_ACCESS_LOG = False
AXES_META_PRECEDENCE_ORDER = (  # Copied from django-ipware as that is apparently not set by default
    "HTTP_X_FORWARDED_FOR",
    "X_FORWARDED_FOR",  # <client>, <proxy1>, <proxy2>
    "HTTP_CLIENT_IP",
    "HTTP_X_REAL_IP",
    "HTTP_X_FORWARDED",
    "HTTP_X_CLUSTER_CLIENT_IP",
    "HTTP_FORWARDED_FOR",
    "HTTP_FORWARDED",
    "HTTP_VIA",
    "REMOTE_ADDR",
)
# Block by Username only (i.e.: Same user different IP is still blocked, but different user same IP is not)
AXES_ONLY_USER_FAILURES = True
AXES_VERBOSE = True
# AXES_IP_BLACKLIST = env.list("BLACKLIST")
AXES_ENABLE_ACCESS_FAILURE_LOG = True
AXES_HTTP_RESPONSE_CODE = 429
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(
            BASE_DIR, "cache_files"
        ),  # Указываем, куда будем сохранять
        # кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "de-de"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = env("DJANGO_STATIC_ROOT")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = env("DJANGO_MEDIA_ROOT")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
# email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email server configuration
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_SSL = True

RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")

# Logging
DB_LOGGER_ENTRY_LIFETIME = 30
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "db_handler": {
            "level": "DEBUG",
            "class": "django_db_logger.db_log_handler.DatabaseLogHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "system": {
            "level": "INFO",
            "handlers": ["console", "db_handler"],
            "propagate": True,
        },
        "async": {
            "level": "INFO",
            "handlers": ["console", "db_handler"],
            "propagate": True,
        },
        "django_scrubber": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
        },
    },
}

QUERYCOUNT = {
    "IGNORE_REQUEST_PATTERNS": [r".*jsi18n.*"],
    "IGNORE_SQL_PATTERNS": [],
    "THRESHOLDS": {
        "MEDIUM": 50,
        "HIGH": 200,
        "MIN_TIME_TO_LOG": 0,
        "MIN_QUERY_COUNT_TO_LOG": 0,
    },
    "DISPLAY_DUPLICATES": None,
    "RESPONSE_HEADER": "X-DjangoQueryCount-Count",
}

# Sentry logging
# SENTRY_ENVIRONMENT = env("DJANGO_SENTRY_ENVIRONMENTS")
# if os.environ.get("DJANGO_SENTRY_DSN"):
#     import sentry_sdk
#     from ai_django_core.sentry.helpers import strip_sensitive_data_from_sentry_event
#     from sentry_sdk.integrations.django import DjangoIntegration
#
#     sentry_sdk.init(
#         env("DJANGO_SENTRY_DSN"),
#         integrations=[DjangoIntegration()],
#         max_breadcrumbs=50,
#         debug=DEBUG,
#         environment=SENTRY_ENVIRONMENT,
#         server_name=FRONTEND_URL,
#         send_default_pii=True,
#         before_send=strip_sensitive_data_from_sentry_event,
#     )
