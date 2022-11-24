from concurrent.futures import thread
from functools import total_ordering
import threading

def hello_from_thread():
    print(f'Hello from thread {threading.current_thread().name}!')

hello_thread=threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads=threading.active_count()
thread_name=threading.current_thread().name

print(f'Python is currently currning {total_threads} thread(s)')
print(f'The current thread is {thread_name}')

hello_thread.join()
