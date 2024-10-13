from moviepy.editor import *

# Now let's try working with split screen videos!
mainvid = VideoFileClip("videos/abc.mp4")
vid1 = mainvid.subclip(15, 20)
vid2 = mainvid.subclip(0, 5)
vid3 = mainvid.subclip(20, 25)
vid4 = mainvid.subclip(6, 11)

# Now this thing works same as array. You can merge your videos into a form of row and column. Let's try doing it with 4 videos and merge them into 2x2 table.
total = clips_array([[vid1, vid2], [vid3, vid4]])
# total.write_videofile("videos/test1.mp4")         

# It will surely take some time to save the video but don't worry, have some patience!

# Time to learn about extracting and replacing the audio!
# Our videos are ready so we are going to try extracting the audio 
vid4.audio.write_audiofile("videos/test2.mp3")             # Run till this part to extract the audio

# It's done and now let's learn to replace the audio with another, say some music!
# Now there are 2 ways to do so, either turn the original volume to 0 or extract the video without the audio. It is highly recommended to lower the original volume to save time.
vid4 = vid4.volumex(0)

# Now using the audio file 
my_audio = AudioFileClip("videos/guitar.mp3").subclip(0, 5)

# The audio and video duration should be same otherwise the audio would cover the whole video to it's duration or vice versa
vid4 = vid4.set_audio(my_audio)
vid4.write_videofile("videos/test3.mp4")

# And it's done! Congrats. Let's move on to the next chapter and learn few more tricks.

