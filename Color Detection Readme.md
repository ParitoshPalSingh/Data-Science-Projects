Colour detection is the process of detecting the name of any colour. It is easy to do for us humans, but it isn't straightforward for computers.

Talking to many of my friends, I soon realized even though I can precisely guess the colours like red, blue, sapphire; I struggle to distinguish between Dark orchid, burgundy, wine, etc.

Hence, I used OpenCV to build this application, where we can identify the colour of any part of the image that is clicked on. There can be 256x256x256 = ~16 million+ different ways to represent colour. So rather than predicting all 16 million colours, I have created the model to give the closest colour to the RGB values of the clicked area. The dataset used is the colors.csv file, consisting of more than 860 colour names and their RGB values and hex values. 

