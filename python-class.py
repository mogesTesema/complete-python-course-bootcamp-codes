"""
create chatbot class with the following attribute and method:
1. __init__ 
2. __len__
3. __getint__
4. __repr__
5. __str__
6. chat()
7. history()
    can view n most recent chats, and delete any chat if necessary
8. recent()

"""
import heapq
class ChatBot:
    def __init__(self,name):
        self.name = name
        self.time = 0
        self.chats = []

    def __len__(self):
        return len(self.chats)

    def __getitem__(self,index):
        return self.chats[index][1]

    def __repr__(self):
        return f"chatbot with {self.chats} chats"

    def __str__(self):
        return f"chatbot system that interact with user that has {len(self.chats)} chats till now."

    def chat(self,chat):
        curr = self.time
        self.time += -1
        self.chats.append((curr,chat))

    def history(self):
        return [chat[1] for chat in self.chats]

    def recent(self,n=0):
        heapq.heapify(self.chats)
        if n == 0:
            return [self.chats[0][1]]
        most_recent = heapq.nsmallest(n,self.chats)
        return [chat[1] for chat in most_recent]
    def oldest(self,n = 1):
        most_oldest = heapq.nlargest(n,self.chats)
        return [chat[1] for chat in most_oldest ]

    def delete(self,index):
        return self.chats.pop(index)[1]
user = ChatBot("user")
print(user)
user.chat("what is Machine Learning?")
user.chat("what is AI?")
user.chat("what is Deep Learning?")
user.chat("why we care about tech?")
history = user.history()
print(history)
print(user)
print(user.recent(3))
print(user.delete(0))
print(user.history())
print(user.recent(2))
user.chat("I think machine learning is the future Engineer")
user.chat("I think you will fail in bad condition unless you focus on what matter for you right now")
user.chat("to be AI engineer or ML engineer, fullstack software development is the first journey you should go.")
print(user.history())
print(user.recent(),user.oldest())
print("\n"*4)
for chat in user:
    print(chat)
print(len(user))

    