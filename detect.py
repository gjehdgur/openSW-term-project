while True:
    ret,frame=capture.read()
    frame=cv2.flip(frame,1)
    if cv2.waitKey(10)>0:
        cv2.destroyAllWindows()
        break
    try:    
        preprocessed=preprocessing(frame) #이미지 전처리
        prediction=predict(preprocessed) #텐서플로 모델로  분류기 적용 
    except Exception as e:
        print(e)
    #print(prediction)
    num=0
    for i in prediction[0]:
         if(i>0.9):
              print(num)
              if(num==0): #0 일 경우 노마스크
                   print('no mast')
              if(num==1): # 1일 경우 마스크
                   print('mask')
         num=num+1
    cv2.imshow('test',frame) #이미지 창에서 영상 표현
