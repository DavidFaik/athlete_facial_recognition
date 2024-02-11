import cv2
from simple_facerec import SimpleFacerec
import pandas as pd



df = pd.read_excel("Stats.xlsx",index_col=0, dtype = {"Name":str, "Age": str, "Club": str, "Goals":str, "Asists": str}) 

xls = pd.ExcelFile('Stats.xlsx')
#df = xls.parse(xls.sheet_names[0])

dic=df.to_dict()

print(dic)

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        if name == 'Unknown':
            cv2.putText(frame, name,(x1+200, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        else:
            cv2.putText(frame, name,(x1+200, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, 'Age: ' + str(dic['Age'][name]),(x1+200, y1 + 20), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, 'Goals: ' + str(dic['Goals'][name]),(x1+200, y1 + 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame, 'Assists: ' + str(dic['Assists'][name]),(x1+200, y1 + 80), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()