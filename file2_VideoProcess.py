import cv2

# Open the video file
cap = cv2.VideoCapture("F:\\2024\\CV\\DenoVid.mp4")

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # If the frame was not read successfully, break the loop
    if not ret:
        print("End of video or error reading frame.")
        break
    
    # Resize the frame
    frame = cv2.resize(frame, (700, 400))
    
    # Display the frame
    cv2.imshow("frame", frame)
    
    # speed of video 
    if cv2.waitKey(25) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
