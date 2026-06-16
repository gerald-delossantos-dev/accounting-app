from app.workers.celery_app import celery_app

@celery_app.task
def generate_invoice_pdf(invoice_id: str) -> dict:
    return {"invoice_id": invoice_id, "status": "queued_pdf_generation"}

@celery_app.task
def send_invoice_email(invoice_id: str, recipient: str) -> dict:
    return {"invoice_id": invoice_id, "recipient": recipient, "status": "queued_email"}
