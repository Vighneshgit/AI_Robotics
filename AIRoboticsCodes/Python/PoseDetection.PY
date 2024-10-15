import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# Initialize MediaPipe Pose Estimation
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Start capturing video (or replace with a path to a video file)
cap = cv2.VideoCapture(0)

# Initialize Pose Estimation model
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False  # Optimize performance

        # Perform pose estimation
        results = pose.process(image_rgb)

        # Convert the image color back to BGR for OpenCV
        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # Draw the pose annotation on the image
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),  # Joints
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)   # Lines
            )

        # Display the resulting frame
        cv2.imshow('Human Pose Estimation', image)

        # Exit the video window with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
