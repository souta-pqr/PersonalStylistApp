import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification

class StyleClassifier:
    def __init__(self):
        self.model_name = "google/vit-base-patch16-224"
        self.feature_extractor = ViTFeatureExtractor.from_pretrained(self.model_name)
        self.model = ViTForImageClassification.from_pretrained(self.model_name)
        
        # ここでモデルをファインチューニングしたものを読み込む
        # self.model.load_state_dict(torch.load('path_to_finetuned_model.pth'))
        
        self.model.eval()

    def predict(self, image):
        inputs = self.feature_extractor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        return self.model.config.id2label[predicted_class]