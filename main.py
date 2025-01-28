import time
import threading
import requests

def http_ping(host, count=10, bot_id=1):
    """
    Simulates a ping using HTTP requests to measure response time.
    Args:
        host (str): The server to ping (e.g., "https://example.com").
        count (int): Number of ping requests to send.
        bot_id (int): The ID for this microbot.
    Returns:
        None
    """
    try:
        print(f"Bot-{bot_id}: Pinging {host} (HTTP)...")

        for i in range(count):
            start_time = time.time()
            try:
                response = requests.get(host, timeout=5)  # 5-second timeout
                response_time = (time.time() - start_time) * 1000  # Convert seconds to ms
                print(f"Bot-{bot_id}: Response from {host}: {response_time:.2f} ms (Status Code: {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Bot-{bot_id}: No response from {host}. Error: {e}")

            time.sleep(1)  # Optional: Adds a delay between requests

        print(f"Bot-{bot_id}: Completed HTTP pings to {host}\n")

    except Exception as e:
        print(f"Bot-{bot_id}: An error occurred: {e}")


def start_microbots(num_bots, host, ping_interval=0.5, count_per_bot=10):
    """
    Starts the specified number of microbots, performing HTTP ping to the target host.
    Args:
        num_bots (int): Number of microbots to start.
        host (str): The server to ping.
        ping_interval (float): Interval between starting each bot.
        count_per_bot (int): Number of pings per bot.
    Returns:
        None
    """
    threads = []

    # Add "https://" if missing for URLs
    if not host.startswith("http://") and not host.startswith("https://"):
        host = "https://" + host

    # Use HTTP ping for URLs
    for i in range(num_bots):
        thread = threading.Thread(target=http_ping, args=(host, count_per_bot, i + 1))
        threads.append(thread)
        thread.start()
        time.sleep(ping_interval)  # Pause between starting threads

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Configuration
    num_bots = 3  # Number of microbots (adjust as needed)
    target = "https://www.fet.ac"  # Change to the target server or URL (e.g., "https://example.com")
    ping_interval = 0.01  # Seconds between starting each bot
    count_per_bot = 1000000  # Number of pings per bot

    # Start the microbots
    start_microbots(num_bots, target, ping_interval, count_per_bot)
