import random
import pandas

class Card_Manager:
    def __init__(self):
        self.data = pandas.read_csv("./data/ja.csv")
        self.data = self.data.to_dict(orient="records")

    def pickOne(self):
        index = random.randint(0,len(self.data)-1)
        item = self.data.pop(index)
        return (item["English"], item["Japanese"])