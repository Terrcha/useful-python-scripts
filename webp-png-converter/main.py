from webp_png_converter import convert_webp_to_jpg
from tkinter.filedialog import askopenfilename, asksaveasfile

input_file = askopenfilename()
output_file = asksaveasfile()

convert_webp_to_jpg(input_file,output_file)