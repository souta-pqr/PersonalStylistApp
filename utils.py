from PIL import Image, ImageDraw, ImageFont

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    return image

def draw_bounding_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    for detection in detections:
        box = detection['box']
        label = detection['label']
        confidence = detection['confidence']

        draw.rectangle(box, outline="red", width=3)
        draw.text((box[0], box[1] - 20), f"{label}: {confidence:.2f}", font=font, fill="red")

    return image

def create_overlay_image(original_image, detections):
    overlay = original_image.copy()
    draw = ImageDraw.Draw(overlay)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    for detection in detections:
        box = detection['box']
        label = detection['label']
        draw.text((box[0], box[1]), label, font=font, fill="blue")

    return Image.blend(original_image, overlay, 0.5)