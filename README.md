# Virtual Background Camera

## Overview

**Virtual Background Camera** is a Python-based real-time webcam enhancer that applies live background **blurring** or **image replacement** using MediaPipe's selfie segmentation. It can also stream the processed output to a **virtual webcam** using `pyvirtualcam`, making it compatible with Zoom, OBS, Discord, and more.

The application is lightweight, easy to configure, and customizable via command-line arguments.

---

## Features

- **Background Segmentation**: Uses MediaPipe to detect and segment people in real-time.
- **Background Blur**: Apply a smooth Gaussian blur behind the subject.
- **Background Replacement**: Replace your background with a static image (e.g., virtual office, anime background, etc.).
- **Virtual Camera Output**: Send the processed video stream to a virtual webcam.
- **Customizable Settings**: Choose camera source, image path, and effect mode via CLI.

---

# Why Pay for Premium Features?

Why pay for expensive subscriptions when you can run a simple script and get the same results for free? With just a few lines of code, you can enhance your webcam with features like background replacement and blurring — all without needing to potentially pay for premium services.

It's simple, customizable, and works with apps like Zoom, OBS, or Discord (surprising to think custom webcam backgrounds aren't free on platforms like Discord)

## Requirements

To run the application, the following Python packages are required:

- `opencv-python` (video capture and display)
- `mediapipe` (for real-time person segmentation)
- `numpy` (array manipulation)
- `pyvirtualcam` (virtual camera output)

You can install the necessary packages using pip:

```bash
pip install -r requirements.txt

```

## Setup

### 1. Clone or Download the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/virtual-background-camera.git
cd virtual-background-camera
```

### 2. Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Prepare Background Image (Optional)

If you want to use a custom background image, place your image (e.g., `sample.jpg`) in the project directory or specify the full path when running the script.

A default image (`images/default.jpg`) is provided as a fallback.

---

## Run the Application

Launch the webcam effect application using:

```bash
python camera.py
```

---

## Command-Line Arguments

You can customize the behavior of the application using the following arguments:

`--replace-bg`, `-r` : Replace background with image (if not set, blur is used)
`--bg-image`, `-i` : Path to the background image file
`--source`, `-s` : Webcam index (default: 0 for built-in webcam)

### Example:

```bash
python camera.py -r -i sample.jpg -s 0
```

This will use the primary webcam (index 0), replace the background with `sample.jpg`, and stream the output to both a preview window and virtual webcam.

---

## Output & Usage

- A window will open showing the live webcam with the applied effect.
- A virtual webcam named `OBS Virtual Camera` or `pyvirtualcam` will also stream the same output.
- You can select this virtual cam in apps like Zoom, OBS, Teams, etc.

---

## Exit the Application

Press the **`q` key** while the video window is active to close the application.

---

## Project Structure

```
.
├── camera.py               # Main script to launch the app
├── BackgroundEffect.py     # Core class implementing the effects
├── images/
│   └── default.jpg         # Default background image
├── .gitignore
├── requirements.txt
└── README.md
```

---
