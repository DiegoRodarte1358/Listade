class NodoDoble:
    def __init__(self,value,siguiente,previo):
        self.data = value
        self.next = siguiente
        self.prev = previo
    
class ListaDoblementeEnlazada:
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size
    def insert(self,value):
        if self.__size == 0:
            nuevo = NodoDoble(value,self.__tail,self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1

    def transversal(self):
        curr_Node = self.__head.next
        while curr_Node.next != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.next
        print("")

    def reverse_transversal(self):
        curr_Node = self.__tail.prev
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.prev
        print("")
