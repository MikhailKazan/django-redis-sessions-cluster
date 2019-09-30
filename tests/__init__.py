from django.conf import settings


settings.configure(
    SESSION_ENGINE='redis_cluster_sessions.session'
)
