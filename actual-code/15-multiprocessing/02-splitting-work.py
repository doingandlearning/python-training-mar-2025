from multiprocessing import Process, set_start_method, cpu_count, Queue
import time
data = list(range(1, 10_000_001))


def compute_sum(numbers, result_queue):
    result_queue.put(sum(numbers))  # as the task cpu complexity!


if __name__ == "__main__":
    set_start_method("spawn")
    num_workers = cpu_count()
    chunk_size = len(data) // num_workers

    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers + 1)]

    if (num_workers + 1) * chunk_size < len(data):
        chunks[-1].append(data[-1])

    processes = []
    result_queue = Queue()

    start_time = time.time()

    for chunk in chunks:
        process = Process(target=compute_sum, args=(chunk, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total = 0
    for _ in processes:
        total += result_queue.get()

    end_time = time.time()
    print(f"Total sum: {total}")
    print(f"Total time: {end_time-start_time} using {num_workers}.")

    start_time = time.time()
    total = sum(data)
    end_time = time.time()
    print(f"Total sum: {total}")
    print(f"Total time: {end_time - start_time} using single process.")