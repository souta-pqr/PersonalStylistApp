from transformers import DetrImageProcessor, DetrForObjectDetection
import torch

class ClothingItemDetector:
    def __init__(self):
        self.image_processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
        self.model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    def detect_items(self, image):
        inputs = self.image_processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        
        # 新しい出力形式に対応
        target_sizes = torch.tensor([image.size[::-1]])
        results = self.image_processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
        
        detections = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            detections.append({
                'box': box.tolist(),
                'label': self.model.config.id2label[label.item()],
                'confidence': score.item()
            })
        
        return detections