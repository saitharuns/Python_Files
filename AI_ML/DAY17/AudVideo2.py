import cv2
from gtts import gTTS
import os

# Initialize the video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open the camera")
else:
    # Define video writer codec and output file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('captured_Video.mp4', fourcc, 30.0, (640, 480))

    # Initial text
    displayed_text = 'SAI THARUN S'
    last_announced_text = None  # Keeps track of the last text announced

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Frame not detected.")
            break

        # Check if the text to announce has changed
        if displayed_text != last_announced_text:
            # Generate audio for the text
            tts = gTTS(text=displayed_text, lang='en')
            tts.save("op.mp3")
            os.system("start op.mp3")  # Play the audio
            last_announced_text = displayed_text  # Update the last announced text

        # Display text on the frame
        cv2.putText(frame, text=displayed_text, fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                    org=(50, 430), fontScale=1, color=(0, 255, 255), thickness=2)
        
        # Show the video frame
        cv2.imshow('Video Capture', frame)
        out.write(frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()

cap.release()
cv2.destroyAllWindows()
