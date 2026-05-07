import time

def retry_action(func, retries=3):

    for attempt in range(retries):

        try:
            return func()

        except Exception:
            time.sleep(1)

    raise Exception("Action failed after retries")