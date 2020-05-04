
import shutil
import os







class FileHandleFuncs:
    def imp(name):
        m = __import__(name)
        for n in name.split(".")[1:]:
            m = getattr(m, n)

        return m
		
		
    def load_binary(file):
        with open(file, 'rb') as file:
            return file.read()

    def getListOfFiles(dirName, filter=""):
        ret = []
        for root, dirs, files in os.walk(dirName):
            for file in files:
                if filter == "" or filter in file:
                    ret.append(os.path.join(root, file))
        return ret

    def deleteAll(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))



    def getListOfUnprotFiles(dirName):
        ret = []
        for root, dirs, files in os.walk(dirName):
            for file in files:
                if not "Protected" in root.split("/"):
                    ret.append(os.path.join(root, file))
        return ret

    def getListOfFolders(dirName):
        ret = []
        for root, dirs, files in os.walk(dirName):
            for file in dirs:
                if not "Protected" in file.split("/"):
                    ret.append(os.path.join(root, file))
        return ret
