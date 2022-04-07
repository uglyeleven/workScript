import os, shutil


def main():
    filePath = "G:\\Try"
    dirPath = "G:\\Try"
    fileNameList = getMap(filePath)
    creatDir(fileNameList,dirPath)
    moveFIle(dirPath)

def getMap(path):
    fileNameMap = {}
    filelist = os.listdir(path)
    for file in filelist:
        if file[:-6] not in fileNameMap and file[-1] == 'g':
            fileNameMap[file[:-6]] = True
    return fileNameMap

def creatDir(fileNamelist,path):
    for fileName in fileNamelist:#
        os.makedirs(path + '\\'+fileName)


def moveFIle(path):
    filelist = os.listdir(path)
    for file in filelist:
        if file[-1] == 'g' :        #如果文件是jpg文件，则将此jpg文件移入对应的文件夹
            shutil.move(path +'\\'+ file, path + '\\' + file[:-6])



if __name__ == '__main__':
    main()
