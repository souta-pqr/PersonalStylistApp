from flask import Flask, render_template, request, jsonify
from models import StyleClassifier
from utils import preprocess_image, get_style_recommendation
import os

app = Flask(__name__)
model = StyleClassifier()

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        image = preprocess_image(filename)
        style = model.predict(image)
        recommendation = get_style_recommendation(style)
        
        return jsonify({
            'style': style,
            'recommendation': recommendation,
            'image_path': filename
        })

if __name__ == '__main__':
    app.run(debug=True)