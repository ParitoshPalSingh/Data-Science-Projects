# Data-Science-Projects

1. Fake News Detection
  - Fake news has been there since the dawn of ages. Fake news existed even before the Internet was a thing. However, with the boom of technology, we use the Internet more than anything else. Hence, making sure that the breaking news we are seeing is genuine and not just a hoax to unnecessarily grab attention. Anything fictitious, like articles that are deliberately fabricated to deceive the readers.
  - Social media and news outlets publish fake news to increase readership and catch as many people as possible to increase their profit. Since this is only good for monetary purposes and can cause more harm than good, I have tried to make a Fake News detection model. It can learn from the data we have online and then make decisions based on the historical references and structures to identify if the news is real or fake. Such click-baits lure users and entice curiosity with flashy headlines or designs to click links to increase advertisements revenues.



2. Colour Detection using OpenCV
  - Colour detection is the process of detecting the name of any colour. It is easy to do for us humans, but it isn't straightforward for computers. Talking to many of my friends, I soon realized even though I can precisely guess the colours like red, blue, sapphire; I struggle to distinguish between Dark orchid, burgundy, wine, etc.
  - Hence, I used OpenCV to build this application, where we can identify the colour of any part of the image that is clicked on. There can be 256x256x256 = ~16 million+ different ways to represent colour. So rather than predicting all 16 million colours, I have created the model to give the closest colour to the RGB values of the clicked area. The dataset used is the colors.csv file, consisting of more than 860 colour names and their RGB values and hex values.
