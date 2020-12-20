# ImageNumber

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
    * The source code to manage folder and file functionality
    * The source code to adjust the tilted image    

- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    Various options

## Installation

- Environment

    Windows 10, Ubuntu 18.04, Python 3.6+

- Dependency Installation
    
    Please run the following command in this project directory in the terminal.
    
    ```
        pip3 install -r requirements.txt
    ```

## Execution

- Please run the following command in this project directory in the terminal.

    ```
        python3 app.py
    ```
