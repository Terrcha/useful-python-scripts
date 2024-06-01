from PIL import Image

def convert_webp_to_jpg(input_file, output_file):
    im = Image.open(input_file).convert("RGB")
    im.save(output_file, "jpeg")