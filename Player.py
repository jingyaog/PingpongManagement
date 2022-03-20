import csv

def flatten(t):
    return [item for sublist in t for item in sublist]

class Player:
    def __init__(self, index):
        self.index = index
        self.name = None
        choice = input("Do you have a previously registered name for Player "
                       + str(self.index) + "? Y/N\n")
        if choice == "Y": self.chooseName()
        elif choice == "N": self.registerName()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def chooseName(self):
        with open('names.csv', mode="r") as f:
            reader = csv.reader(f)
            names = [row for row in reader]
            print("Please choose your name from the list by typing the name: \n")
            print(flatten(names[1:]))
        self.name = input()

    def registerName(self):
        new_name = input("Please register your name: \n")
        with open('names.csv', mode="r") as f_in:
            reader = csv.reader(f_in)
            data = [row for row in reader]
            # print(data)
        with open('names.csv', mode="w") as f_out:
            # print(data)
            writer = csv.writer(f_out)
            data.append([new_name])
            writer.writerows(data)
        self.name = new_name
