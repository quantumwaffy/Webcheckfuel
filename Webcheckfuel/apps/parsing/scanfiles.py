import os
import shutil

from lxml import etree


class scan:
    params = {}

    def getparams(self):
        config = os.path.join(os.path.dirname(__file__), "parsing5676.config")
        with open(config) as f:
            config = f.read().encode("utf-8")
        parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
        root = etree.fromstring(config, parser=parser)
        for value in root.getchildren():
            if value.tag == "PATH":
                self.params[value.tag] = value.text
            if value.tag == "PATHCOPY":
                self.params[value.tag] = value.text
        return self.params

    def checkfiles(self):
        paths = []
        self.getparams()
        dir_ = self.params["PATH"]
        for file in os.listdir(dir_):
            path = os.path.join(dir_, file).replace("\\", "/")
            paths.append(path)
        return paths

    def movefiles(self, file):
        dircopy = self.params["PATHCOPY"]

        if not os.path.exists(dircopy):
            os.mkdir(dircopy)
            print("PATHCOPY created")
        else:
            print("PATHCOPY exists")
            shutil.copy2(file, dircopy)

    def removefiles(self, file):
        os.remove(file)
