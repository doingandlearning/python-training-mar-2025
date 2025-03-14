from multiprocessing import set_start_method, cpu_count, Pool
import time
data = list(range(1, 10_000_001))


def compute_sum(numbers):
    return sum(numbers)  # as the task cpu complexity!


if __name__ == "__main__":
    set_start_method("spawn")
    num_workers = cpu_count()
    chunk_size = len(data) // num_workers

    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers)]


    start_time = time.time()

    with Pool(processes=num_workers) as pool:
        results = pool.map(compute_sum, chunks)

    total_sum = sum(results)


    end_time = time.time()
    print(f"Total sum: {total_sum}")
    print(f"Total time: {end_time-start_time} using {num_workers}.")

    start_time = time.time()
    total = sum(data)

    end_time = time.time()
    print(f"Total sum: {total}")
    print(f"Total time: {end_time - start_time} using single process.")