{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, render_template\
from get_color_codes import get_color_codes\
\
app = Flask(__name__)\
\
@app.route("/", methods=["GET", "POST"])\
def upload_file():\
    if request.method == "POST":\
        # Check if a file was uploaded\
        if "file" not in request.files:\
            return "No file uploaded"\
        \
        file = request.files["file"]\
        \
        # Check if the file is an SVG\
        if file.filename.split(".")[-1].lower() != "svg":\
            return "File must be an SVG"\
        \
        # Get the color codes from the SVG file\
        color_codes = get_color_codes(file)\
        \
        # Render the color codes in an HTML table\
        return render_template("color_codes.html", color_codes=color_codes)\
    \
    # Render the file upload form\
    return render_template("upload_file.html")\
\
if __name__ == "__main__":\
    app.run(debug=True)\
}