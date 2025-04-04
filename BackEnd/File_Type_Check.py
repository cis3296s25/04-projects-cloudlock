#means from a specific python file, import all its functions
import os.path

def checking_file_type(filePath):
    FileTypesNames = {"png": ".png", "jpeg": ".jpeg", "text": ".txt", "pdf": ".pdf", "wordDoc": "docx",
                       "powerpoint": ".pptx", "excel": ".xlsx", "mp4": ".mp4", "mp3": ".mp3"}
    #the above can be done with magic but it would mean the user would need to install magic before running
    #and that can cause issues

    if(os.path.isfile(filePath)):
        for(fileName,fileType) in FileTypesNames.items():
            #for each key value pair...
            #if it matches a value in our dictionary, return the key which is the file type
            if(filePath.lower().endswith(fileType)):
                return fileName


def correct_file_for_test(filePath):
    fileName = checking_file_type(filePath)

    if(fileName == "text"):
        return True
    else:
        return False

def encrypting_file(filePath):
    if(correct_file_for_test(filePath)):


#correctFileForTest("C:\\Users\\Salwa\\Downloads\\seq2.txt")