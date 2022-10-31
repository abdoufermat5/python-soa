import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("---------------PERFORMANCE---------------")
        print("Temps d'exécution (en s): %.2f" % (end - start))

    return wrapper
