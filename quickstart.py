from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

captionArray = []
confidenceArray = []
tagArray= []
def imagemake(imagePath, key, endpoint):
    key = key
    endpoint = endpoint
    creds = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(endpoint= endpoint, credentials=creds)

    with open(imagePath, "rb") as img:
        describe_result = client.describe_image_in_stream(img)

    for caption in describe_result.captions:
        print("Caption:", caption.text)
        captionArray.append(caption.text)
        print("Confidence:", caption.confidence)
        confidenceArray.append(caption.confidence)
    # Get image tags
    with open(imagePath, "rb") as img:
        features = ["tags"]
        analyze_result = client.analyze_image_in_stream(img, visual_features=features)

    tagkey = []
    for tag in analyze_result.tags:
        tagkey.append(tag.name)
    tagArray.append(tagkey)


# 파일이 존재하는지 확인
def check_file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)


key = "30a5a843ef184b9481f6a39a0e8ca3ef"
endpoint = "https://jhs.cognitiveservices.azure.com/"



for i in range(634):
    imagePath = "/Users/jeonhyoseong/Tagging_system/CBImageGroup/number{}".format(i) + "/frame" + "{}".format(0).zfill(
        4) + ".png"
    if check_file_exists(imagePath):
        imagemake(imagePath, key, endpoint)
        print("success: " + str(i))



