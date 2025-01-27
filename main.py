import time
import threading
from ping3 import ping, verbose_ping

def ping_server(host, count=100000, bot_id=1):
    """
    Pings a server to check latency using ping3.
    Args:
        host (str): The server to ping (e.g., "8.8.8.8").
        count (int): Number of ping requests to send.
        bot_id (int): The ID for this microbot.
    Returns:
        None
    """
    try:
        print(f"Bot-{bot_id}: Pinging {host}...")

        # Use ping3 to send a ping request
        for i in range(count):
            response = ping(host)  # ping3 sends ICMP requests
            if response is None:
                print(f"Bot-{bot_id}: No response from {host}.")
            else:
                print(f"Bot-{bot_id}: Response from {host}: {response} ms")

            time.sleep(1)  # Optional: Adds a delay between pings

        print(f"Bot-{bot_id}: Completed pings to {host}\n")

    except Exception as e:
        print(f"Bot-{bot_id}: An error occurred: {e}")

def start_microbots(num_bots, host="8.8.8.8", ping_interval=0.5):
    """
    Starts the specified number of microbots, each pinging the server.
    Args:
        num_bots (int): Number of microbots to start.
        host (str): The server to ping.
        ping_interval (float): Interval between each ping request.
    Returns:
        None
    """
    threads = []
    for i in range(num_bots):
        # Create a new thread for each microbot
        thread = threading.Thread(target=ping_server, args=(host, 99999, i + 1))  # Keeping count as 99999
        threads.append(thread)
        thread.start()
        time.sleep(ping_interval)  # Pause between starting threads (optional)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_bots = 100000   # Set the number of microbots to spawn (reduced to 10 for practicality)
    server = "34.120.115.37"  # Set the server you want to ping (e.g., Google's DNS server)
    ping_interval = 0.1  # Seconds between starting each microbot

    # Start the microbots
    start_microbots(num_bots, server, ping_interval)
