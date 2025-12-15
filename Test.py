from Functions import jarvis
import time
# play sounds for specific work
jarvis.play_sound("wake")
time.sleep(1.5)
jarvis.play_sound("stop")
time.sleep(1.5)
jarvis.play_sound("done")
time.sleep(1.5)
jarvis.play_sound("start")
time.sleep(1.5)
jarvis.play_sound("error")
time.sleep(1.5)

#music play in youtube directly 
jarvis.play("At peace")

#volume Control
jarvis.volume("increase")
time.sleep(1.5)
jarvis.volume("increase",15)
time.sleep(1.5)
jarvis.volume("decrease")
jarvis.volume("decrease",15)
time.sleep(1.5)
jarvis.volume("mute")
time.sleep(1.5)
jarvis.volume("unmute")
time.sleep(1.5)

#day,date,time Control
jarvis.get_date()
jarvis.get_day()
jarvis.get_time()
jarvis.uptime()

#some basic on/off and status
jarvis.airplane_mode_off()
time.sleep(1)
jarvis.airplane_mode_on()
time.sleep(1)
jarvis.wifi_status()
time.sleep(1)
jarvis.wifi_off()
time.sleep(1)
jarvis.wifi_on()
time.sleep(1)
jarvis.bluetooth_status()
time.sleep(1)
jarvis.bluetooth_off()
time.sleep(1)
jarvis.bluetooth_on()
time.sleep(1)
jarvis.battery_status()
time.sleep(1)
jarvis.internet_status()
time.sleep(1)
#open/close app
jarvis.open_app("Spotify")
time.sleep(3)
jarvis.close_app("Spotify")
time.sleep(2)

#system
jarvis.lock_screen()
time.sleep(2)
jarvis.take_screenshot()
time.sleep(4)

#humour enable/disable 
jarvis.toggle_humour()

#brightness
jarvis.brightness_down(15)
jarvis.brightness_down() #if no value then its 5
jarvis.brightness_up(15)
jarvis.brightness_down() #if no value then its 5
