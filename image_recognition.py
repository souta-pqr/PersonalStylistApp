from transformers import DetrFeatureExtractor, DetrForObjectDetection
import torch

class ClothingItemDetector:
    def __init__(self):
        self.feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
        self.model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    def detect_items(self, image):
        inputs = self.feature_extractor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        
        # 新しい出力形式に対応
        probas = outputs.logits.softmax(-1)[0, :, :-1]
        keep = probas.max(-1).values > 0.9  # 信頼度が90%以上の検出結果のみを使用
        
        items = []
        for p, box in zip(probas[keep], outputs.pred_boxes[0, keep]):
            class_id = p.argmax().item()
            label = self.model.config.id2label[class_id]
            items.append(label)
        
        return items

    def get_item_specific_recommendation(self, item):
        item_recommendations = {
            'person': "人物に合わせた服装を選びましょう。",
            'bicycle': "サイクリングに適した服装を選びましょう。",
            'car': "ドライブに適した快適な服装を選びましょう。",
            'motorcycle': "バイクに乗るときは安全性を考慮した服装を。",
            'airplane': "飛行機旅行には快適で機内で調節しやすい服装を。",
            'bus': "公共交通機関利用時は清潔感のある服装を心がけましょう。",
            'train': "電車での移動に適した動きやすい服装を。",
            'truck': "作業に適した丈夫で機能的な服装を選びましょう。",
            'boat': "マリンアクティビティに適した服装を。日よけも忘れずに。",
            'traffic light': "交通安全を意識した明るい色の服装を心がけましょう。",
            'fire hydrant': "アウトドア活動に適した服装を選びましょう。",
            'stop sign': "目立つ色使いの服装で安全性を高めましょう。",
            'parking meter': "都市部での活動に適したスマートカジュアルを。",
            'bench': "公園やアウトドアでくつろげる服装を。",
            'bird': "自然の中でのアクティビティに適した服装を。",
            'cat': "ペットと過ごすときは動きやすく、毛が付きにくい素材を選びましょう。",
            'dog': "ペットの散歩に適した動きやすい服装を。",
            'horse': "乗馬に適した服装を選びましょう。",
            'sheep': "田舎や農場訪問時は動きやすく汚れてもよい服装を。",
            'cow': "農場訪問時は動きやすく汚れてもよい服装を。",
            'elephant': "サファリや動物園訪問時は動きやすく涼しい服装を。",
            'bear': "アウトドア活動に適した丈夫で保護的な服装を。",
            'zebra': "サファリや動物園訪問時はカジュアルで動きやすい服装を。",
            'giraffe': "動物園訪問時は歩きやすく快適な服装を。",
            'backpack': "バックパックに合わせた機能的で動きやすい服装を。",
            'umbrella': "雨の日に適した防水性のある服装を選びましょう。",
            'handbag': "ハンドバッグに合わせたエレガントな服装を。",
            'tie': "フォーマルな場面に適したスーツスタイルを。",
            'suitcase': "旅行に適した快適で機能的な服装を選びましょう。",
            'frisbee': "アウトドアスポーツに適した動きやすい服装を。",
            'skis': "スキーに適した防寒性と機能性のある服装を。",
            'snowboard': "スノーボードに適した防寒性と機能性のある服装を。",
            'sports ball': "スポーツに適した動きやすい服装を選びましょう。",
            'kite': "凧揚げなどの屋外活動に適した動きやすい服装を。",
            'baseball bat': "野球に適した動きやすいユニフォームスタイルを。",
            'baseball glove': "野球に適した動きやすいユニフォームスタイルを。",
            'skateboard': "スケートボードに適したカジュアルでクールな服装を。",
            'surfboard': "サーフィンに適した水着や日よけ対策を忘れずに。",
            'tennis racket': "テニスに適した動きやすいスポーツウェアを。",
            'bottle': "アウトドア活動に適した機能的な服装を選びましょう。",
            'wine glass': "パーティーやディナーに適したエレガントな服装を。",
            'cup': "カフェやカジュアルな集まりに適した服装を。",
            'fork': "食事の場面に適した服装を選びましょう。",
            'knife': "料理や食事の場面に適した服装を選びましょう。",
            'spoon': "カジュアルな食事の場面に適した服装を。",
            'bowl': "家庭的な雰囲気に合う快適な服装を。",
            'banana': "カジュアルな日常生活に適した服装を。",
            'apple': "健康的なライフスタイルに合う爽やかな服装を。",
            'sandwich': "カジュアルなランチ時に適した服装を。",
            'orange': "明るく元気な雰囲気を演出する服装を。",
            'broccoli': "健康的な生活に合う爽やかな服装を。",
            'carrot': "カジュアルで健康的な印象の服装を。",
            'hot dog': "カジュアルな外食時に適した服装を。",
            'pizza': "カジュアルな集まりに適した快適な服装を。",
            'donut': "リラックスした雰囲気に合う服装を。",
            'cake': "お祝いの場面に適したちょっとしゃれた服装を。",
            'chair': "オフィスや家庭での快適な服装を選びましょう。",
            'couch': "リラックスした雰囲気に合う快適な服装を。",
            'potted plant': "ガーデニングや自然に親しむ活動に適した服装を。",
            'bed': "快適な睡眠のためのパジャマや部屋着を選びましょう。",
            'dining table': "食事の場面に適した清潔感のある服装を。",
            'toilet': "家庭での快適な服装を心がけましょう。",
            'tv': "リラックスした時間に適した快適な服装を。",
            'laptop': "在宅勤務やカジュアルな仕事場面に適した服装を。",
            'mouse': "デスクワークに適した快適で知的な印象の服装を。",
            'remote': "リラックスした家庭での時間に適した服装を。",
            'keyboard': "デスクワークに適した快適で知的な印象の服装を。",
            'cell phone': "日常生活のあらゆる場面に適した汎用性のある服装を。",
            'microwave': "家事や料理の場面に適した機能的な服装を。",
            'oven': "料理や家事の際の安全性を考慮した服装を。",
            'toaster': "朝の時間帯に適した快適な服装を。",
            'sink': "家事や料理の場面に適した機能的な服装を。",
            'refrigerator': "家庭での日常生活に適した快適な服装を。",
            'book': "読書や勉強の時間に適した集中できる服装を。",
            'clock': "時間を意識した効率的な活動に適した服装を。",
            'vase': "家庭でのくつろいだ時間に適した服装を。",
            'scissors': "創作活動や日常の作業に適した機能的な服装を。",
            'teddy bear': "リラックスした家庭での時間や子供との時間に適した服装を。",
            'hair drier': "身だしなみを整える時間に適した服装を。",
            'toothbrush': "朝と夜の日課に適した快適な服装を選びましょう。"
        }
        return item_recommendations.get(item, "このアイテムに合わせたコーディネートを考えてみましょう。")