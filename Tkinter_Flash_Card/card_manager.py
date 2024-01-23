import random
import pandas
from enum import Enum

class WritingType(Enum):
    WRITE = 1
    UPDATE = 2

class Card_Manager:
    def __init__(self):
        try:
            self.data = pandas.read_csv("./data/words_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("./data/ja.csv")

        self.data = self.data.to_dict(orient="records")
        self.pickOne()


    def pickOne(self):
        index = random.randint(0,len(self.data)-1)
        self.current_word = {"english": self.data[index]["English"], "trans": self.data[index]["Japanese"], "index": index}

        return self.current_word
    
    def has_learned(self):
        item = self.data.pop(self.current_word["index"])
        item = [{
            "English" : item["English"],
            "Japanese" : item["Japanese"]
        }]
        self.write_csv("learned", item, writing_type=WritingType.UPDATE, header=False)
        self.write_csv("words_to_learn", self.data, writing_type=WritingType.WRITE, header=True)
    
    def write_csv(self, file_name, data, writing_type=WritingType.WRITE, header: bool = True):
        dataFrame = pandas.DataFrame.from_records(data)
        dataFrame.to_csv(f"./data/{file_name}.csv", index=False, mode="w" if writing_type == WritingType.WRITE else "a", header=header)
