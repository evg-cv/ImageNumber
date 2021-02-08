# ImageOCR

## Overview

This project is to extract the necessary information in the image and save the image in the new path. In this project, Google Vision API is used to get the OCR result. 

## Structure

- src
    
    * The source code to receive the OCR result and process it to extract the necessary information

- utils

    * credential: The key for Google Vision API    
    * The source code to manage folder and file functionality    

- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    Several settings including the path

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
