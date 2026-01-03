import asyncio
import time
import httpx
from collections import Counter

URL = "http://localhost/"
TOTAL_REQUESTS = 200
CONCURRENCY = 20


async def fetch(client: httpx.AsyncClient, request_id: int):
    start = time.perf_counter()
    try:
        response = await client.get(URL, timeout=5.0)
        elapsed = time.perf_counter() - start

        data = response.json()
        container = data.get("message", "unknown")

        return {
            "status": response.status_code,
            "container": container,
            "latency": elapsed,
        }

    except Exception as e:
        return {
            "status": "error",
            "container": "error",
            "latency": None,
            "error": str(e),
        }


async def run_test():
    limits = httpx.Limits(max_connections=CONCURRENCY)
    async with httpx.AsyncClient(limits=limits) as client:
        tasks = [fetch(client, i) for i in range(TOTAL_REQUESTS)]

        start_time = time.perf_counter()
        results = await asyncio.gather(*tasks)
        total_time = time.perf_counter() - start_time

    return results, total_time


def summarize(results, total_time):
    successes = [r for r in results if r["status"] == 200]
    failures = [r for r in results if r["status"] != 200]

    latencies = [r["latency"] for r in successes if r["latency"]]
    containers = [r["container"] for r in successes]

    print("\n===== Stress Test Summary =====")
    print(f"Total requests     : {TOTAL_REQUESTS}")
    print(f"Concurrent workers : {CONCURRENCY}")
    print(f"Total time (s)     : {total_time:.2f}")
    print(f"Requests/sec      : {TOTAL_REQUESTS / total_time:.2f}")
    print(f"Success responses : {len(successes)}")
    print(f"Failed responses  : {len(failures)}")

    if latencies:
        print("\nLatency (seconds):")
        print(f"  Min : {min(latencies):.4f}")
        print(f"  Avg : {sum(latencies) / len(latencies):.4f}")
        print(f"  Max : {max(latencies):.4f}")

    print("\nRequests per container:")
    for container, count in Counter(containers).items():
        print(f"  {container} -> {count}")


if __name__ == "__main__":
    results, total_time = asyncio.run(run_test())
    summarize(results, total_time)
