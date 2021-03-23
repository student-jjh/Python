class Node:

    def __init__(self,data,next):
        self.data= data
        self.next= next

class LinkedList:
    def __init__(self):
        self.no=0
        self.head=None
        self.current=None

    def __len__(self):
        return self.no
    
    def search(self,data):
        cnt=0
        ptr=self.head
        while ptr is not None:
            if ptr.data==data:
                self.current=ptr
                return cnt

            cnt+=1
            ptr=ptr.next
        return -1
    
    def __contains__(self,data):
        return self.search(data)>=0
    
    def add_first(self,data):

        ptr=self.head
        self.head=self.current=Node(data,ptr)
        self.no+=1

    def add_last(self,data):
        if self.head is None:
            self.add_first(data)
        else:
            ptr=self.head
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=self.current=Node(data,None)
            self.no+=1
    
    def remove_first(self):
        if self.head is not None:
            self.head=self.current=self.head.next

        self.no-=1

    def remove_last(self):
        if self.no is 1:
            self.remove_first()
        else:
            ptr=self.head
            pre=self.head
        
        while ptr.next is not None:
            pre=ptr
            ptr=ptr.next

        pre.next=None
        self.current=pre
        self.no-=1