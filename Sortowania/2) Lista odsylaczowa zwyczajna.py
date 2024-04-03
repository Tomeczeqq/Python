#Jest to prostsza mozliwosc deklarowania kopca jako kolejki
class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

#Wstawianie node'a przed pierwszym wiekszym elementem i zwrocenie head
def insert(lst,ele):
    if lst==None:
        return ele
    elif ele.value<=lst.value:
        ele.next=lst
        return ele
    pointer=lst
    while pointer.next is not None:
        if pointer.value<=ele.value and pointer.next.value>ele.value:       #warto jedna ostra i jedna nieostra nierownosc
            tmp=pointer.next
            pointer.next=ele
            ele.next=tmp
            return lst
        pointer=pointer.next
    pointer.next=ele
    return lst

#Usuniecie najwiekszego elementu z listy wraz ze zwracaniem maksymalnej wartosci i head
def removeMax(lst):
    head,max,prev=lst,lst,None
    while lst.next is not None:
        if lst.next.value > max.value:
            max=lst.next
            prev=lst
        lst=lst.next
    if prev is None:
        head=max.next
    else:
        prev.next=max.next
    max.next=None
    return (max,head)

#Sortowanie rosnaco listy odsylaczowej wraz ze zwroceniem tej listy
def sortf(lst):
    if lst is None or lst.next is None:
        return
    new_lst=None
    while lst is not None:
        temp,lst=removeMax(lst)
        new_lst=insert(new_lst,temp)
    return new_lst

#Wypisanie zawartosci listy odsylaczowej
def printf(lst):
    if lst is None:
        print(None)
    else:
        while True:
            print(lst.value,"-> ",end='')
            if lst.next is None:
                print(None)
                break
            lst=lst.next
    return

#Wstawianie na koniec listy odsylaczowej
def append(lst,ele):
    if lst is None:
        lst=ele
    else:
        pointer=lst
        while pointer.next is not None:
            pointer=pointer.next
        pointer.next=ele
    return

#Wypisanie dlugosci listy odsylaczowej
def lengthf(lst):
    if lst is None:
        return 0
    pointer=lst
    result=1
    while pointer.next is not None:
        pointer=pointer.next
        result+=1
    return result

#Zwracanie ostatniego elementu listy odsylaczowej
def lastf(lst):
    if lst is None:
        return None
    current=lst
    while current.next is not None:
        current=current.next
    return current.value

#Odwracanie zawartosci listy odsylaczowej wraz ze zwroceniem nowego heada
def reversef(lst):
    if lst is None or lst.next is None:
        return lst
    prev_node,curr_node,next_node=None,lst,None
    while curr_node is not None:
        next_node=curr_node.next
        curr_node.next=prev_node
        prev_node=curr_node
        curr_node=next_node
    return prev_node

#Przykladowe wykorzystanie funkcji przez tworzenie i operowanie na nowej liscie odsylaczowej
node1=Node(100)
node2=Node(999)
node3=Node(32)
node4=Node(20)
node1.next=node2
node2.next=node3
node3.next=node4
append(node1,Node(10))
head=insert(node1,Node(2137))
print("Dlugosc listy:",lengthf(head))
print("Zawartosc listy na poczatku:",end=' ')
printf(head)
head=sortf(head)
print("Zawartosc listy po posortowaniu:",end=' ')
printf(head)
head=reversef(head)
print("Zawartosc listy po odwroceniu:",end=' ')
printf(head)
print("Ostatni element listy to:",lastf(head))