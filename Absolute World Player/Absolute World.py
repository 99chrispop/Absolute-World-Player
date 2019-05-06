"""
This code creates a GUI that lets the user play through my latest album, Absolute World.

Author: Christopher Pop
"""

from Tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import glob

# Global variables
clicks = 0
albumIndex = 0

# Selects which songs are played based on the user's interactions with the program
def songSelection(prevFlag, nextFlag, root):
    albumSongs = glob.glob("*.wav")
    albumSongs.sort()

    global albumIndex

    if(nextFlag == True and albumIndex == 5):
        albumIndex = 0
        playPauseSongs(prevFlag, albumSongs[albumIndex], nextFlag, root)

        return albumIndex

    elif(nextFlag == True):
        albumIndex += 1
        playPauseSongs(prevFlag, albumSongs[albumIndex], nextFlag, root)

        return albumIndex

    if(prevFlag == True and albumIndex == 0):
        albumIndex = len(albumSongs) - 1
        playPauseSongs(prevFlag, albumSongs[albumIndex], nextFlag, root)

        return albumIndex

    elif(prevFlag == True and albumIndex > 0):
        albumIndex -= 1
        playPauseSongs(prevFlag, albumSongs[albumIndex], nextFlag, root)

        return albumIndex

    playPauseSongs(prevFlag, albumSongs[albumIndex], nextFlag, root)

# Plays/pauses the current song
def playPauseSongs(prevFlag, songName, nextFlag, root):
    global clicks
    clicks += 1 

    song = mixer.Sound(songName)

    if(prevFlag == True or nextFlag == True):
        mixer.stop()
        clicks = 1
        song.play()

        return clicks

    if(clicks > 1):
        if(clicks % 2 == 0):
            mixer.pause()

            return clicks

        mixer.unpause()

        return clicks

    song.play()

# Main function
# Responsible for creating the GUI
def main():
    root = Tk()
    root.title("Absolute World EP")
    root.minsize(250, 250)
    root.resizable(False, False)

    img = ImageTk.PhotoImage(Image.open("Absolute World Art.jpg"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    mixer.init(44100, -16, 2, 2048)

    playPause = Button(root, text = "Play/Pause", command = lambda : songSelection(False, False, root))
    playPause.pack()
    
    prevSong = Button(root, text = "Previous", command = lambda : songSelection(True, False, root))
    prevSong.pack(side = LEFT)

    nextSong = Button(root, text = "Next", command = lambda : songSelection(False, True, root))
    nextSong.pack(side = RIGHT)

    root.mainloop()

main()