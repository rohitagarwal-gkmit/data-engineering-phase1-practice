from fastapi import FastAPI
import httpx
import time

app = FastAPI()


# i/o bound example
@app.get("/io-bound")
async def io_bound() -> float:
    url = "https://httpbin.org/delay/2"  # Simulates a 2-second delay

    time_start = time.time()
    async with httpx.AsyncClient() as client:
        await client.get(url)

    time_end = time.time()
    print(f"IO-bound task took {time_end - time_start} seconds")
    return time_end - time_start  # return time in seconds


@app.get("/cpu-bound")
def cpu_bound_task() -> float:
    # Simulate a CPU-bound task (e.g., calculating Fibonacci)

    time_start = time.time()
    for _ in range(10**6):
        pass  # Simulating CPU work
    time_end = time.time()
    print(f"CPU-bound task took {time_end - time_start} seconds")

    return time_end - time_start  # return time in seconds
