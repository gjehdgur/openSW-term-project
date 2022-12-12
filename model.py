model_filename="./converted_keras/keras_model.h5"
try:
    capture=cv2.VideoCapture(0) #카메라 열기
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) #이미지 가로 픽셀
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #이미지 세로 픽셀 
    model=tensorflow.keras.models.load_model(model_filename) #텐서플로 이미지 분류기 가져오기
except Exception as e:
    print(e)
