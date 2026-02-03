import asyncio
import time


# SYNCHRONOUS (Normal) Function
def sync_function():
    """
    Normal function - blocking
    """
    print("Sync: Starting")
    time.sleep(2)  # Blocking sleep
    print("Sync: Done")
    return "Sync Result"


# ASYNCHRONOUS (Coroutine) Function
async def async_function():
    """
    Async function - non-blocking
    'async' keyword se ye coroutine ban jata hai
    """
    print("Async: Starting")
    await asyncio.sleep(2)  # Non-blocking sleep (control release kar deta hai)
    print("Async: Done")
    return "Async Result"


# Sync execution
print("=== Synchronous ===")
start = time.time()
sync_function()
sync_function()
print(f"Time: {time.time() - start:.2f}s")  # ~4 seconds

# Async execution
print("\n=== Asynchronous ===")


async def main():
    start = time.time()
    # await keyword: "Isko execute karo, jab tak wait ho control release karo"
    await async_function()
    await async_function()
    print(f"Time: {time.time() - start:.2f}s")  # Still ~4 seconds (sequential await)


# Event loop run karo
asyncio.run(main())  # Python 3.7+ way

# Concurrent async execution
print("\n=== Concurrent Asynchronous ===")


async def main_concurrent():
    start = time.time()
    # asyncio.gather: Multiple coroutines ko ek sath chalata hai
    await asyncio.gather(async_function(), async_function())
    print(f"Time: {time.time() - start:.2f}s")  # ~2 seconds (concurrent)


asyncio.run(main_concurrent())
