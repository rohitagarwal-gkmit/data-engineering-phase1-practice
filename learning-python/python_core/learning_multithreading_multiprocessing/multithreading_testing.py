# this is a learning module for multithreading in Python

# what is multithreading?
# Multithreading is a programming technique that allows multiple threads to run concurrently within a single process.
# Each thread can execute independently while sharing the same memory space, which can lead to improved performance, especially for I/O-bound tasks.
# Threads are lighter than processes, making it easier to create and manage multiple threads within an application.
# Multithreading is commonly used in scenarios such as web servers, GUI applications, and real-time systems where responsiveness and
# efficient resource utilization are crucial.

# multiple threads can be used to perform different tasks simultaneously,
# such as handling user input, processing data, and performing background tasks without blocking the main program flow.

# one of the key advantages of multithreading is that
# Multiple threads share the same memory space, which allows for efficient communication and data sharing between threads.

import time
import requests
from concurrent.futures import ThreadPoolExecutor


def make_request():
    requests.get("http://127.0.0.1:8000/")


def non_threading():
    # 100 requests sequentially
    for _ in range(100):
        make_request()


def thread_pooling():
    # Thread pool with max 10 worker threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit 100 tasks to the pool
        for _ in range(100):
            executor.submit(make_request)
    # exiting the `with` block waits for all tasks to complete


if __name__ == "__main__":
    print("\n--- Non-threaded run ---")
    start = time.perf_counter()
    non_threading()
    non_threaded_elapsed = time.perf_counter() - start
    print(f"\nNon-threaded elapsed: {non_threaded_elapsed:.6f} seconds")

    print("\n--- Thread pool run (10 threads, 100 requests) ---")
    start = time.perf_counter()
    thread_pooling()
    threaded_elapsed = time.perf_counter() - start
    print(f"\nThread pool elapsed: {threaded_elapsed:.6f} seconds")

    if threaded_elapsed < non_threaded_elapsed:
        print(
            "\nThread pooling by {:.6f} seconds".format(
                non_threaded_elapsed - threaded_elapsed
            )
        )
    else:
        print(
            "\nNon-threaded by {:.6f} seconds".format(
                threaded_elapsed - non_threaded_elapsed
            )
        )
