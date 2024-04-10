import cv2

def capture_photos(num_photos):
    # Open webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Unable to open webcam.")
        return

    # Iterate to capture photos
    for i in range(num_photos):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Display the captured frame
        cv2.imshow('Captured Photo', frame)

        # Save the captured frame to a file
        file_name = f'captured_photo_{i+1}.jpg'
        cv2.imwrite(file_name, frame)

        # Wait for a key press to capture next photo
        cv2.waitKey(1000)

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    num_photos = 5
    capture_photos(num_photos)
 
