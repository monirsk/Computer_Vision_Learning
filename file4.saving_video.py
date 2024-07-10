import cv2

# Open the default webcam (usually the first one)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    # If the frame was not read successfully, break the loop
    if not ret:
        print("End of video or error reading frame.")
        break
    
    # Write the frame to the output file
    output.write(frame)
    
    # Display the frame
    cv2.imshow("frame", frame)
    
    # Check if 'q' key is pressed to exit
    if cv2.waitKey(25) == ord('q'):
        break

# Release the video capture and writer objects, and close all OpenCV windows
cap.release()
output.release()
cv2.destroyAllWindows()
