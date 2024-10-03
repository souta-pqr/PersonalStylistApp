from flask import Flask, render_template, request, jsonify
from models import StyleClassifier
from utils import preprocess_image
from user_profile import UserProfile
from image_recognition import ClothingItemDetector
from style_recommendation import get_personalized_recommendation, adjust_recommendation_for_season_and_occasion
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
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            image = preprocess_image(filepath)
            style = model.predict(image)
            detected_items = detector.detect_items(image)
            
            # ユーザープロファイルの取得（実際のアプリケーションではユーザー認証後に取得）
            user_profile = UserProfile(age=30, gender='female', body_type='average', preferences=['casual', 'comfortable'])
            
            # 季節と場面の取得
            season = request.form.get('season', 'spring')
            occasion = request.form.get('occasion', 'casual')
            
            # パーソナライズされた推奨事項の生成
            recommendation = get_personalized_recommendation(style, user_profile)
            recommendation = adjust_recommendation_for_season_and_occasion(recommendation, season, occasion)
            
            # 検出されたアイテムごとの推奨事項を追加
            for item in detected_items:
                item_recommendation = detector.get_item_specific_recommendation(item)
                recommendation += f"\n{item}について: {item_recommendation}"
            
            return jsonify({
                'style': style,
                'recommendation': recommendation,
                'detected_items': detected_items,
                'image_path': filepath
            })
        except Exception as e:
            return jsonify({'error': f'File upload failed: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)