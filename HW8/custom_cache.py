import time




# @decorator
def main(i):
    time.sleep(i / 10)
    return i ** 2


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
