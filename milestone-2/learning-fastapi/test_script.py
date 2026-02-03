import asyncio
import httpx
import time

BASE_URL = "http://127.0.0.1:8000"


async def send_request(client: httpx.AsyncClient, endpoint: str) -> float:
    """Send a single request and return the response time."""

    start = time.time()
    await client.get(f"{BASE_URL}{endpoint}")
    end = time.time()
    return end - start


async def test_endpoint(endpoint: str, num_requests: int = 100) -> float:
    """Send multiple concurrent requests to an endpoint and return total time."""
    async with httpx.AsyncClient(timeout=None) as client:
        start_time = time.time()
        tasks = [send_request(client, endpoint) for _ in range(num_requests)]
        await asyncio.gather(*tasks)
        end_time = time.time()
        return end_time - start_time


async def main():
    print("Testing /io-bound (async endpoint)...")
    io_time = await test_endpoint("/io-bound")
    print(f"Total time for 100 requests to /io-bound: {io_time:.2f} seconds")

    print("\nTesting /cpu-bound (sync endpoint)...")
    cpu_time = await test_endpoint("/cpu-bound")
    print(f"Total time for 100 requests to /cpu-bound: {cpu_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
