import cv2
import numpy as np

def cam():
    # Initialize the camera or video feed
    cap = cv2.VideoCapture(0)  # You can replace 0 with the camera index if you have multiple cameras

    # Define the lower and upper range of the yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    # Dictionary to store cube names based on hash values
    cube_names = {}

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        
        if not ret:
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the yellow color range
        yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

        # Apply morphological operations to clean up the mask
        kernel = np.ones((5, 5), np.uint8)
        yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
        yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)

        # Find contours in the mask
        contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Update detected cube names based on positions
        new_cube_names = {}

        for contour in contours:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)
            
            # Filter out small contours
            if area > 500:
                # Calculate the moments of the contour to find the centroid
                moments = cv2.moments(contour)
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])
                
                # Generate a unique hash value for the cube's position
                cube_position_hash = hash((cx, cy))
                
                # If the cube is already in cube_names, retain the existing name
                if cube_position_hash in cube_names:
                    cube_name = cube_names[cube_position_hash]
                else:
                    cube_name = len(new_cube_names) + 1

                new_cube_names[cube_position_hash] = cube_name
                
                # Draw a marker around the detected cube and label it

                # cv2.putText(frame, cube_name, (cx - 20, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Calculate the orientation of the cube
                # You'll need to implement this part based on your cube's geometry
                cube_orientation = 0.0  # Replace with the actual orientation value
                
                #mapping the position to the grid:
                cx=float(cx/320)
                cy=float(cy/240)
                
                # Print the cube's information
                # return (cube_name, (cx, cy), cube_orientation)
                return (cx,cy)
                # return(cube_name, "Orientation:", cube_orientation)

        # Update the cube names dictionary
        cube_names = new_cube_names

        # Display the frame with markers
        cv2.imshow("Cube Detection", frame)

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
