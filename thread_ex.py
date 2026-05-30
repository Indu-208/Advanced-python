import threading
def task():
    print("Thread is running")
t1 = threading.Thread(target=task)
t1.start()