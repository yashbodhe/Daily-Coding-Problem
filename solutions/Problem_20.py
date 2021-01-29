class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
def createLinkedList(a):
    head=Node(0)
    itr=head
    for x in a:
        itr.next=Node(x)
        itr=itr.next
    return head.next

def reverse(head):
    itr=head
    prev=None
    next=None
    while itr:
        next=itr.next
        itr.next=prev
        prev=itr
        itr=next
    return prev
def findIntersectingNode(h1,h2):
    h1=reverse(h1)
    h2=reverse(h2)
    if (not h1) or (not h2) or h1.data!=h2.data:
        return -1
    while h1.next and h2.next:
        if h1.next.data!=h2.next.data:
            return h1.data
        h1=h1.next
        h2=h2.next
    return h1.data
if __name__=="__main__":
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    head1=createLinkedList(a1)
    head2=createLinkedList(a2)
    print(findIntersectingNode(head1,head2))