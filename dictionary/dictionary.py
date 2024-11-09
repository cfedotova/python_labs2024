def display_devices(devices):
    for device, info in devices.items():
        print(
            f"{device}: IP - {info['ip_address']}, Status - {info['security_status']}, Threats - {info['threats_detected']}")


def update_security_status(device, new_status):
    if device in network_devices:
        network_devices[device]["security_status"] = new_status
        print(f"Security status of {device} updated to {new_status}.")
    else:
        print(f"Device {device} not found in the network.")


def remove_threat(device, threat):
    if device in network_devices:
        if threat in network_devices[device]["threats_detected"]:
            network_devices[device]["threats_detected"].remove(threat)
            print(f"Threat '{threat}' removed from {device}.")
        else:
            print(f"Threat '{threat}' not found on {device}.")
    else:
        print(f"Device {device} not found in the network.")


def display_compromised_devices(devices):
    print("Compromised devices in the network:")
    for device, info in devices.items():
        if info["security_status"] == "compromised":
            print(f"{device}: IP - {info['ip_address']}, Threats - {info['threats_detected']}")


network_devices = {
    "Device1": {
        "ip_address": "192.168.1.1",
        "security_status": "compromised",
        "threats_detected": ["malware", "phishing"]
    },
    "Device2": {
        "ip_address": "192.168.1.2",
        "security_status": "safe",
        "threats_detected": []
    },
    "Device3": {
        "ip_address": "192.168.1.3",
        "security_status": "compromised",
        "threats_detected": ["ransomware"]
    }
}

print("All devices in the network:")
display_devices(network_devices)

print("\nUpdating security status of Device1 to 'safe':")
update_security_status("Device1", "safe")

print("\nRemoving threat 'malware' from Device1:")
remove_threat("Device1", "malware")

print("\nDisplaying compromised devices:")
display_compromised_devices(network_devices)
