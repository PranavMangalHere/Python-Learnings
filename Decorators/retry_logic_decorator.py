import requests
import time

def retry(
    max_retries = 3, delay = 2,
    exceptions=(Exception,)
    ):
    def decorator(func):
        def wrapper(*args, **kwrgs):
            for attempt in range(1, max_retries+1):
                try :
                    return func(*args, **kwrgs)
                except exceptions as e:
                    if attempt == max_retries:
                        print("Max retries reached")
                        raise
                    print(f"Retrying in {delay} seconds...\n")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(
    max_retries=3,
    delay=2,
    exceptions=(
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.HTTPError
    )
)
def get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=3
    )
    response.raise_for_status()
    return response.json()
data = get_users()
print(data)