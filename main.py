from datetime import datetime
import pip
pip.main(['install', 'qrcode'])
pip.main(['install', 'pyzbar'])
pip.main(['install', 'opencv-python'])
pip.main(['install', 'numpy'])
global yes
yes = False
global attendence
attendence = False

def attendence_marked():
    # global attendence
    attendence = False

def generate_qrcode():
    import qrcode

    img = qrcode.make(input("Admission Number: "))
    file_name = input("File Name: ")
    img.save(f"""C:\\Coding\\Attendance System\\{file_name}.jpg""")
    img.show(f"""C:\\Coding\\Attendance System\\{file_name}.jpg""")
    print("QR Code Sucessfully Generated")

def not_found():
    # global attendence
    # attendence = False
    pass

def mark_present(row_index, addmision_number):
    import datetime
    import csv
    file=open('data.csv')
    Reader = csv.reader(file, delimiter=',')
    L=[]
    admission=int(addmision_number)
    import datetime
    x = str(datetime.datetime.now())
    date = x[:19]
    Uroll = admission
    Found2=False
    for row in Reader:
        if row[1] == str(Uroll):
            Found2=True
            Stream="Present " + str(date)
            row[2] = Stream 
        L.append(row)
    file.close()
    # print("not udated")
    if Found2 == False:
        not_found()
    else:
        file=open("data.csv", "w+", newline='')
        Writer=csv.writer(file)
        Writer.writerows(L)
        file.seek(0)
        Reader=csv.reader(file)
        for row in Reader:
            pass
        file.close()
        global yes
        yes = True
        attendence_marked()

def get_index(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos

def attendence_marked():
    # global attendence
    attendence = False

def change_data(admission_no):
    import pandas as pd
    df = pd.read_csv("data.csv")
    for (columnName, columnData) in df.iteritems():
        # print('Column Name : ', columnName)
        # print('Column Contents : ', columnData.values)
        if columnName == "Admission No.":
            for i in columnData.values:
                if i == admission_no:

                    
                    import csv

                    filename = 'data.csv'

                    with open(filename, 'r') as csvfile:
                        datareader = csv.reader(csvfile)
                        for row in datareader:
                            # print(row[2])
                            # mark_present(1)
                            # print(i)
                            # Get list of index positions i.e. row & column of all ocṇcurrences of 81 in the dataframe
                            listOfPositions = get_index(df, admission_no)
                            # print('Index positions of 81 in Dataframe : ')
                            for j in range(len(listOfPositions)):
                                # print('Position ', j, ' (Row index , Column Name) : ', listOfPositions[j])
                                var = str(listOfPositions[j])
                                row = str(var[1:2])
                                column_name = str(var[5:18])
                    # mark_present(row, admission_no)
    if yes == False:
        not_found()  

def save_file():
    import pandas as pd
    df = pd.read_csv("data.csv")
    df.to_csv("data.csv", index=False)


def main(number):
    if __name__ == '__main__':
        change_data(number)
        save_file()


import cv2
import numpy as np
from pyzbar.pyzbar import decode
# from tkinter import tkinter.messagebox
def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    cv2.putText(frame, "Press 'q' to quit",(50,50), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255), 2)
    for obj in barcode:

        barcodeData = str(obj.data.decode("utf-8"))
        barcodeType = obj.type
        # string = str(barcodeData)
        
        import csv
        file=open('data.csv')
        Reader = csv.reader(file, delimiter=',')
        # L=[]
        # admission=int(addmision_number)
        # import datetime
        # x = str(datetime.datetime.now())
        # date = x[:19]
        # Urotill = admission
        # Found=False
        string="Not Found"
        color = (0,0,0)
        Found = False
        for row in Reader:
            # print(type(row[1]))
            if row[1] == str(barcodeData):
                Found=True
                string=row[0]
                # row[2] = Stream 
                color = (255,0,0)
           
        if Found == False:
            color = (0,0,255)
        else:
            color = (0,255,0)
        # string = Stream
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, color, 3)
        file.close()
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,color, 2)
        # print(barcodeData)
        # global attendence
        # print(str(attendence))
        # print(barcodeData)
        if Found == True:
            cv2.putText(frame, "Attendence Marked",(0,500), cv2.FONT_HERSHEY_SIMPLEX,0.8,(250,0,0), 2) 
            save_file()
            import datetime
        import csv
        file=open('data.csv')
        Reader = csv.reader(file, delimiter=',')
        L=[]
        admission=barcodeData
        import datetime
        x = str(datetime.datetime.now())
        date = x[:19]
        Uroll = admission
        Found2=False
        for row in Reader:
            if row[1] == str(Uroll):
                Found2=True
                Stream="Present " + str(date)
                row[2] = Stream 
            L.append(row)
        file.close()
        # print("not udated")
        if Found2 == False:
            not_found()
        else:
            file=open("data.csv", "w+", newline='')
            Writer=csv.writer(file)  
            Writer.writerows(L)
            file.seek(0)
            Reader=csv.reader(file)
            for row in Reader:
                pass
            file.close()
            global yes
            yes = True
            attendence_marked()  

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break