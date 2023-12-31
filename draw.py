import cv2

def draw(output_path: str, img_path: str, bound_list: list):
    """Handle all drawing operations for a given image based on a list of coordinates."""

    image = cv2.imread(img_path)

    for bounds in bound_list:
        image = draw_rectangle(image, bounds)

    # Output to new image file
    cv2.imwrite(output_path, image)

def draw_rectangle(image, bounds: list):
    """Draw a yellow dotted rectangle onto a given image at the specified coordinates."""
    
    x1, y1 = bounds[0], bounds[1]
    x2, y2 = bounds[2], bounds[3]
    color = (64, 231, 241)
    thickness = 6
    line_type = cv2.LINE_8
    dash_length = 10

    # **These two for loops were generated using ChatGPT and modified by me.**
    # Draw horizontal dashes
    for x in range(x1, x2, dash_length * 2):
        image = cv2.line(image, (x, y1), (min(x + dash_length, x2), y1), color, thickness, line_type)
        image = cv2.line(image, (x, y2), (min(x + dash_length, x2), y2), color, thickness, line_type)

    # Draw vertical dashes
    for y in range(y1, y2, dash_length * 2):
        image = cv2.line(image, (x1, y), (x1, min(y + dash_length, y2)), color, thickness, line_type)
        image = cv2.line(image, (x2, y), (x2, min(y + dash_length, y2)), color, thickness, line_type)

    return image