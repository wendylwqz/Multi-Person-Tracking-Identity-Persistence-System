import cv2
import torchreid
from torch.nn.functional import cosine_similarity

extractor = torchreid.utils.FeatureExtractor(
    model_name='osnet_x1_0',
    device='cpu'
)

memory_bank = {}

img1 = cv2.imread("../data/test_person.jpg")
feat1 = extractor(img1)

memory_bank[1] = feat1

img2 = cv2.imread('../data/test_another_person.jpg')
feat2 = extractor(img2)

best_id = None
best_score = 0

for person_id, stored_feat in memory_bank.items():
    score = cosine_similarity(feat2, stored_feat).item()
    
    print(f"Comparing with person {person_id}: {score:.3f}")

    if score > best_score:
        best_score = score
        best_id = person_id

print("\nBest match:")
print(best_id, best_score)