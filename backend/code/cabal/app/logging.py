def logging(settings):
    settings['logging'] = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'generic': {
                'format':
                '%(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': "DEBUG",
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': [],
            },
            'sqlalchemy': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'sqlalchemy.engine',
            },
            'alembic': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'alembic',
            },
            'cabal': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'qualname': 'cabal',
            },
            'waitress': {
                'level': 'ERROR',
                'handlers': ['console'],
            },
        }
    }
