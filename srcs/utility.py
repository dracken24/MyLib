from pyray import * # Import for Raylib

"""Recursive function for draw and scroll text inside a box (rectangle)
    Args:
        box (Rectangle): Rectangle for draw text
        text (str): Text to draw
        line_position (int): Position of the line in the box
        scroll_offset (int): Scroll offset for base on mouse wheel
        line_ct (int): Text is cut in x line_ct to fix in box whide
    
    Returns:
        int: Line count
"""
def adjust_text_in_box_and_draw_result(box: Rectangle, text: str, line_position: int = 0,
                                       scroll_offset: int = 0, line_ct: int = 0) -> int:
    # Function for draw in a specific zone. (like writing text inside a box) 
    begin_scissor_mode(int(box.x), int(box.y), int(box.width), int(box.height))
    
    text_width: int = measure_text(text.encode('utf-8'), 20)    # Check if text is more whide than the box
    line_height: int = 22                                       # Space for offset each line in pixel
    writable_length: int = int(box.width - 20)                  # Writable whide space in the box (20 pixels offset)

    adjusted_y = int(box.y + line_position + scroll_offset)     # Adjust each line position in y

    # if the text is to whide for the box
    if text_width > writable_length:
        line = text[:int(writable_length / 10.2)]   # Take a line in the text base on writable_length

        ct: int = 0
        find: bool = False
        for c in line:
            if (c == '\n'):
                line = text[:ct]
                find = True
                break
            ct += 1
        
        if (find == True):
            text = text[ct + 1:]
        else:
            text = text[int(writable_length / 10.2):]   # Erase that line from the text

        draw_text(line, int(box.x + 10), adjusted_y, 20, BLACK) # Draw the line in the box
        line_ct += 1 # Add one to the line counter
        # Call recursive function with the text less the cut line
        line_ct = adjust_text_in_box_and_draw_result(box, text, line_height + line_position, scroll_offset, line_ct)
    # If text fit in the box, just write it
    else:
        draw_text(text, int(box.x + 10), adjusted_y, 20, BLACK)

    # End scissor mode
    end_scissor_mode()

    # Return the number of line
    return line_ct