Features
Real-Time Detection: Detects faces and eyes live from your webcam feed.
Visualization: Draws rectangles around detected faces and eyes for clear visualization.
Configurable Detection: Allows tuning of the detection sensitivity through the detectMultiScale parameters.

Prerequisites
Before running the script, ensure the following are installed:
Python 3.x
OpenCV library (cv2)
NumPy library (numpy)

How It Works
Face Detection:
Converts the frame to grayscale for better accuracy.
Detects faces using haarcascade_frontalface_default.xml.
Draws rectangles around detected faces.
Eye Detection:
Extracts the face region and detects eyes using haarcascade_eye.xml.
Draws rectangles around detected eyes within the face region.
