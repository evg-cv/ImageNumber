# OCRLabel

## Overview

This project is to extract the number and name in the image and save the image in the new path, where the name of new path
is matched with name and number in OCR csv file. In this project, Google Vision API is used to get the OCR result. 
Moreover, the images are rotated to make the gray part with number and name vertical while running this project.

## Structure

- input

    The directory that the images to process are contained. It must be made manually.

- src

    * The source code to process csv file
    * The source code to receive the OCR result and process it to extract the necessary information

- utils

    * credential: The authorization key file(.json) used to get the OCR result from Google Vision API
    * OCR.csv: The csv file with various information used to mathe the number and name with the new name
    * The source code to manage folder and file functionality
    * The source code to adjust the tilted image
    * The source code to communicate with Google Vision API

- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    Various options

## Installation

- Environment

    Windows 8+, Ubuntu 16.04+, Python 3.6+

- Dependency Installation
    
    Please run the following command in this project directory in the terminal.
    
    ```
        pip3 install -r requirements.txt
    ```

## Execution

- Please copy the images to process into the input directory

- Please run the following command in this project directory in the terminal.

    ```
        python3 app.py
    ```

## Note

- You can see the process of running this project. After running, you can find out the new directory named output, where
the gif images with new names are saved. 

- Also, because of various reasons including image with an unclear name, etc, some
of them might not be processed successfully. To recognize the unprocessed images easily, the file whose name is processed_files.txt
are created after running. You can easily find out which images have been processed successfully. With this, the result.log
file is also created, where you can know about the reason why some of them haven't been processed.   
