import cv2

def draw(img_path: str, bound_list: list):
    """Handle all drawing operations for a given image based on a list of coordinates."""

    image = cv2.imread(img_path)

    for bounds in bound_list:
        image = draw_rectangle(image, bounds)

    # Output to new image file
    cv2.imwrite("test.png", image)

def draw_rectangle(image, bounds: list):
    """Draw a yellow dotted rectangle onto a given image at the specified coordinates."""
    
    start_point = (bounds[0], bounds[1])
    end_point = (bounds[2], bounds[3])
    color = (64, 231, 241)
    thickness = 3

    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    return image