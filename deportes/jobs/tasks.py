from celery import shared_task


@shared_task(ignore_result=True)
def beat():
    print('beat')
