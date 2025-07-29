import cv2
import mediapipe as mp
import pyautogui

# Initialize the camera and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get the screen size
screen_w, screen_h = pyautogui.size()

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Flip the frame horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get the result from MediaPipe
    output = face_mesh.process(rgb_frame)

    # Get the frame dimensions
    frame_h, frame_w, _ = frame.shape

    # Check if landmarks are detected and focus only on the left eye's iris
    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark
        left_iris = landmarks[473:478]
        iris_x, iris_y = 0, 0

        # Loop over the landmarks to calculate the average position of the left iris
        for landmark in left_iris:
            iris_x += landmark.x * frame_w
            iris_y += landmark.y * frame_h

        # Calculate the average position
        iris_x /= len(left_iris)
        iris_y /= len(left_iris)

        # Draw a circle on the left iris
        cv2.circle(frame, (int(iris_x), int(iris_y)), 3, (0, 255, 0), -1)

        # Move the mouse cursor using pyautogui
        screen_x = screen_w / frame_w * iris_x
        screen_y = screen_h / frame_h * iris_y
        pyautogui.moveTo(screen_x, screen_y)

    # Display the frame
    cv2.imshow('Eye Controlled Mouse', frame)

    # Break the loop when 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
