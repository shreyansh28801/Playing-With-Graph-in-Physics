class ModernPhysics:
    def showGraph(self):
        import codeS
        codeS.plt.show()
        f = open("detailsS.txt", "r")
        a = f.read()
        print(a)


class Gravitation:
    def showGraph(self):
        import codeK
        f = open("detailsK.txt", "r")
        a = f.read()
        print(a)


class Thermodynamics:
    def showGraph(self):
        import codeSA
        codeSA.plt.show()
        f = open("detailsSA.txt", "r")
        a = f.read()
        print(a)


class kinematics:
    def showGraph(self):
        import codeSP


class BingeGraphs:
    def __init__(self, order):
        if order == "Yes":
            print("We are ready for the Search")
            print(".......................................")
            print("What are you searching for?")
            print("ENTER 1 for Modern Physics")
            print("ENTER 2 for Gravitation")
            print("ENTER 3 for Kinematics")
            print("ENTER 4 for Thermodynamics")
            print("ENTER 0 for the Slideshow of all the domains.")
            print(".......................................")
            what = input()
            if what == '1':
                ModernPhysics.showGraph(self)
            elif what == '2':
                Gravitation.showGraph(self)
            elif what == '3':
                kinematics.showGraph(self)
            elif what == '4':
                Thermodynamics.showGraph(self)
            elif what == '0':
                ModernPhysics.showGraph(self)
                Gravitation.showGraph(self)
                kinematics.showGraph(self)
                Thermodynamics.showGraph(self)
            else:
                print("invalid input")
        else:
            print("Program Terminated. Thank you, May you have a Good Day.")


print("If you are ready to explore our project, type Yes else type No.")
response = input()
OurProject = BingeGraphs(response)
