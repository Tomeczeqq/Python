#Deklaracje listy jednokierunkowej
class Node:
    def __init__(self):             #konstruktor
        self.val=None
        self.next=None

class Node2:
    def __init__(self,x):
        self.val=x
        self.next=None

#Deklaracja listy dwukierunkowej
class Node3:
    def __init__(self):
        self.val=None
        self.next=None
        self.prev=None

#Deklaracja drzewa binarnego
class Node4:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None
        #self.parent=None