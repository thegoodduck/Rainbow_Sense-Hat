import main

# Define the shape as a star
shape = [
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the pixel order to create a star pattern
pixel_order = [
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),  # Center column
    (2, 2), (1, 1), (0, 0),  # Top-left branch
    (2, 5), (1, 6), (0, 7),  # Bottom-left branch
    (4, 5), (5, 6), (6, 7),  # Bottom-right branch
    (4, 2), (5, 1), (6, 0)   # Top-right branch
]

while True:
    main.main(shape, pixel_order)