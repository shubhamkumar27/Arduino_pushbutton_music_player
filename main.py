#THIS PROJECT IS CURRENTLY ONGOING. READ README.md FOR MORE INFORMATION

import serial #importing pyserial library 
from pygame import mixer # importing mixer from pygame library
mixer.init() #initialising mixer

# Start function defined
def start(path):
    ser = serial.Serial('COM5', 9600) #creating serial object

    i = 0
    j = 0
    #infinte loop
    while 1:
        data = ser.readline() # reading data from serial monitor
        if data==b'play\r\n':
            i+=1
            if i%2 !=0:
                mixer.music.load(path)
                mixer.music.play()
                print('Starting the song')
            else:
                mixer.music.stop()
                print('Music Stopped')

        if data == b'pause\r\n':
            j += 1
            if j%2 != 0:
                mixer.music.pause()
                print('SONG PAUSED')
            else:
                mixer.music.unpause()
                print('SONG RESUMED')

        if data == b'replay\r\n':
            mixer.music.rewind()
            print("Restarting the song")

if __name__ == '__main__':
    path = input("Enter the path of music:") # taking path as input
    start(path) # calling start function with path as argument
