import main
import time
shape = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the pixel order to go around the shape
pixel_order = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Top row
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),  # Right column
    (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7),  # Bottom row
    (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1)   # Left column
]
while True:
    main.main(shape, pixel_order)