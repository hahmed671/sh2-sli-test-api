import requests
from random import choices, randrange
import time
from multiprocessing import Process
import traceback

def sli_load_test():
    endpoint = 'https://8wk8dyslla.execute-api.ca-central-1.amazonaws.com/prod/'
    while True:
        wait_time = randrange(1,10)
        method = choices(population=["GET","POST","DELETE","PUT","PATCH"], weights=[0.4, 0.4,0.18,0.01,0.01])[0]
        try:
            if method == "GET":
                r = requests.get(endpoint)
            elif method == "POST":
                r = requests.post(endpoint)
            elif method == "DELETE":
                r = requests.delete(endpoint)
            elif method == "PUT":
                r = requests.put(endpoint)
            elif method == "PATCH":
                r = requests.patch(endpoint)
            print(method, r.status_code)
        except Exception as e:
            tb_str = traceback.format_exc()
            print(tb_str)
            continue
        finally:
            time.sleep(wait_time)


if __name__ == '__main__':
    threads = 10
    for i in range(threads):
        p = Process(target=sli_load_test)
        p.start()