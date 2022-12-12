#한하람,  commit,파일 이름: preprocessing

def preprocessing(frame):
    size=(224,224)
    frame_resize=cv2.resize(frame,size,interpolation=cv2.INTER_AREA)
    frame_normalized=(frame_resize.astype(np.float32)/127.0)-1  #이미지 정규화 
    frame_reshaped=frame_normalized.reshape((1,224,224,3))  # 전처리 
    return frame_reshaped
