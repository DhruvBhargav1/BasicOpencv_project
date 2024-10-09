import cv2
#video capture instance
cap=cv2.VideoCapture('sample.mp4')

#properties of video

#total number of frames in video
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)

#FRAME PER SECOND OF VIDEO(used for writing the video)
fps=cap.get(cv2.CAP_PROP_FPS)

#HEIGHT AND WIDTH OF THE VIDEO
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#initializing the output writer of the video
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width*0.5),int(height*0.5)))

print("No of frames are: {}".format(frames))
print("FPS is:{}".format(fps))

#we get the index of last frames of the video file
frame_index=frames-1

#checking if video instance is ready
if(cap.isOpened()):
    #reading till the end of the video
    while(frame_index!=0):
        #we set the current frame position to the last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame=cap.read()
        
        #resize the frame
        frame=cv2.resize(frame, (int(width*0.5),int(height*0.5)))
        
        #optional: to show the reversing video
        cv2.imshow('winname',frame)
        
        #writing the reversed video
        out.write(frame)
        #decremenating frame index at each step
        frame_index=frame_index-1
        
        
        #priting the progress
        if(frame_index%100==0):
            print(frame_index)
        if(cv2.waitKey(2)==ord('q')):
          break
                
out.release()
cap.release()
cv2.destroyAllWindows()        

