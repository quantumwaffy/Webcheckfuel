from .parsexml import parsing5676 as ps
from .scanfiles import scan as sc
from time import sleep

dlist = []
def startgetinf():
    scan = sc()
    for file in scan.checkfiles():
        if file in dlist:
            print("Files done")
            scan.removefiles(file)
        else:
            dlist.append(file)
            train = ps()
            train.parsingxml(file)
            print("Parsing")
            print(dlist)
            train.gotosql()
            scan.movefiles(file)
            scan.removefiles(file)
            del train
    del scan


# def make():
#     tr = calculation()
#     tr.maketrainsql()
# make()

# def main():
#     startgetinf()
# main()

if __name__ == '__main__':
    startgetinf()


# active = True
# while active:
#     sleep(3)
#     main()


















