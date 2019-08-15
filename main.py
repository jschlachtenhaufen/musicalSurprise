import time
import subprocess

PASSWORD = "password"
SONG_PATH_FILE = './song.mp3'
OS_SCRIPT_FILE = './toggleFnState.scpt'
DELAY_TIME = 5
PLAY_TIME = 60

def main():
    installPygame()
    time.sleep(DELAY_TIME)
    mixer.init()
    mixer.music.load(SONG_PATH_FILE)
    if notMaxVolume():
        setVolume()
    toggleFnState()
    disableSleep()
    mixer.music.play()
    wait()
    mixer.music.stop()
    toggleFnState()
    enableSleep()

def installPygame():
    command = "pip install pygame"
    process = subprocess.Popen(command, shell=True)
    process.wait()
    from pygame import mixer

def setVolume():
    command = "echo {} | sudo -S osascript -e \"set Volume 10\"".format(PASSWORD)
    subprocess.Popen(command, shell=True)

def notMaxVolume():
    command = "osascript -e \"get volume settings\""
    vol = subprocess.check_output(command, shell=True)
    vol = vol.split(',')
    currVol = vol[0].split(':')[1]
    muted = vol[3].split(':')[1]
    truths = ['True', 'true', 'True\n', 'true\n']
    return float(currVol) < 100 or muted in truths

def toggleFnState():
    command = "osascript {} {}".format(OS_SCRIPT_FILE, PASSWORD)
    subprocess.Popen(command, shell=True)

def disableSleep():
    command1 = "echo {} | sudo -S pmset -b disablesleep 1".format(PASSWORD)
    command2 = "echo {} | sudo -S pmset -b sleep 0".format(PASSWORD)
    subprocess.Popen(command1, shell=True)
    subprocess.Popen(command2, shell=True)

def enableSleep():
    command1 = "echo {} | sudo -S pmset -b disablesleep 0".format(PASSWORD)
    command2 = "echo {} | sudo -S pmset -b sleep 5".format(PASSWORD)
    subprocess.Popen(command1, shell=True)
    subprocess.Popen(command2, shell=True)

def wait():
    tEnd = time.time() + PLAY_TIME
    while time.time() < tEnd:
        if notMaxVolume():
            setVolume()

if __name__ == "__main__":
    main()
