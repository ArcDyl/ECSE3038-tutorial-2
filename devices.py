readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

# print each device's name and temperature
def list_devices(devices):
    for device in devices:
        print(f"{device['name']}: {device['temp']}°C")

list_devices(readings)

# return the average temperature
def average_temp(devices):
    sum_temp = 0
    for device in devices:
        sum_temp+= device['temp']
        avg_temp = sum_temp / len(devices)
    return avg_temp

avg_temp = average_temp(readings)
print(f"Average temperature: {avg_temp:.2f}°C")

# return the whole dictionary of the hottest device
def hottest(devices):
    hottest_temp = 0.0
    hottest_device = None
    for device in devices:
        if device['temp'] > hottest_temp:
            hottest_temp = device['temp']
            hottest_device = device
    return hottest_device

hottest_device = hottest(readings)
print(f"{hottest_device['name']}: {hottest_device['room']}: {hottest_device['temp']}°C: {hottest_device['online']}")

# take one device, return a new dictionary
def to_status(device):
    status = {
        "device": device["name"],
        "status": "online" if device["online"] else "offline",
        "celsius": device["temp"],
    }
    return status

print(to_status(readings[3]))

# return a dictionary of room names to lists of device names
def by_room(devices):
    room_dict = {}
    for device in devices:
        room = device["room"]
        if room not in room_dict:
            room_dict[room] = []
        room_dict[room].append(device["name"])
    return room_dict


print(by_room(readings))