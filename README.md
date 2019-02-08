# Arduino_pushbutton_music_player
# THIS PROJECT IS UNDER PROGRESS......

>AIM : Perform basic fuctions like play/pause/stop/rewind etc to control music using arduino and push buttons

>Libraries used: Pyserial and Pygame(mixer)

>How its working:
  It takes input from push button and print data accordingly on serial monitor. After this, that data on serial monitor is read using         serial library and actions are performed according to Python code.

>How to perform:
  Firstly, open the schematic image given and make the circuit according to it.
  Upload the .ino code on your arduino board.
  Run the python code on your system and control using push buttons.

CURRENT FUNCTIONS IT CAN PERFORM:
1) Start and Stop the music.
2) Pause and unpause the music.
3) Rewind the current song.

FEATURES TO BE ADDED IN FUTURE:
1) Adding playlist/queue support.
2) Controlling volume using potentiometer.
3) Adding LCD to display informations.
4) Skipping a part of song.
5) GUI support.
