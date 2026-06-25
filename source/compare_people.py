import cv2
import torch
import torchreid
from torch.nn.functional import cosine_similarity

# init feature extractor
extractor = torchreid.utils.FeatureExtractor(
    model_name='osnet_x1_0',
    device='cpu'
)

img1 = cv2.imread("../data/test_person.jpg")
img2 = cv2.imread("../data/test_another_person.jpg")

feat1 = extractor(img1)
feat2 = extractor(img2)

similarity = cosine_similarity(feat1, feat2)

print("Similarity score:", similarity)