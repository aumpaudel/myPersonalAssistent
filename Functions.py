import os
import re
import io
import asyncio
import tempfile
import edge_tts
import webbrowser
from pytube import Search
from datetime import datetime
import speech_recognition as sr
from State import a
from Utilies import pick_response, extract_music_name, extract_number
from Dictionaries import SOUNDS, APP_ALIASES
from contextlib import redirect_stdout, redirect_stderr
from Decoder import decode, decode_action,decode_intent
class Jarvis(): 
    async def speak_mixed(self, text):
        """
        The function `speak_mixed` asynchronously generates speech from text using a specific voice and
        plays it back using the `afplay` command in Python.
        
        :param text: The `text` parameter in the `speak_mixed` function is the input text that you want
        to convert into speech using a text-to-speech (TTS) engine. In this case, the function uses the
        `edge_tts.Communicate` class to generate an audio file from
        """
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                temp_path = f.name

            communicate = edge_tts.Communicate(
                text=text,
                voice="hi-IN-SwaraNeural",
                rate="+0%",
                volume="+0%"
            )

            await communicate.save(temp_path)
            await asyncio.to_thread(os.system, f'afplay "{temp_path}"')

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def speak_offline(self, text):
        """
        The function `speak_offline` takes a text input, escapes double quotes, and uses the `say`
        command in macOS to speak the text offline with the voice "Kiyara" at a rate of 180 words per
        minute.
        
        :param text: The `text` parameter in the `speak_offline` function is the text that you want the
        computer to speak offline using the `say` command. This text will be processed to ensure that
        any double quotes are escaped before passing it to the `say` command
        """
        safe_text = text.replace('"', '\\"')
        os.system(f'say -v Kiyara -r 180 "{safe_text}"')

    def speak(self,text):
        """
        The function `speak` in the provided Python code handles speaking text either online or offline,
        utilizing asyncio for asynchronous operations.
        
        :param text: The `text` parameter in the `speak` method is the text that you want the assistant
        (Jarvis🤖) to speak out loud. This text will be processed by the method to determine whether to
        speak it using a network connection or offline
        """
        a.state_update("speaking")
        try:
            if self.network:
                try:
                    loop = asyncio.get_running_loop()
                except RuntimeError:
                    loop = None

                if loop and loop.is_running():
                    # already in async loop
                    loop.create_task(self.speak_mixed(text))
                else:
                    asyncio.run(self.speak_mixed(text))
            else:
                self.speak_offline(text)

        except Exception as e:
            self.speak_offline(text)

        print(f"Jarvis🤖: {text}")

    def listen(self):
        """
        The `listen` function uses the SpeechRecognition library in Python to listen for audio input
        from a microphone, adjust for ambient noise, recognize speech using Google's speech recognition
        API, and return the recognized command in lowercase.
        :return: The `listen` method returns the recognized command as a lowercase string with leading
        and trailing whitespaces removed. If a `sr.WaitTimeoutError` or `sr.UnknownValueError` occurs
        during the speech recognition process, an empty string is returned. If any other exception
        occurs, an empty string is also returned after printing the error message.
        """
        a.state_update("listening")
        try:
            if not hasattr(self, "r"):
                self.r = sr.Recognizer()

            with sr.Microphone() as source:
                print("🎧 Listening...")
                self.r.adjust_for_ambient_noise(source, duration=0.3)
                audio = self.r.listen(source, timeout=5, phrase_time_limit=8)

            command = self.r.recognize_google(audio, language="en-IN")
            print(f"Aum🫡: {command}")
            return command.lower().strip()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print("Listening error:", e)
            return ""
        
    def play_sound(self,sound_type):
        """
        The function `play_sound` plays a specified sound file using the `afplay` command in Python.
        
        :param sound_type: The `sound_type` parameter in the `play_sound` function is used to specify
        the type of sound that should be played. This function checks if the `sound_type` is valid
        (exists in the `SOUNDS` dictionary) and then plays the corresponding sound file located in the
        "Sounds"
        :return: If the `sound_type` is not found in the `SOUNDS` dictionary, then `None` will be
        returned.
        """
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if sound_type not in SOUNDS:
            return 

        sound_path = os.path.join(BASE_DIR, "Sounds", SOUNDS[sound_type])
        os.system(f'afplay "{sound_path}" &')
   
    def volume(self, action, value=None):
        """
        The function allows for setting, increasing, decreasing, muting, and unmuting the volume on a
        system using AppleScript in Python.
        
        :param action: The `action` parameter in the `volume` method is used to specify the action to be
        performed on the volume control. It can have the following values:
        :param value: The `value` parameter in the `volume` method represents the volume level that you
        want to set or adjust. It is used in conjunction with the `action` parameter to perform
        different actions such as setting the volume, increasing or decreasing the volume by a specific
        amount, muting or unmuting
        :return: The `volume` method returns different responses based on the `action` parameter
        provided. If the action is successfully executed, it returns a response indicating that the
        action was completed (e.g., "volume_set", "volume_increase", "volume_decrease", "volume_mute",
        "volume_unmute"). If there is an issue or an error occurs during the execution of the action, it
        returns a
        """
        try:
            action = action.lower()

            if action == "set":
                if value is None:
                    self.play_sound("error")
                    self.speak(pick_response("something_wrong"))
                    return

                value = max(0, min(100, value))
                os.system(f'osascript -e "set volume output volume {value}"')
                self.play_sound("done")
                self.speak(pick_response("volume_set"))

            elif action == "increase":
                if value is None:
                    value = 10
                os.system(
                    f'osascript -e "set currentVolume to output volume of (get volume settings)" '
                    f'-e "set volume output volume (currentVolume + {value})"'
                )
                self.play_sound("done")
                self.speak(pick_response("volume_increase"))

            elif action == "decrease":
                if value is None:
                    value = 10
                os.system(
                    f'osascript -e "set currentVolume to output volume of (get volume settings)" '
                    f'-e "set volume output volume (currentVolume - {value})"'
                )
                self.play_sound("done")
                self.speak(pick_response("volume_decrease"))

            elif action == "mute":
                os.system('osascript -e "set volume with output muted"')
                self.play_sound("done")
                self.speak(pick_response("volume_mute"))

            elif action == "unmute":
                os.system('osascript -e "set volume without output muted"')
                self.play_sound("done")
                self.speak(pick_response("volume_unmute"))

            else:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))

        except Exception:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def get_time(self):
        """
        The function `get_time` retrieves the current time, plays a sound, and speaks the time in a
        specific format, handling errors by playing an error sound and speaking a predefined response.
        """
        try:
            now = datetime.now()
            self.play_sound("done")
            self.speak(now.strftime("%I:%M %p"))
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def brightness_up(self, steps=5):
        """
        The function `brightness_up` increases the brightness of the screen by sending key codes using
        AppleScript and provides feedback through sound and speech.
        
        :param steps: The `steps` parameter in the `brightness_up` function represents the number of
        times the brightness will be increased. By default, it is set to 5, but you can provide a
        different value when calling the function, defaults to 5 (optional)
        """
        try:
            steps = max(1, int(steps))
            for _ in range(steps):
                os.system('osascript -e \'tell application "System Events" to key code 144\'')
            self.play_sound("done")
            self.speak(pick_response("brightness_increase"))
        except Exception:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def brightness_down(self,steps=5):
        """
        The function `brightness_down` decreases the brightness of the screen by sending key codes using
        AppleScript in Python.
        
        :param steps: The `steps` parameter in the `brightness_down` function represents the number of
        times the brightness will be decreased by pressing the brightness down key. By default, it is
        set to 5, but you can provide a different value when calling the function, defaults to 5
        (optional)
        """
        try:
            steps = max(1,int(steps))
            for _ in range(steps):
                os.system(
                    'osascript -e \'tell application "System Events" to key code 145\''
                )
            self.play_sound("done")
            self.speak(pick_response("brightness_decrease"))
        except Exception:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def play(self, song):
        """
        The `play` function plays a song by searching for it, opening the first result in a web browser,
        and providing feedback through sound and speech, handling errors gracefully.
        
        :param song: The `song` parameter in the `play` method is a string that represents the title of
        the song that the user wants to play. This method searches for the song using the `Search` class
        and plays the first result found on YouTube by opening the video in a web browser. If an error
        :return: If the `play` method is executed successfully without any exceptions, it will return
        None.
        """
        try:
            f = io.StringIO()
            with redirect_stdout(f), redirect_stderr(f):
                results = Search(f'{song} official').results

            if not results:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))
                return

            result = results[0]
            webbrowser.open(f'https://youtu.be/{result.video_id}')
            self.play_sound("done")
            self.speak(pick_response("music_play"))

        except Exception as e:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))
            print(f'Error: {e}')

    def open_app(self,app_name):
        """
        The function `open_app` attempts to open a specified application using its alias, playing sounds
        and providing feedback messages in case of errors.
        
        :param app_name: The `app_name` parameter in the `open_app` function is a string that represents
        the name of the application that you want to open. This function tries to open the specified
        application using the `os.system` command. If the application name is not found in the
        `APP_ALIASES
        :return: If the `app` variable is not found in the `APP_ALIASES` dictionary, the function will
        return without opening any application.
        """
        try:
            key = app_name.lower().strip()
            app = APP_ALIASES.get(key)
            if not app:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))
                return
            os.system(f'open -a "{app}"')
            self.play_sound("done")
            self.speak(f"Opnening {app}")
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def close_app(self,app_name):
        """
        The function `close_app` attempts to close a specified application using its alias, playing
        sounds and providing feedback messages in case of errors.
        
        :param app_name: The `app_name` parameter in the `close_app` function is a string that
        represents the name of the application that you want to close. It is used to identify the
        application that the user wants to quit
        :return: If the `app` variable is not found in the `APP_ALIASES` dictionary, the function will
        return without closing any application.
        """
        try:
            key = app_name.lower().strip()
            app = APP_ALIASES.get(key)
            if not app:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))
                return
            os.system(f'osascript -e \'tell application "{app}" to quit\'')
            self.play_sound("done")
            self.speak(f"Closing {app}")
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def wifi_status(self):
        """
        This Python function checks the status of the WiFi connection and provides corresponding audio
        and spoken feedback.
        """
        try:
            result = os.popen("networksetup -getairportpower en0").read().lower()
            if "on" in result and "off" not in result:
                self.play_sound("done")
                self.speak("Wifi On")
            elif "off" in result:
                self.play_sound("done")
                self.speak("Wifi Close")
            else:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def bluetooth_status(self):
        """
        This Python function checks the status of Bluetooth and provides corresponding audio and spoken
        feedback based on the status.
        """
        try:
            state = os.popen("blueutil -p").read().strip()
            if state == "1":
                self.play_sound("done")
                self.speak("Bluetooth is On")
            elif state == "0":
                self.play_sound("done")
                self.speak("Bluetooth is off")
            else:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def internet_status(self):
        """
        The function checks the internet connection status and provides audio feedback in Hindi.
        """
        try:
            response = os.system("ping -c 1 -W 1 8.8.8.8 > /dev/null 2>&1")
            if response == 0: 
                self.play_sound("done")
                self.speak("इंटरनेट चालू है")
            else: 
                self.play_sound("done")
                self.speak("इंटरनेट नहीं चल रहा")
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def lock_screen(self):
        """
        The `lock_screen` function locks the screen of the device and provides feedback through sound
        and speech based on the success or failure of the operation.
        """
        result = os.system("pmset displaysleepnow")
        if result == 0:
            self.play_sound("done")
            self.speak(pick_response("lock_done"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))
    
    def take_screenshot(self):
        """
        The function `take_screenshot` captures a screenshot and provides feedback based on the success
        or failure of the operation.
        """
        path = os.path.expanduser("~/Desktop/screenshot.png")
        result = os.system(f'screencapture "{path}"')

        if result == 0:
            self.play_sound("done")
            self.speak(pick_response("screenshot_done"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))
   
    def uptime(self):
        """
        The `uptime` function in Python reads the system uptime, extracts the number of days, and speaks
        the result in Hindi if available.
        :return: The `uptime` method is returning the number of days the system has been up if it is
        found in the output of the `uptime` command. If the system has been up for less than a day, it
        will return "Less than a day". If there is an error or if the uptime information cannot be
        extracted from the output, it will return a response indicating that something went wrong.
        """
        try:
            uptime_output = os.popen("uptime").read().strip().lower()
            match = re.search(r'up\s+(\d+)\s+day', uptime_output)
            if match:
                days = match.group(1)
                self.play_sound("done")
                self.speak(f"{days} दिन")
                return

            if "up" in uptime_output:
                self.play_sound("done")
                self.speak("Less than a day")
            else:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))

        except Exception:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def get_day(self):
        """
        The function `get_day` retrieves and speaks the current day of the week while handling potential
        errors.
        """
        try: 
            self.play_sound("done")
            self.speak(datetime.now().strftime("%A"))
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def get_date(self):
        """
        The function `get_date` plays a sound and speaks the current date in a specific format, handling
        errors with appropriate responses.
        """
        try:
            self.play_sound("done")
            self.speak(datetime.now().strftime("%d %B %Y"))
        except:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def battery_status(self):
        """
        This Python function retrieves and displays the battery status of a device in Hindi language.
        """
        try:
            out = os.popen("pmset -g batt").read().lower()

            match = re.search(r'(\d+)%', out)
            if not match:
                raise ValueError("Battery percentage not found")

            percent = match.group(1)

            if "ac power" in out and "charging" in out:
                state = "चार्ज हो रही है"
            elif "battery power" in out or "discharging" in out:
                state = "डिस्चार्ज हो रही है"
            else:
                state = "चार्ज पूरी है"

            self.play_sound("done")
            self.speak(f"बैटरी {percent}% {state}")

        except Exception:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def bluetooth_on(self, a=True):
        """
        The function `bluetooth_on` turns on Bluetooth using the `blueutil` command and provides audio
        feedback based on the result.
        
        :param a: The `a` parameter in the `bluetooth_on` function is a boolean parameter with a default
        value of `True`. It is used to determine whether to perform additional actions after turning on
        the Bluetooth. If `a` is `True`, it will play a sound and speak a response related to, defaults
        to True (optional)
        """
        result = os.system("blueutil -p 1")

        if result == 0:
            if a:
                self.play_sound("done")
                self.speak(pick_response("bluetooth_on"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def bluetooth_off(self, a=True):
        """
        The function `bluetooth_off` turns off Bluetooth using the `blueutil` command and provides audio
        feedback based on the result.
        
        :param a: The `a` parameter in the `bluetooth_off` method is a boolean parameter with a default
        value of `True`. It is used to determine whether to perform additional actions after turning off
        the Bluetooth. If `a` is `True`, it will play a sound and speak a response related to, defaults
        to True (optional)
        """
        result = os.system("blueutil -p 0")

        if result == 0:
            if a:
                self.play_sound("done")
                self.speak(pick_response("bluetooth_off"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def wifi_on(self, a=True):
        """
        The function `wifi_on` turns on the Wi-Fi connection and provides audio and spoken feedback
        based on the result.
        
        :param a: The `a` parameter in the `wifi_on` method is a boolean parameter with a default value
        of `True`. It is used to determine whether to perform additional actions after turning on the
        Wi-Fi. If `a` is `True`, the method will play a sound and speak a response specific, defaults to
        True (optional)
        """
        result = os.system("networksetup -setairportpower en0 on")

        if result == 0:
            if a:
                self.play_sound("done")
                self.speak(pick_response("wifi_on"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def wifi_off(self, a=True):
        """
        The function `wifi_off` turns off the wifi connection and provides audio feedback based on the
        success or failure of the operation.
        
        :param a: The `a` parameter in the `wifi_off` method is a boolean parameter with a default value
        of `True`. It is used to determine whether to perform additional actions after turning off the
        Wi-Fi. If `a` is `True`, it will play a sound and speak a response related to, defaults to True
        (optional)
        """
        result = os.system("networksetup -setairportpower en0 off")

        if result == 0:
            if a:
                self.play_sound("done")
                self.speak(pick_response("wifi_off"))
        else:
            self.play_sound("error")
            self.speak(pick_response("something_wrong"))

    def airplane_mode_on(self):
        """
        The function `airplane_mode_on` turns off WiFi and Bluetooth, plays a sound, and speaks a
        response indicating that airplane mode is on.
        """
        self.wifi_off(False)
        self.bluetooth_off(False)
        self.play_sound("done")
        self.speak(pick_response("airplane_on"))

    def airplane_mode_off(self):
        """
        The function `airplane_mode_off` turns off WiFi and Bluetooth, plays a sound, and speaks a
        response indicating that airplane mode is off.
        """
        self.wifi_on(False)
        self.bluetooth_on(False)
        self.play_sound("done")
        self.speak(pick_response("airplane_off"))

    def ask_action_question(self, intent):
        """
        The function `ask_action_question` returns a specific question based on the given intent or a
        default question if the intent is not recognized.
        
        :param intent: The `intent` parameter in the `ask_action_question` function is used to determine
        which question to ask the user based on the specific action they want to perform. The function
        returns a question related to the intent provided, such as "wifi", "bluetooth", "volume",
        "brightness", "
        :return: The `ask_action_question` function returns a question based on the provided `intent`.
        If the `intent` matches one of the keys in the `questions` dictionary, it returns the
        corresponding question. If the `intent` does not match any key in the dictionary, it returns the
        default question "What should I do?".
        """
        questions = {
            "wifi": "Wi-Fi on or off?",
            "bluetooth": "Bluetooth on or off?",
            "volume": "Increase, decrease, or set?",
            "brightness": "Increase, decrease, or set?",
            "music": "What do you want to play?",
            "system": "What should I do?",
            "app": "Open or close?"
        }

        return questions.get(intent, "What should I do?")

    def toggle_humour(self):
        a.humour = not a.humour
        self.play_sound("done")
        if a.humour:
            self.speak("Humour mode on 😄")
        else:
            self.speak("Humour mode off 🙂")

    def router(self):
        while True:
            command = self.listen()
            if not command:
                continue

            intent, action, value = decode(command)
            print(intent,action,value)
            if intent is None and action in ["lock", "screenshot"]:
                intent = "system"
            elif intent is None and action in ["date", "day", "battery", "uptime", "time"]:
                intent = "info"
            elif intent is None and action in ["stop", "sleep", "wake", "HUMOUR_WORDS"]:
                intent = "assistant"

            # -------- ASKING PHASE --------

            # intent missing but action exists
            if intent is None and action is not None:
                self.speak(f"What should I {action}?")
                self.play_sound("start")
                follow_up = self.listen()
                self.play_sound("done")
                intent = decode_intent(follow_up)

                if intent is None:
                    self.speak("Sorry, I didn't understand.")
                    return

            # intent exists but action missing
            elif intent is not None and action is None:
                self.speak(self.ask_action_question(intent))
                self.play_sound("start")
                follow_up = self.listen()
                self.play_sound("done")
                action = decode_action(follow_up)

                if action is None:
                    self.speak("Sorry, I didn't understand.")
                    return

            # action is set but value missing
            elif action == "set" and value is None:
                self.speak(self.ask_value_question(intent))
                self.play_sound("start")
                follow_up = self.listen()
                self.play_sound("done")
                value = extract_number(follow_up)

                if value is None:
                    self.speak("Sorry, I didn't understand.")
                    return
            
            a.last_action = action
            a.last_intent = intent
            a.last_value = value
            a.state_update("thinking")
            print(intent,action,value)
            # -------- EXECUTION PHASE --------

            if intent == "wifi":
                if action == "on":
                    self.wifi_on()
                elif action == "off":
                    self.wifi_off()
                elif action == "status":
                    self.wifi_status()

            elif intent == "bluetooth":
                if action == "on":
                    self.bluetooth_on()
                elif action == "off":
                    self.bluetooth_off()
                elif action == "status":
                    self.bluetooth_status()

            elif intent == "volume":
                self.volume(action, value)

            elif intent == "brightness":
                if action == "increase":
                    self.brightness_up(value or 5)
                elif action == "decrease":
                    self.brightness_down(value or 5)
                elif action == "set":
                    self.brightness_set(value)

            elif intent == "music":
                if action == "play":
                    song = extract_music_name(command)
                    if song:
                        self.play(song)
                    else:
                        self.speak("Which song should I play?")
                        self.play_sound("start")
                        follow_up = self.listen()
                        self.play_sound("done")
                        a.state_update("thinking")
                        song = extract_music_name(follow_up)
                        if song:
                            self.play(song)
                        else:
                            self.play_sound("error")
                            self.speak(pick_response("something_wrong"))

            elif intent == "system":
                if action == "lock":
                    self.lock_screen()
                elif action == "screenshot":
                    self.take_screenshot()

            elif intent == "info":
                if action == "time":
                    self.get_time()
                elif action == "date":
                    self.get_date()
                elif action == "day":
                    self.get_day()
                elif action == "battery":
                    self.battery_status()
                elif action == "uptime":
                    self.uptime()

            elif intent == "assistant":
                if action == "sleep":
                    self.speak(pick_response("assistant_sleep"))
                    a.set_sleep_mode(True)
                    return
                elif action == "wake":
                    self.play_sound("error")
                    self.speak("Already active...")
                elif action == "stop":
                    self.speak(pick_response("assistant_stop"))
                    a.stop = True
                    return

                elif action == "HUMOUR_WORDS":
                    self.toggle_humour()
                

            else:
                self.play_sound("error")
                self.speak(pick_response("something_wrong"))

jarvis = Jarvis()
# jarvis.play("play baby")