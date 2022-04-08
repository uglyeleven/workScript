import os, shutil


def main():
    filePath = input("请输入路径")
    fileNameList = getMap(filePath)
    creatDir(fileNameList,filePath)
    moveFIle(filePath)

def getMap(path):
    fileNameMap = {}
    filelist = os.listdir(path)
    finalNameLen = 6
    for fileName in filelist:
        if len(fileName) == 13 + finalNameLen or len(fileName) == 12 + finalNameLen or len(fileName) == 8 + finalNameLen:  #8位、12位、13位条码
            if fileName[:-finalNameLen] not in fileNameMap and os.path.splitext(fileName)[1] == '.jpg':
                fileNameMap[fileName[:-finalNameLen]] = True

    return fileNameMap



def creatDir(fileNamelist,path):
    for fileName in fileNamelist:#
        os.makedirs(path + '\\'+fileName)


def moveFIle(path):
    finalNameLen = 6
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.splitext(file)[1] == '.jpg' :        #如果文件是jpg文件，则将此jpg文件移入对应的文件夹
            shutil.move(path +'\\'+ file, path + '\\' + file[:-finalNameLen])



if __name__ == '__main__':
    main()
