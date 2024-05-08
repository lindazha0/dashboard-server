# Send an MQTT message as if we were a node
import time
import struct
import paho.mqtt.publish as publish
from IPython import embed


MQTT_BROKER = "en1-pi.eecs.tufts.edu"

# TEAM = "eccentric-egret"
TEAM = "fire-nation"
NODE = "n3"


# Construct the payload
timestamp = int(time.time())          # 8 bytes
sensor_temp = int(23.125 * 1000)      # 4 bytes
thermistor_temp = int(22.893 * 1000)  # 4 bytes
battery = 90  # 1 byte
userdata = b"Arbitrary team-specific data"
userlen = len(userdata)  # 2 bytes

if userlen >= 2**16:
  print("Can't send data over 2^16-1 bytes in one message!")
  exit()

blob = bytearray(19 + userlen)
struct.pack_into("qiib", blob, 0, timestamp, sensor_temp, thermistor_temp, battery)
struct.pack_into("h", blob, 17, userlen)
blob[19:] = userdata

# publish.single(f"nodes/{TEAM}/{NODE}", blob, hostname=MQTT_BROKER)
publish.single(f"czhao07/hw5/new_test", 'test', hostname=MQTT_BROKER)


