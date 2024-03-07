import pyudev
import pyttsx3

def announce_device_connected(device):
    engine = pyttsx3.init()
    engine.say(f"Device connected:{device}")
    engine.runAndWait()

def monitor_device_connection():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsytem='block')

    for action,device in monitor:
        if action =='add':
            print("device connected:",device)
            announce_device_connected(device)
            
if __name__=="__main__":
    monitor_device_connection()