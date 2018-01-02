# Dolomite
In this project we use background subtraction and contour detection to find the largest object in the foreground

The image of the largest object is saved for every second of the video. The image is saved as text file. Finally, the data is outputed as a json file.

# Background Subtraction
This program reads a video file(25fps), then for every second we apply background subtraction, and for every frame in the video after background subtraction, we apply the following process. First, we do thresholding to make foreground objects white in colour and the background black. Then, we do countour detection to find the areas that are white in colour. Then, we find the island with the largest area and output it as an image

The image is then converted to text format and saved with a timestamp in an object array. Finally, the data is dumped in a JSON format.

# Reader
This program reads the file in JSON format and converts the data from text back into image.
