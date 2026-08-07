import subprocess
import re

def get_mac_wifi_ip():
    try:
        # Runs 'ifconfig en0' and grabs the text output
        output = subprocess.check_output(["ifconfig", "en0"], text=True)
        # Search specifically for the 'inet ' pattern followed by the IP address
        match = re.search(r"inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output)
        if match:
            return match.group(1)
    except Exception:
        pass
    return "127.0.0.1"  # Fallback if en0 fails

print(f"👉 To view on your phone, type this URL: http://{get_mac_wifi_ip()}:8000/houston_contacts_map.html")
