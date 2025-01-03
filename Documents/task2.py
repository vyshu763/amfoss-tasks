import pytesseract
from PIL import Image
import re

# to get image from device
image_path = "/home/vyshnavi/Documents/2+2.png"
#open the image
img = Image.open(image_path)
#open the image 
#using Tesseract OCR to extract the text
extracted_text = pytesseract.image_to_string(img).strip()


# Print the extracted text
print(f"Extracted Text: '{extracted_text}'")

try:
   #using try condition 
    match = re.search(r'\d+\s*[\+\-\/]\s*\d+', extracted_text)
# using regrex to match the extracted text with our given pattern 
# our pattern is \d+ = one or more digits and \s* is 0 or more white space characters 
# [\+\-\/] indicates any one in the baracet that is +,-,,/
    if match:
        expression = match.group()
        # match.group() returns the matched expression to a string 
        
        result = eval(expression)
        # Evaluate the expression
        print(f"The expression is: {expression}")
        print(f"The result is: {result}")
    else:
        print("No valid arithmetic expression found.")
except Exception as e:
    print(f"Error: {e}")
    # e is a variable that holds information of the error
