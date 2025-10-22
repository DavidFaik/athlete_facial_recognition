# Face Recognition (OpenCV + face_recognition)

Real‑time face recognition from a webcam using OpenCV and the `face_recognition` library (dlib). Known faces are encoded from images in an `images/` folder and matched on the fly. Optionally, overlay extra info (e.g., Age/Goals/Assists) from an Excel sheet.

## Features
- Live face detection and recognition from a webcam
- Labels known faces using the image filename (e.g., `Elon Musk.jpg` → "Elon Musk")
- Draws bounding boxes and names on the video stream
- Optional data overlay from `Stats.xlsx` via `webCam.py`
- Utility script to compare two images (`image_comparison.py`)

## Project Structure
```
.
├─ images/                           # Known faces (used by root-level scripts)
├─ image_comparison.py               # Compare two images
├─ main_video.py                     # Live recognition
├─ simple_facerec.py                 # Face encoding + matching helper
├─ faceRec.py                        # Simple two-image compare example
├─ webCam.py                         # Live recognition + Excel overlay
└─ Stats.xlsx                        # Example metadata for overlay
```

## Requirements
- Python 3.8+ (tested with CPython)
- pip packages:
  - `opencv-python`
  - `face_recognition` (depends on `dlib`)
  - `numpy`
  - `pandas` and `openpyxl` (only for `webCam.py` Excel overlay)

On Windows, installing `face_recognition/dlib` may require:
- CMake and Visual C++ Build Tools
- Alternatively, use a Python distribution with compatible prebuilt wheels (e.g., conda).

## Setup
```bash
# 1) Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install opencv-python face_recognition numpy
# Only if you plan to use the Excel overlay:
pip install pandas openpyxl
```
If you hit errors installing `face_recognition`/`dlib`, install CMake first and try again, or consider using conda:
```bash
# Example with conda
conda create -n facerec python=3.10 -y
conda activate facerec
conda install -c conda-forge dlib face_recognition opencv numpy pandas openpyxl -y
```

## Usage
1) Add known faces:
- Place one or more clear, front-facing photos per person into an `images/` folder.
- The filename (without extension) becomes the displayed name (e.g., `Ryan Reynolds.jpg` → "Ryan Reynolds").
- Keep `images/` next to the script you are running (root-level or `source code/`).

2) Run live recognition (choose one location and run from that folder):
```bash
From repository root (uses ./images/ and ./simple_facerec.py)
python main_video.py
```
- Press `Esc` to quit the video window.
- If the wrong camera opens, change the index in `cv2.VideoCapture(<index>)` inside `main_video.py`.

3) Compare two images:
```bash
# Edit paths in image_comparison.py as needed
python image_comparison.py
```

4) Optional: Excel overlay (player stats) with `webCam.py`:
- Ensure `Stats.xlsx` has at least these columns: `Name`, `Age`, `Goals`, `Assists`.
- File names in `images/` should match the `Name` values (e.g., `Messi.webp` → Name: `Messi`).
- Install extras: `pip install pandas openpyxl`
- Run:
```bash
python webCam.py
```

## Configuration Tips
- Frame resizing for speed: `SimpleFacerec.frame_resizing` (default `0.25`) controls the scale used during detection. Larger values (e.g., `0.5`) can improve accuracy but reduce FPS.
- Camera index: Update `cv2.VideoCapture(0)` or `cv2.VideoCapture(2)` depending on your device.
- Image formats: Common formats like `.jpg`, `.png`, `.webp` are fine.

## Troubleshooting
- dlib/face_recognition install issues (Windows):
  - Install CMake and Visual C++ Build Tools, or use conda packages.
  - Ensure your Python version is compatible with available wheels.
- No faces recognized or labeled as "Unknown":
  - Use clear, front-facing training photos with good lighting.
  - Provide multiple images per person if recognition is inconsistent.
  - Verify the `images/` folder path matches where you run the script.
- Camera not opening:
  - Try changing the index (0/1/2/...). Ensure other apps aren’t using the camera.

## How It Works (High Level)
1) On startup, `SimpleFacerec.load_encoding_images("images/")` encodes all faces found in the `images/` folder and stores their encodings with the corresponding names (from filenames).
2) Each frame from the webcam is resized and converted to RGB.
3) `face_recognition` locates faces and computes encodings for detected faces.
4) Encodings are compared with known encodings; the closest match (below a tolerance) determines the label.
5) OpenCV draws bounding boxes and labels on the video stream.

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [face_recognition (dlib)](https://github.com/ageitgey/face_recognition)
