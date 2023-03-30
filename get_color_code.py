{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from PIL import Image\
from collections import defaultdict\
\
\
def get_color_codes(filename):\
    # Open the image\
    image = Image.open(filename)\
\
    # Convert the image to RGB mode\
    rgb_image = image.convert('RGB')\
\
    # Get the colors in the image\
    colors = defaultdict(list)\
    for x in range(image.width):\
        for y in range(image.height):\
            r, g, b = rgb_image.getpixel((x, y))\
            hex_code = '#\{:02x\}\{:02x\}\{:02x\}'.format(r, g, b)\
            cmyk_code = rgb_to_cmyk(r, g, b)\
            pantone_code = hex_to_pantone(hex_code)\
            colors['Hex'].append(\{'type': 'hex', 'value': hex_code\})\
            colors['RGB'].append(\{'type': 'rgb', 'value': f'rgb(\{r\}, \{g\}, \{b\})'\})\
            colors['CMYK'].append(\{'type': 'cmyk', 'value': cmyk_code\})\
            if pantone_code:\
                colors['Pantone'][pantone_code] += 1\
\
    return colors\
\
\
def rgb_to_cmyk(r, g, b):\
    # Convert RGB to CMYK\
    r = r / 255.0\
    g = g / 255.0\
    b = b / 255.0\
    k = 1 - max(r, g, b)\
    if k == 1:\
        c = 0\
        m = 0\
        y = 0\
    else:\
        c = (1 - r - k) / (1 - k)\
        m = (1 - g - k) / (1 - k)\
        y = (1 - b - k) / (1 - k)\
    cmyk = '\{:.2f\},\{:.2f\},\{:.2f\},\{:.2f\}'.format(c, m, y, k)\
    return cmyk\
\
\
def hex_to_pantone(hex_code):\
    # Convert HEX to Pantone\
    # This function should be replaced with your own implementation\
    # of a Pantone color lookup based on the HEX code.\
    # For the purposes of this example, it just returns None.\
    return None\
}