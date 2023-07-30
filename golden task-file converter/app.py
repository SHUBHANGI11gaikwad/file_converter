# app.py
from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_image_to_pdf():
    try:
        image = request.files['image']
        image_data = Image.open(image)
        pdf_buffer = io.BytesIO()

        if image_data.mode != "RGB":
            image_data = image_data.convert("RGB")

        image_data.save(pdf_buffer, format='PDF', save_all=True)

        pdf_buffer.seek(0)
        return send_file(pdf_buffer, attachment_filename='converted_file.pdf', as_attachment=True)

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)