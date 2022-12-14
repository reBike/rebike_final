from .models import trash_image, challenge, user_challenge
from rebikeuser.models import user

import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import torch, cv2
import os

from PIL import Image

from uuid import uuid4

def get_img_url(img):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    image = img
    image_type = "jpg"
    image_uuid = str(uuid4())
    s3_client.put_object(Body=image, Bucket='image-bucket2', Key=image_uuid + "." + image_type)
    image_url = "http://image-bucket2.s3.ap-northeast-2.amazonaws.com/" + \
                image_uuid + "." + image_type
    image_url = image_url.replace(" ", "/")
    return image_url

def get_ai_result(image):
    img = Image.frombytes(image['mode'], image['size'], image['pixels'])

    hubconfig = os.path.join(os.getcwd(), 'rebiketrash', 'yolov5')
    weightfile = os.path.join(os.getcwd(), 'rebiketrash', 'yolov5',
                              'runs', 'train', 'garbage_yolov5s_results', 'weights', 'best.pt')
    model = torch.hub.load(hubconfig, 'custom',
                           path=weightfile, source='local')
    results = model(img)

    results_dict = results.pandas().xyxy[0].to_dict(orient="records")
    if not results_dict:
        return {"ai_results":0, "image_url":0}
    else:
        ai_results = []
        for result in results_dict:
            if result.get('name') not in ai_results:
                ai_results.append(result.get('name'))
    
    results.render()
    RGB_img = cv2.cvtColor(results.imgs[0], cv2.COLOR_RGB2BGR)    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
    success, a_numpy = cv2.imencode('.jpg', RGB_img, encode_param)
    image = a_numpy.tostring()

    image_url = get_img_url(image)

    return {"ai_results":' '.join(ai_results), "image_url":image_url}


def check_challenge(user_id):
    uploaded_img_count = trash_image.objects.filter(user_id=user_id).count()

    challenge_info = 0
    challenge_id = 1
    for i in [1, 3, 5, 7, 10]:
        if not user_challenge.objects.filter(user_id=user_id, challenge_id=challenge_id):
            if uploaded_img_count == i:
                challenge_info = create_user_challenge(user_id, challenge_id)
        challenge_id += 1

    if challenge_info == 0:
        challenge_id = 'NONE'
        challenge_content = 'NONE'
    else:
        challenge_id = challenge_info.id
        challenge_content = challenge_info.content
    return challenge_id, challenge_content


def create_user_challenge(user_id, challenge_number):
    user_challenge.objects.create(user_id=user.objects.get(id=user_id),
                                  challenge_id=challenge.objects.get(id=challenge_number))
    return challenge.objects.get(id=challenge_number)
