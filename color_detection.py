import cv2
import numpy as np
import pandas as pd
import argparse
import os

# Function to calculate minimum distance from all colors and get the most matching color name
def getColorName(R, G, B, color_data):
    minimum_distance = 10000
    color_name = ""
    for index, row in color_data.iterrows():
        d = abs(R - row['R']) + abs(G - row['G']) + abs(B - row['B'])
        if d < minimum_distance:
            minimum_distance = d
            color_name = row['color_name']
    return color_name

# Function to handle mouse double click event
def draw_function(event, x, y, flags, param):
    global b, g, r
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b, g, r = img[y, x]

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i/--image', required=True, help="Path to input image")
args = vars(ap.parse_args())

# Read image path from command line argument
img_path = args['C:\Python312\ColorDetetction\colorpic.jpg ']

# Check if the image file exists
if not os.path.isfile(img_path):
    print(f"Error: Image file not found at '{img_path}'")
    exit(1)

# Read the image using OpenCV
img = cv2.imread(img_path)

# Check if the image is loaded successfully
if img is None:
    print(f"Error: Unable to load image from '{img_path}'")
    exit(1)

# Load color data from CSV file
csv_path = os.path.join(os.path.dirname(__file__), 'colors.csv')
color_data = pd.read_csv(csv_path)

# Create a named window for displaying the image
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# Main loop to display the image and detect colors on double click
while True:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'esc' to exit
        break
    elif key == ord('c'):  # Press 'c' to print color information
        if 'r' in globals() and 'g' in globals() and 'b' in globals():
            color_name = getColorName(r, g, b, color_data)
            print(f"Detected Color: {color_name} (R={r}, G={g}, B={b})")
        else:
            print("Error: Click on the image to select a color.")

# Close all OpenCV windows
cv2.destroyAllWindows()
