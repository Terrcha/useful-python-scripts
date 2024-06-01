from PIL import Image

def convert_webp_to_png(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            if img.mode == 'CMYK':
                img = img.convert('RGB')

                img.save(output_file, 'PNG')

            print(f"Image saved as {output_file}")

        except IOError:
            print(f"Unable to open {input_file}")
