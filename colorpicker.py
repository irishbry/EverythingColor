{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import svglib\
from reportlab.graphics import renderPM\
import io\
import re\
from collections import defaultdict\
\
def get_color_codes(svg_file):\
    # Load the SVG file\
    svg_doc = svglib.svg2rlg(svg_file)\
    \
    # Convert the SVG file to a PNG image\
    img_data = io.BytesIO()\
    renderPM.drawToFile(svg_doc, img_data, fmt="PNG")\
    \
    # Get the color information from the PNG image\
    img_data.seek(0)\
    hex_codes = re.findall(rb"#\\w\{6\}", img_data.getvalue())\
    rgb_codes = [tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5)) for hex_code in hex_codes]\
    cmyk_codes = [tuple(map(lambda x: round(x/255, 2), (255-rgb_code[0], 255-rgb_code[1], 255-rgb_code[2], 0))) for rgb_code in rgb_codes]\
    \
    # Get the Pantone color information from the SVG file\
    pantone_codes = re.findall(r"PANTONE\\s+([^\\s]+)", svg_file.read().decode())\
    pantone_dict = defaultdict(int)\
    for pantone_code in pantone_codes:\
        pantone_dict[pantone_code] += 1\
    \
    # Return the color information\
    return \{\
        "Pantone": dict(pantone_dict),\
        "Hex": [hex_code.decode() for hex_code in hex_codes],\
        "RGB": rgb_codes,\
        "CMYK": cmyk_codes\
    \}\
\
# Example usage\
with open("logo.svg", "rb") as f:\
    color_codes = get_color_codes(f)\
    print(color_codes)\
}