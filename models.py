from transformers import ViTImageProcessor, ViTForImageClassification
import torch

class StyleClassifier:
    def __init__(self):
        self.model_name = "google/vit-base-patch16-224"
        self.image_processor = ViTImageProcessor.from_pretrained(self.model_name)
        self.model = ViTForImageClassification.from_pretrained(self.model_name)
        
        self.model.eval()

        # ImageNetクラスラベルをファッションスタイルにマッピング
        self.style_mapping = {
            'shirt': 'casual',
            'jersey': 'sporty',
            'suit': 'formal',
            'dress': 'formal',
            'jean': 'casual',
            'sweatshirt': 'sporty',
            # 他のマッピングを追加...
        }

    def predict(self, image):
        with torch.no_grad():
            inputs = self.image_processor(images=image, return_tensors="pt")
            outputs = self.model(**inputs)
        
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_class = self.model.config.id2label[predicted_class_idx]

        # 予測されたクラスをスタイルにマッピング
        style = self.style_mapping.get(predicted_class.lower(), 'casual')  # デフォルトは'casual'
        return style