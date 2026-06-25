import cv2 
import torchreid

# init ReID model
extractor = torchreid.utils.FeatureExtractor(
    model_name='osnet_x1_0',
    device='cpu'
)

image = cv2.imread('../data/test_person.jpg')

features = extractor(image)

print("Feature vector shap:", features.shape)
print(features)