# Welcome to another module tutorial in which we are going to learn about MOVIEPY, which is the best module for video editing automation. Let's begin with our tutorial!
# You need to type 'pip install moviepy' to use this module inside our program.
# We already have a demo mp4 file inside the 'video' folder. We will experiment with what we can do.

# Importing moviepy module
from moviepy.editor import *

# Loading our video inside a function
vid = VideoFileClip("videos/abc.mp4")

# If you want to trim a video, we use the function 'subclip'. This function takes two arguments - First is the starting timer and second is the ending timer (in seconds).
vid = vid.subclip(15, 20)       # Making it a 5 second clip

# Now let's save our file into a gif!
vid.write_gif("videos/a1.gif")

# You will need to wait few minutes in order to get the work done.