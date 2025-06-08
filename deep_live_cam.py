import cv2
import time

# Initialize camera
cap = cv2.VideoCapture(0)

# Set resolution (optional)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Font for UI text
font = cv2.FONT_HERSHEY_SIMPLEX

# For FPS calculation
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # --- UI Design Elements ---
    
    # Draw outer frame border
    frame = cv2.rectangle(frame, (5, 5), (635, 475), (0, 255, 255), 4)

    # Display "LIVE" in top-left
    cv2.putText(frame, 'LIVE', (20, 40), font, 1, (0, 0, 255), 2)

    # Display FPS in top-right
    cv2.putText(frame, f'FPS: {int(fps)}', (500, 40), font, 0.7, (0, 255, 0), 2)

    # Draw "STOP" button (green rectangle)
    cv2.rectangle(frame, (500, 420), (620, 460), (0, 255, 0), -1)
    cv2.putText(frame, 'STOP (ESC)', (505, 450), font, 0.6, (0, 0, 0), 2)

    # Show the frame
    cv2.imshow(' Deep Live Cam', frame)

    # Press ESC to quit
    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
