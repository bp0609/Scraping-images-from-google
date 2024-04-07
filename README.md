# automatic-Google-images-downloader
This file helps to download images in large amounts from google using python. 

The code takes two inputs
- The name of the image that you want to download. Eg: `dog`
- The number of images you want to download.

The images will be downloaded in a self created folder. This method of downloading the images using python is better than brut forcely downloading them from google which would take lots of time. Such methods are used mostly in creating datasets for training Machine Learning models. 


NOTE: Since google updates its code frequently you might need to check some things in the code to make it work correctly
- Check the `class name` given to the img element from the html code by printing the html text and then update it accordingly.
- To check the class, print `soup` in the download images function and find the `class name` given to img element.
- Update the latest class name in
  ` results = soup.findAll('img', {'class': 'class_name'}) `
