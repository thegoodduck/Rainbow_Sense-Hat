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
    (255, 0, 255),  # Magenta
    (255, 0, 192),  # Red-Violet
    (255, 0, 128)   # Red
]

# Define the desired form (in this case, a heart shape)
heart = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]

# Function to draw the snake on the Sense HAT
def draw_snake(x, y, color_index):
    sense.set_pixel(x, y, colors[color_index])

# Function to clear the Sense HAT display
def clear_display():
    sense.clear()

# Main loop
while True:
    # Clear the display
    clear_display()

    # Iterate through the desired form and the color list
    color_index = 0
    for y in range(8):
        for x in range(8):
            if heart[y][x] == 1:
                draw_snake(x, y, color_index)
                color_index = (color_index + 1) % len(colors)
                sleep(0.1)  # Adjust the speed of the snake

    # Pause before repeating the loop
    sleep(1)