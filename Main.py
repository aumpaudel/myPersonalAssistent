from Functions import jarvis, router
from State import a

def main():
    while True:
        if a.stop :
            break

        wake = jarvis.listen()
        wake1 = wake.lower()
        if not wake:
            continue
        elif "jarvis" in wake or "जार्विस" in wake1:
            jarvis.speak("assistant_wake")
            router()

main()