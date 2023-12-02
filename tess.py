from PIL import Image
import pytesseract
import pyautogui
from io import BytesIO

# Change below to the executable for PyTesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def capture_screen_region(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    return screenshot

def process_image(image):
    return image

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

def main():
    x, y, width, height = 0, 1160, 975, 350 # Change these to the coordinate range of your chat window
    screenshot = capture_screen_region(x, y, width, height)
    processed_image = process_image(screenshot)
    extracted_text = extract_text(processed_image)
    extracted_text = str(extracted_text)
    return extracted_text