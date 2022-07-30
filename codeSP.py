from pandas.io.formats.style import jinja2


class PythonProject:
    projectName = "Playing With Graph in classical Physics"
    name = "Shreyansh"
    field_of_Research = "Motion in 1 Dimension"

    def __init__(self) -> None:
        print("You are doing analysis ", end="")

    @classmethod
    def setProjectName(cls, str):
        cls.projectName = str

    @staticmethod
    def displayProjectName():
        print("\nThe python project name is Playing With Graph in classical Physics\n")

    def settingData(self, s1, s2):
        self.name = s1
        self.displayProjectName = s2


PythonProject.displayProjectName()
print("The field of analysis is ", PythonProject.field_of_Research, "\n")


class DistanceTimeAnalysis(PythonProject):
    dict1 = {}

    @classmethod
    def settingDict1(cls, dict2):
        cls.dict1 = dict2

    def __init__(self) -> None:
        super().__init__()
        print("of Distance vs time graph")

    def totalDisplacement(self):
        t1 = 0
        t0 = int(self.dict1["displacement"][0])
        for x in self.dict1["displacement"]:
            t1 = x
        t1 = t1-t0
        return t1

    def totalTime(self):
        tim1 = 0
        tim0 = int(self.dict1["time"][0])
        for y in self.dict1["time"]:
            tim1 = y
        totalTime1 = tim1-tim0
        return totalTime1

    def avgVelocity(self):
        d1 = self.totalDisplacement()
        t1 = self.totalTime()
        return d1/t1

    def documentationOfSTGraph(self):
        f = open("DistanceTimeAnalysis.txt", "r")
        print(f.read())
        f.close()

    def convertXTtoVtGraph(self):
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        edge_error = 0.000000000000001
        dict_acceleration = {"acc": [], "time": []}
        j = 0
        for x in df.index:
            if j == 0:
                pass
            else:
                dict_acceleration["acc"].append(
                    (df.loc[x, "displacement"]-df.loc[x-1, "displacement"])/(df.loc[x, "time"]-df.loc[x-1, "time"]))
                dict_acceleration["acc"].append(
                    (df.loc[x, "displacement"]-df.loc[x-1, "displacement"])/(df.loc[x, "time"]-df.loc[x-1, "time"]))
                dict_acceleration["time"].append(
                    df.loc[x-1, "time"]+edge_error)
                dict_acceleration["time"].append(df.loc[x, "time"])
            j = j+1
        import pandas as pd
        import matplotlib.pyplot as p
        pf = pd.DataFrame(dict_acceleration)
        # 2 plots side by side
        # plot 1:
        p.subplot(1, 2, 1)
        p.plot(dict(df["time"]).values(), dict(df["displacement"]).values(), 'o-k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.ylabel("Displacement ------>", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.title(" Dislacement Time Graph", fontdict=font1, loc='center')
        # #plot 2:
        p.subplot(1, 2, 2)
        p.plot(dict(pf["time"]).values(), dict(pf["acc"]).values(), 'o-k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.ylabel("Velocity ------>", fontdict=font2)
        p.title(" Velocity Time Graph", fontdict=font1, loc='center')
        p.suptitle(
            "Displacement & its Corresponding Velocity Time ", fontdict=font3)

        p.show()

    def submitYourAnalysis(self):
        f = open("DistanceTimeAnalysis.txt", "a")
        str = input("Enter Your analysis during observation\n")
        f.write(str)
        f.close()


dict1 = {
    "displacement": [3, 6, 9, 12],
    "time": [1, 2, 3, 4]
}

obj=DistanceTimeAnalysis()
obj.settingDict1(dict1)
obj.convertXTtoVtGraph()
print("In our analysis the Average velocity of plotted X-T  graph is  ",obj.avgVelocity())
print("In our analysis the total Displacement in plotted graph is :  ",obj.totalDisplacement())
obj.documentationOfSTGraph()
obj.submitYourAnalysis()

# Velocity-Time Graph
class VelocityTimeAnalysis(PythonProject):
    dict1 = {}

    @classmethod
    def settingDict1(cls, dict2):
        cls.dict1 = dict2

    def __init__(self, d2) -> None:
        super().__init__()
        print("of Velocty vs time graph")
        self.dict1 = d2

    def totalDisplacementInGraph(self):
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        init = 0
        totalDis = 0
        final_velocity = 0
        for x in df.index:
            if init == 0:
                pass
            else:
                totalDis = totalDis + (0.5*(df.loc[x, "time"]-df.loc[x-1, "time"]) *
                                       (df.loc[x-1, "velocity"]+df.loc[x, "velocity"]))
            init = init+1
            # final_velocity=df.loc[x,"velocity"]
        return totalDis

    def avgVelocityDuringAnalysis(self):
        # pass
        t_dis = self.totalDisplacementInGraph()
        total_Time = 0
        j_in = 0
        init_Time = 0
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        for x in df.index:
            if j_in == 0:
                init_Time = df.loc[x, "time"]
            j_in = j_in+1

            total_Time = df.loc[x, "time"]

        return t_dis/(total_Time-init_Time)

    def avgAcceleration(self):
        t1 = 0
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        final_velocity = 0
        j_in = 0
        init_Time = 0
        init_vel = 0
        for x in df.index:
            if j_in == 0:
                init_Time = df.loc[x, "time"]
                init_vel = df.loc[x, "velocity"]
            final_velocity = df.loc[x, "velocity"]
            t1 = df.loc[x, "time"]
            j_in = j_in+1
        return ((final_velocity-init_vel)/(t1-init_Time))

    def documentationOfSTGraph(self):
        f = open("velocityTimeGraph.txt", "r")
        print(f.read())
        f.close()

    def submitYourAnalysis(self):
        f = open("velocityTimeGraph", "a")
        str = input("Enter Your analysis during observation\n")
        f.write(str)
        f.close()

    def minMaxVelocityDuringAnalysis(self):
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        vel_min = df.loc[0, "velocity"]
        vel_max = df.loc[0, "velocity"]
        for x in df.index:
            if vel_min > df.loc[x, "velocity"]:
                vel_min = df.loc[x, "velocity"]
            if vel_max < df.loc[x, "velocity"]:
                vel_max = df.loc[x, "velocity"]
        print("Minimum velocity during whole observation is", vel_min)
        print("Maximum velocity during whole observation is", vel_max)

    def convertVtToAtGraph(self):
        import pandas as pd
        df = pd.DataFrame(self.dict1)
        edge_error = 0.000000000000001
        dict_acceleration = {"acc": [], "time": []}
        j = 0
        for x in df.index:
            if j == 0:
                pass
            else:
                dict_acceleration["acc"].append(
                    (df.loc[x, "velocity"]-df.loc[x-1, "velocity"])/(df.loc[x, "time"]-df.loc[x-1, "time"]))
                dict_acceleration["acc"].append(
                    (df.loc[x, "velocity"]-df.loc[x-1, "velocity"])/(df.loc[x, "time"]-df.loc[x-1, "time"]))
                dict_acceleration["time"].append(
                    df.loc[x-1, "time"]+edge_error)
                dict_acceleration["time"].append(df.loc[x, "time"])
            j = j+1
        import pandas as pd
        import matplotlib.pyplot as p
        pf = pd.DataFrame(dict_acceleration)
        # 2 plots side by side
        # plot 1:
        p.subplot(1, 2, 1)
        p.plot(dict(df["time"]).values(), dict(df["velocity"]).values(), 'o-k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.ylabel("Velocity ------>", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.title(" Velocity Time Graph", fontdict=font1, loc='center')
        # #plot 2:
        p.subplot(1, 2, 2)
        p.plot(dict(pf["time"]).values(), dict(pf["acc"]).values(), 'o-k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.ylabel("Acceleration ------>", fontdict=font2)
        p.title(" acceleration Time Graph", fontdict=font1, loc='center')
        p.suptitle(
            "Velocity & its Corresponding acceleration Time ", fontdict=font3)

        p.show()

    @ classmethod
    def doAnalysisUsingImportedFile(cls):
        # pass
        import pandas as pd
        df = pd.read_csv('velocityData.csv')
        inpt = int(input(
            "Hey user enter 1 ,2,3 for replacing nill velocity in csv file as mean ,meadian and node respectively :\n"))
        if inpt == 1:
            mean_val = df["velocity"].mean()
        elif inpt == 2:
            mean_val = df["velocity"].median()
        else:
            mean_val = df["velocity"].mode()[0]

        df["velocity"].fillna(mean_val, inplace=True)
        # Removing row containing missing value(of time ) to change the original DataFrame as a meaningful Data
        df.dropna(inplace=True)

        # Drop Duplicates
        df.drop_duplicates(inplace=True)
        j = 0
        for x in df.index:
            df.loc[x, "velocity"] = df.loc[x, "velocity"]+12
            df.loc[x, "time"] = j
            j = j+1
        total_time = j

        # plotting graph of given data
        import matplotlib.pyplot as plt
        plt.plot(dict(df["time"]).values(), dict(
            df["velocity"]).values(), 'hotpink', marker='o', ms=1, mec='k')
        plt.xlabel("Time --->")
        plt.ylabel("Velocity ----->")
        plt.title("Velocity Time Deep Analysis")
        plt.show()

        vel_min = df.loc[0, "velocity"]
        vel_max = df.loc[0, "velocity"]
        for x in df.index:
            if vel_min > df.loc[x, "velocity"]:
                vel_min = df.loc[x, "velocity"]
            if vel_max < df.loc[x, "velocity"]:
                vel_max = df.loc[x, "velocity"]

        print("Minimum velocity during whole observation is", vel_min, "\n")
        print("Maximum velocity during whole observation is", vel_max, "\n")
        init = 0
        totalDis = 0
        final_velocity = 0
        for x in df.index:
            if init == 0:
                init = init+1
            else:
                totalDis = totalDis + (0.5*(df.loc[x, "time"]-prev_t) *
                                       (prev_vel+df.loc[x, "velocity"]))
            prev_t = df.loc[x, "time"]
            prev_vel = df.loc[x, "velocity"]
            final_velocity = df.loc[x, "velocity"]
        print("Total displacement during whole observation is", totalDis, "\n")
        print("average velocity during whole observation is",
              totalDis/total_time, "\n")
        print("average acceleration during whole observation is",
              final_velocity/total_time, "\n")
        edge_error = 0.000000000000001
        dict_acceleration = {"acc": [], "time": []}
        j = 0
        for x in df.index:
            if j == 0:
                pass
            else:
                dict_acceleration["acc"].append(
                    (df.loc[x, "velocity"]-prev_vel)/(df.loc[x, "time"]-prev_t))
                dict_acceleration["acc"].append(
                    (df.loc[x, "velocity"]-prev_vel)/(df.loc[x, "time"]-prev_t))
                dict_acceleration["time"].append(prev_t+edge_error)
                dict_acceleration["time"].append(df.loc[x, "time"])
            j = j+1
            prev_t = df.loc[x, "time"]
            prev_vel = df.loc[x, "velocity"]
        import pandas as pd
        import matplotlib.pyplot as p
        pf = pd.DataFrame(dict_acceleration)
        # 2 plots side by side
        # plot 1:
        p.subplot(1, 2, 1)
        p.plot(dict(df["time"]).values(), dict(df["velocity"]).values(), 'o-k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.ylabel("Velocity ------>", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.title(" Velocity Time Graph", fontdict=font1, loc='center')
        # #plot 2:
        p.subplot(1, 2, 2)
        p.plot(dict(pf["time"]).values(), dict(pf["acc"]).values(), 'o--k')
        font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
        font2 = {'family': 'cursive', 'color': 'green', 'size': 10}
        font3 = {'family': 'cursive', 'color': 'red', 'size': 100}
        p.xlabel("Time ----->", fontdict=font2)
        p.grid(color='hotpink', linestyle='--', linewidth=0.2)
        p.ylabel("Acceleration ------>", fontdict=font2)
        p.title(" acceleration Time Graph", fontdict=font1, loc='center')
        p.suptitle(
            "Velocity & its Corresponding acceleration Time ", fontdict=font3)

        p.show()
        y=int(input("Hey! enter 1 if you want to see documentation of Acceleration Time Graph else enter 2\n"))
        if y==1:
            f = open("accelerationTimeGraph.txt", "r")
            print("The documentation of Acceleration Time graph is as follows ")
            print(f.read())
            f.close()
            print("Thanks for your response ")
        else:
            print("Thanks for your response ")

dict2 = {
    "velocity": [3, 6, 9, 12],
    "time": [1, 2, 3, 4]
}
import numpy as np
import pandas as pd
# newdf=pd.DataFrame(np.random.rand(334,2),index=np.arange(334))
# newdf.to_csv('Velocitydata.csv')
obj = VelocityTimeAnalysis(dict2)
obj.convertVtToAtGraph()
print("Total displacement during observation of plotted V-T Graph :  ",
      obj.totalDisplacementInGraph(), "\n")
print("Average Acceleration during observation of Plotted V-T Graph  : ", obj.avgAcceleration(), "\n")
obj.minMaxVelocityDuringAnalysis()
print("final")

VelocityTimeAnalysis.doAnalysisUsingImportedFile()
