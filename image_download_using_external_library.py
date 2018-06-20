# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:27:12 2018

@author: Sandhu
"""
#to download multiple images from google image search , showing how to use an external library
#library taken from pypi.org

from google_images_download import google_images_download
import os
response = google_images_download.googleimagesdownload()
args={"keywords":"tiger","limit":5}			#limit is no.of images being downloaded
absolute_image_paths = response.download(args)
for i in range(0,len(absolute_image_paths[args["keywords"]])):
    os.startfile(absolute_image_paths[args["keywords"]][i])