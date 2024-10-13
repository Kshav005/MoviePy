# In this chapter, we are going to look at some nice features of this module.
# Let's create our basic template.

from moviepy.editor import *

vid = VideoFileClip("videos/abc.mp4")

# To rotate your video, 'rotate(degrees)'
vid = vid.rotate(90)        # Rotating it to 90 degrees

# To change volume of the video, we use 'volumex(float)', where float is a float number. 1 is default volume.
vid = vid.volumex(0.5)      # Reducing the volume to half

# To show the clip in python itself, i.e. without saving it, 'ipython_display(width=int)' but it only works in Jupyter notebook type apps.
vid.ipython_display(width=300)