# License Plate and Helmet Detection

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Introduction
This project leverages YOLOv8 to address two crucial functionalities: detecting whether a bike rider is wearing a helmet and identifying license plates for riders not adhering to safety regulations. Upon detecting a rider without a helmet, the system captures their license plate and saves this information to a CSV file. The project also generates a fine or ticket for each identified license plate. This functionality is particularly useful for surveillance cameras deployed on freeways or highways, where monitoring helmet compliance is essential for enhancing road safety.
# License Plate and Helmet Detection

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Introduction
This project leverages YOLOv8 to address two crucial functionalities: detecting whether a bike rider is wearing a helmet and identifying license plates for riders not adhering to safety regulations. Upon detecting a rider without a helmet, the system captures their license plate and saves this information to a CSV file. The project also generates a fine or ticket for each identified license plate. This functionality is particularly useful for surveillance cameras deployed on freeways or highways, where monitoring helmet compliance is essential for enhancing road safety.

## Requirements
To set up the project, you will need the following software installed on your machine:

- **Python 3.8 or higher**
- **Virtual Environment Management** (e.g., `venv` or `conda`)
- **Required Python Libraries**:
  - cv2
  - cvzone
  - ultralytics
  - opencv-python
  - pytesseract
  - pandas
  - Pillow
  - matplotlib
  - YOLOv8 dependencies (as specified in YOLOv8 documentation)
    
You can train your model in Google Colab, make sure to use the GPU.
You can install the required libraries using the `requirements.txt` file provided in this repository.


## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/SyedAtta11200/License-Plate-Detection.git
```

### Step 2: Create a Virtual Environment

```bash
python -m venv yolov8-env
source yolov8-env/bin/activate  # On Windows use: yolov8-env\Scripts\activate
```
Using conda:
If you prefer conda, create a new environment with the following command:

```bash
conda create --name yolov8-env python=3.12
conda activate yolov8-env
```
### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Download YOLOv10 Weights

Download the YOLOv8 weights if not already included in the repository. You can find them in the YOLOv8 GitHub repo or their official site.

### Step 5: Data Preparation

Ensure your dataset is prepared according to the YOLOv8 data format. You will need images and corresponding annotation files in the YOLO format.

### Step 6: Training the ModelStep 6: Training the Model

To train the YOLOv8 model, run the following command: Also insure the path for train and valid imiges in the data.yaml file
```bash
!yolo task=detect mode=train epochs=100 batch=16 plots=True model=weights/yolov8n.pt data=data.yaml
```

### Step 7: Running the Detection

After training, you can use the model to run detections on your images or video streams. Follow the instructions in the script comments for more details.

## Usage

To run the helmet detection, execute the script helmet_detection.py. This script assesses if a rider is wearing a helmet; if they are not, it triggers the license plate detection process.

To perform license plate detection, use the script license_plate_detection.py. The detected license plates are stored in a Pandas DataFrame, which can be saved as a CSV file for further analysis or record-keeping.

## Acknowledgments

YOLOv8 for the original model and implementation.
OpenCV for image processing capabilities.

```bash
This version maintains a smooth flow in the setup instructions and makes it easy for users to follow along. Feel free to adjust any sections as needed!
```
