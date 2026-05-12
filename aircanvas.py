import cv2
import numpy as np
import mediapipe as mp

# Use the direct path to solutions to bypass the AttributeError
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_draw

# Initialize Hand Tracking correctly
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Canvas setup
canvas = None
prev_x, prev_y = 0, 0
draw_color = (0, 0, 255) # Red color for writing
eraser_thickness = 50
brush_thickness = 5

cap = cv2.VideoCapture(0)
# ... (the rest of your while loop remains the same)