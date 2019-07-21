
 >- DOWNLOAD AND CREATE YOUR OWN CUSTOM DATASET USING GOOGLE IMAGES -<

1. Search for the relevant image on google and scrolling until you have found all relevant images to your query. 
From there, we need to grab the URLs for each of these images. 
Switch to the JavaScript console and then copy the JavaScript snippet from download_urls.js and paste into the Console, and you will get "urls.txt".

2. Open command prompt and run this command "python download_images.py --urls urls.txt --output images/wallet", where, "images/wallet" are the folder directories to save images into, which should create before run the command.

3. Enjoy it.

CODE FROM: https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/