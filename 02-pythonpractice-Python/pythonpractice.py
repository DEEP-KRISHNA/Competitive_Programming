"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self): 
        self.items = []

    def addItem(self, s):
        self.items.append(s)
    
    def classiness(self):
        score = 0
        for i in self.items:
            if (i == "tophat"):
                score = score + 2
            elif (i == "bowtie"):
                score = score + 4
            elif (i == "monocle"):
                score = score + 5
        return score    

# def main():
#     me = Classy()
#     result = me.classiness()
#     me.addItem("tophat")
#     result = me.classiness()
#     me.addItem("bowtie")
#     me.addItem("jacket")
#     me.addItem("monocle")
#     result = me.classiness()
#     me.addItem("bowtie")
#     result = me.classiness()
#     print(result)

# if __name__ == "__main__":
#     main()
