from threading import Thread
import time
import random


results_dict = {}

# { "sensor_name": {"timestamp": "reading", , , } }


def task(sensor_name):
    counter = 10
    while counter > 0:
        print(sensor_name)
        timestamp = time.time()
        if sensor_name not in results_dict:
            results_dict[sensor_name] = {}
        results_dict[sensor_name][timestamp] = random.random()
        time.sleep(2)
        counter -= 1


thread = Thread(target=task, args=["sensor1"])
thread2 = Thread(target=task, args=["sensor2"])
thread3 = Thread(target=task, args=["sensor3"])
thread4 = Thread(target=task, args=["sensor4"])

def summarize_readings():
    counter = 10
    while counter > 0:
        for sensor in results_dict:
            print(f"{sensor} average: {sum(results_dict[sensor].values())/len(results_dict[sensor])}")
        time.sleep(2)
        counter -= 1

processing_thread = Thread(target=summarize_readings)



thread.start()
thread2.start()
thread3.start()
thread4.start()
processing_thread.start()

# while True:
#     time.sleep(2)
#     print(results_dict)

print("Waiting for threads to finish.")

thread.join()
thread2.join()
thread3.join()
thread4.join()
processing_thread.join()

print("All work - exiting now")