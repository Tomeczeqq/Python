#Jest to mozliwosc deklarowania kopca jako kolejki opierajaca sie na klasie LinkedList
class LinkedListNode:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    #Wstawianie node'a przed pierwszym wiekszym elementem i zwrocenie head
    def insert(self,value):
        lst=self.head
        ele=LinkedListNode(value)
        if lst is None:
            self.head=ele
            return self.head
        elif ele.value<=lst.value:
            ele.next=lst
            self.head=ele
            return self.head
        pointer=lst
        while pointer.next is not None:
            if pointer.value<=ele.value and pointer.next.value>ele.value:
                tmp=pointer.next
                pointer.next=ele
                ele.next=tmp
                return self.head
            pointer=pointer.next
        pointer.next=ele
        return self.head

    #Usuniecie najwiekszego elementu z listy i zwrocenie jego wartosci
    def removeMax(self):
        currentNode,maxNode,previousNode=self.head,self.head,None
        while currentNode.next is not None:
            if currentNode.next.value>maxNode.value:
                maxNode=currentNode.next
                previousNode=currentNode
            currentNode=currentNode.next
        if previousNode is None:
            self.head=maxNode.next
        else:
            previousNode.next=maxNode.next
        maxNode.next=None
        return maxNode.value

    #Sortowanie rosnaco listy odsylaczowej
    def sortf(self):
        if self.head is None or self.head.next is None:
            return
        new_lst=LinkedList()
        while self.head is not None:
            max_node=self.removeMax()
            new_lst.insert(max_node)
        self.head=new_lst.head
        return new_lst

    #Wypisanie zawartosci listy odsylaczowej
    def printf(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.value,"-> ",end='')
            currentNode=currentNode.next
        print(None)

    #Wstawianie na koniec listy odsylaczowej
    def append(self,value):
        ele=LinkedListNode(value)
        if self.head is None:
            self.head=ele
            return
        currentNode=self.head
        while currentNode.next is not None:
            currentNode=currentNode.next
        currentNode.next=ele

    #Wypisanie dlugosci listy odsylaczowej
    def lengthf(self):
        currentNode=self.head
        if self.head is None:
             return 0
        result=1
        while currentNode.next is not None:
            currentNode=currentNode.next
            result+=1
        return result

    #Zwracanie ostatniego elementu listy odsylaczowej
    def lastf(self):
        if self.head is None:
            return None
        pointer=self.head
        while pointer.next is not None:
            pointer=pointer.next
        return pointer.value

    #Odwracanie zawartosci listy odsylaczowej
    def reversef(self):
        lst=self.head
        if lst is None or lst.next is None:
            return lst
        prev_node,curr_node,next_node=None,lst,None
        while curr_node is not None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        self.head=prev_node
        return prev_node

#Przykladowe wykorzystanie funkcji przez tworzenie i operowanie na nowej liscie odsylaczowej
LL=LinkedList()
LL.append(100)
LL.append(999)
LL.append(32)
LL.append(20)
LL.append(10)
LL.insert(2137)
print("Dlugosc listy:",LL.lengthf())
print("Zawartosc listy na poczatku:",end=' ')
LL.printf()
LL.sortf()
print("Zawartosc listy po posortowaniu:",end=' ')
LL.printf()
LL.reversef()
print("Zawartosc listy po odwroceniu:",end=' ')
LL.printf()
print("Ostatni element listy to:",LL.lastf())