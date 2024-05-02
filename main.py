from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define the colors for the rainbow
colors = [
    (255, 0, 0),    # Red
    (255, 64, 0),   # Orange-Red
    (255, 128, 0),  # Dark Orange
    (255, 192, 0),  # Orange
    (255, 255, 0),  # Yellow
    (192, 255, 0),  # Yellow-Green
    (128, 255, 0),  # Green-Yellow
    (64, 255, 0),   # Green
    (0, 255, 0),    # Green
    (0, 255, 64),   # Green-Blue
    (0, 255, 128),  # Blue-Green
    (0, 255, 192),  # Cyan
    (0, 255, 255),  # Cyan
    (0, 192, 255),  # Sky Blue
    (0, 128, 255),  # Blue
    (0, 64, 255),   # Navy Blue
    (0, 0, 255),    # Blue
    (64, 0, 255),   # Indigo
    (128, 0, 255),  # Purple
    (192, 0, 255),  # Violet
    (130, 0, 255),  # Magenta
    (160, 0, 255),  # Red-Violet
    (190, 0, 255)   # Red
]

# Define the desired form (in this case, a heart shape)

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
    for x, y in pixel_order:
        if shape[y][x] == 1:
            draw_snake(x, y, color_index)
            color_index = (color_index + 1) % len(colors)
            print(color_index)
            sleep(0.1)  # Adjust the speed of the snake

    # Pause before repeating the loop

    # Pause before repeating the loop