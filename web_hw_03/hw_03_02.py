import time
import multiprocessing


def factorize_multi(*numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(factorize_single, numbers)
    return result


def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]


if __name__ == "__main__":
    start_time_multi = time.time()
    a, b, c, d = factorize_multi(128, 255, 99999, 10651060)
    end_time_multi = time.time()

    print(f"Factorize parallel execution time: {end_time_multi - start_time_multi:.6f} seconds")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
