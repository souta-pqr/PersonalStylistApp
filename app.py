from flask import Flask, render_template, request, jsonify
from models import StyleClassifier
from utils import preprocess_image, draw_bounding_boxes, create_overlay_image
from image_recognition import ClothingItemDetector
from style_recommendation import get_personalized_recommendation, adjust_recommendation_for_season_and_occasion
from user_profile import UserProfile
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = StyleClassifier()
detector = ClothingItemDetector()

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# アップロードフォルダが存在しない場合は作成
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        image = preprocess_image(filepath)
        style = model.predict(image)
        detections = detector.detect_items(image)
        
        # 検出結果を画像に描画
        image_with_boxes = draw_bounding_boxes(image, detections)
        result_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
        image_with_boxes.save(result_image_path)

        # オーバーレイ画像の作成
        overlay_image = create_overlay_image(image, detections)
        overlay_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'overlay_' + filename)
        overlay_image.save(overlay_image_path)
        
        season = request.form.get('season', 'spring')
        occasion = request.form.get('occasion', 'casual')
        
        # ユーザープロファイルの作成（実際のアプリケーションではユーザー入力から取得）
        user_profile = UserProfile(age=30, gender='female', body_type='average', preferences=['casual', 'comfortable'])
        
        recommendation = get_personalized_recommendation(style, [d['label'] for d in detections], user_profile)
        recommendation = adjust_recommendation_for_season_and_occasion(recommendation, season, occasion)
        
        return jsonify({
            'style': style,
            'recommendation': recommendation,
            'detected_items': [d['label'] for d in detections],
            'original_image': filepath,
            'result_image': result_image_path,
            'overlay_image': overlay_image_path
        })

if __name__ == '__main__':
    app.run(debug=True)