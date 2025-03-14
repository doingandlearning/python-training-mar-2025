from multiprocessing import Process, set_start_method
# from concurrent import futures
# import asyncio
import time



def task(msg):
    for _ in range(0, 10):
        time.sleep(1)
        print(msg)

if __name__ == "__main__":
    print("Starting")
    set_start_method("spawn")
    processes = [Process(target=task, args=[message])
                 for message in ["input1", "input2", "input3"]
                 ]
    for process in processes:
        process.start()
    time.sleep(5)