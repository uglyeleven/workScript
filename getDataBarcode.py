import os, shutil, re

def getBarcode(rowFilePath, dirPath):
    fileList = os.listdir(rowFilePath)
    for file in fileList:
        if '.' not in file:
            firstPath = rowFilePath + '\\' + file
            dataFile = os.listdir(firstPath)
            for data in dataFile:
                secondPath = rowFilePath + '\\' + file + '\\' + data
                if os.path.splitext(secondPath)[1] == '.txt':
                    key = '标识数据译码'
                    txt = open(secondPath, 'r')
                    lineList = txt.readlines()
                    for line in lineList:
                        if key in line:
                            rs = re.findall('\d*', line)
                            barCode = ''.join(rs).replace(" ", "")
                            shutil.copyfile(secondPath, dirPath + '\\' + barCode +'.txt')
                    txt.close()
        else:
            print('File {} not a dir'.format(file))
            pass


def main():
    rowFilePath = input("请输入未处理数据文件夹存放目录")
    dirPath = input("请输目标目录")
    getBarcode(rowFilePath, dirPath)

if __name__ == '__main__':
    main()
