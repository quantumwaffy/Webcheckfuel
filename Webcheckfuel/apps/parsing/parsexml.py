import datetime
import os
import sqlite3

from lxml import etree

from Webcheckfuel.settings import BASE_DIR


class parsing5676:
    def __init__(self):
        pass

    def parsingxml(self, xmlFile):
        with open(xmlFile) as f:
            xml = f.read().encode("utf-8")
        parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
        root = etree.fromstring(xml, parser=parser)
        train_dict = {}
        lok_dict = {}
        brig_dict = {}
        for value in root.getchildren():
            if value.tag == "TRAIN":
                for train in value.getchildren():
                    if train.tag == "LOKOMOTIV":
                        for lok in train.getchildren():
                            if lok.tag == "BR":
                                for br in lok.getchildren():
                                    brig_dict[br.tag] = br.text
                            lok_dict[lok.tag] = lok.text
                    if not train.text:
                        text = "None"
                    else:
                        text = train.text
                    train_dict[train.tag] = text
        parsdt = datetime.datetime.now()
        datop = train_dict["DATOP"].split("-")
        op_dt = (
            datop[0]
            + "-"
            + datop[1]
            + "-"
            + datop[2]
            + " "
            + datop[3].split(".")[0]
            + ":"
            + datop[3].split(".")[1]
            + ":"
            + datop[3].split(".")[2]
            + "."
            + datop[3].split(".")[3]
        )
        self.inf = (
            train_dict["IPP"],
            train_dict["NP"],
            train_dict["KSO"],
            train_dict["KOP"],
            op_dt,
            train_dict["KLGP"],
            train_dict["KLGRVG"],
            train_dict["KLPRVG"],
            lok_dict["SER"],
            lok_dict["NS"],
            parsdt,
        )

    def gotosql(self):
        db_path = os.path.join(BASE_DIR, "db.sqlite3")
        db = sqlite3.connect(db_path)
        sql = db.cursor()
        print(db_path)
        sql.execute(
            "INSERT INTO parsing_train(ip, num, op_st, op_name, op_dt, vag_all, vag_h, "
            "vag_l, loc_ser, loc_num, parse_dt) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);",
            self.inf,
        )
        db.commit()
        db.close()
