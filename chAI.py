import cv2
import sys

try:
    import mediapipe as mp
    print("✅ MediaPipe successfully imported!")
except ImportError:
    print("❌ MediaPipe is NOT installed correctly.")
    sys.exit()

# MediaPipe के टूल्स सेटअप करें
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# कैमरा शुरू करें
cap = cv2.VideoCapture(0)

print("Starting Camera... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Camera not detected.")
        break

    # इमेज को सीधा (Mirror) करें और RGB में बदलें
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # हाथों को डिटेक्ट करें
    results = hands.process(rgb_frame)

    # अगर हाथ मिले, तो उन पर पॉइंट्स ड्रॉ करें
    if results.multi_hand_landmarks:
        print("✋ Hand Detected!") # टर्मिनल में मैसेज आएगा
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Test AI Window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()