from app.celery_app import app as celery_app

import logging

log = logging.getLogger("celery")

@celery_app.task
def five_min_bot():
    print("five min bot do something")
    try:
        log.info("five min bot do something")
    except:
        pass