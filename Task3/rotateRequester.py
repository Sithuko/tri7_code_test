import requests
import itertools
import time

proxies = [
    "http://localhost:8001",
    "http://localhost:8002",
    "http://localhost:8003"
]

server_url = "http://localhost:3000/user"

proxy_usage_count = {proxy: 0 for proxy in proxies}

proxy_cycle = itertools.cycle(proxies)

def send_request_with_proxy():
    for _ in range(50):
        proxy = next(proxy_cycle)

        if proxy_usage_count[proxy] >= 10:
            continue

        try:
            print(f"Trying proxy {proxy}...")
            response = requests.get(server_url, proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                print(f"Response from server: {response.text} using proxy {proxy}")
                proxy_usage_count[proxy] += 1
            else:
                print(f"Failed to get response from server using proxy {proxy}: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error with proxy {proxy}: {e}")

        time.sleep(1)

send_request_with_proxy()
