import time


def cache_func(func):
    saved = {}

    def wrapper(num):

        if num not in saved:
            saved.update({num: func(num)})
        else:
            return saved[num]
    print(saved)
    return wrapper


@cache_func
def main(num):
    time.sleep(num / 10)
    return num ** 2


if __name__ == "__main__":
    start = time.time()
    results = []
    values = (1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 1, 2, 3, 2, 1, 4, 4, 1, 2, 4)
    print(values)
    for i in values:
        results.append(main(i))
    print(results)
    end = time.time()
    print(f"Total time: {end - start}")
