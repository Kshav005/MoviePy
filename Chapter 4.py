# In this chapter, we will learn about merging videos using another way and this one includes starting another video when first video ends.
from moviepy.editor import *
vid1 = VideoFileClip("videos/test3.mp4")
vid2 = VideoFileClip("videos/abc.mp4").subclip(5, 10)

# Setting a position for video 2
vid2.set_position((50, 150))

total = concatenate_videoclips([vid1, vid2])
# total.write_videofile("videos/test4.mp4")

# Now learning about adding margin to the video (resizing without changing aspect ratio)
vid1 = vid1.margin(100)
# vid1.write_videofile("videos/test5.mp4")

# Saving a frame image from the video 
vid2.save_frame("videos/test_image.jpg", t=14)         # 't' represents the time in seconds

# With this, the tutorial ends and now you can look at the documentation to learn about more stuff related to this library.