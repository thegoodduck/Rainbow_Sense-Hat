from sense_hat import SenseHat
from time import sleep
import time
sense = SenseHat()

# Define the colors for the rainbow
colors = [
    (255, 0, 0),    # Red
    (255, 32, 0),   # Orange-Red
    (255, 64, 0),   # Dark Orange
    (255, 96, 0),   # Orange
    (255, 128, 0),  # Orange
    (255, 160, 0),  # Orange
    (255, 192, 0),  # Orange
    (255, 224, 0),  # Yellow-Orange
    (255, 255, 0),  # Yellow
    (224, 255, 0),  # Yellow-Green
    (192, 255, 0),  # Green-Yellow
    (160, 255, 0),  # Green-Yellow
    (128, 255, 0),  # Green-Yellow
    (96, 255, 0),   # Green
    (64, 255, 0),   # Green
    (32, 255, 0),   # Green
    (0, 255, 0),    # Green
    (0, 255, 32),   # Green-Blue
    (0, 255, 64),   # Blue-Green
    (0, 255, 96),   # Blue-Green
    (0, 255, 128),  # Cyan
    (0, 255, 160),  # Cyan
    (0, 255, 192),  # Cyan
    (0, 224, 255),  # Sky Blue
    (0, 192, 255),  # Sky Blue
    (0, 160, 255),  # Blue
    (0, 128, 255),  # Blue
    (0, 96, 255),   # Navy Blue
    (0, 64, 255),   # Navy Blue
    (0, 32, 255),   # Navy Blue
    (0, 0, 255),    # Blue
    (32, 0, 255),   # Indigo
    (64, 0, 255),   # Indigo
    (96, 0, 255),   # Purple
    (128, 0, 255),  # Purple
    (160, 0, 255),  # Violet
    (192, 0, 255),  # Violet
    (224, 0, 255),  # Magenta
    (255, 0, 224),  # Red-Violet
    (255, 0, 192),  # Red-Violet
    (255, 0, 160),  # Red-Violet
    (255, 0, 128),  # Red-Violet
    (255, 0, 96),   # Red-Violet
    (255, 0, 64),   # Red-Violet
    (255, 0, 32)    # Red-Violet
]


# Function to draw the snake on the Sense HAT
def draw_snake(x, y, color_index):
    sense.set_pixel(x, y, colors[color_index])

# Function to clear the Sense HAT display
def clear_display():
    sense.clear()

# Main loop
def main(shape, pixel_order):
    # Clear the display
    clear_display()

    # Iterate through the pixel order list and the color list
    color_index = 0
    active_pixels = []  # List to store active pixels and their color indices

    for x, y in pixel_order:
        if shape[y][x] == 1:
            draw_snake(x, y, color_index)
            active_pixels.append((x, y, color_index))  # Add the pixel and its color index
            color_index = (color_index + 1) % len(colors)
            sleep(0.1)  # Adjust the speed of the snake

    while True:
        # Update the active pixels with the next color in the sequence
        for i, (x, y, color_index) in enumerate(active_pixels):
            new_color_index = (color_index + 1) % len(colors)
            draw_snake(x, y, new_color_index)
            active_pixels[i] = (x, y, new_color_index)  # Update the color index

        sleep(0.1)  # Small delay to reduce CPU usage
