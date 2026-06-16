from celery import Celery
from app.core.config import settings

celery_app = Celery("ledgerpro", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.task_routes = {
    "app.workers.tasks.generate_invoice_pdf": {"queue": "documents"},
    "app.workers.tasks.send_invoice_email": {"queue": "email"},
}
