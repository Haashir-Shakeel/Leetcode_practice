class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoList(list1,list2):       
    temp_node = ListNode()
    current_node = temp_node
        
    while list1  and list2 :
        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else: 
            current_node.next = list2
            list2=list2.next
        current_node = current_node.next
            
    if list1:
        current_node.next = list1
        list1 = list1.next
    if list2:
        current_node.next = list2
        list2 = list2.next
        
    return temp_node.next

## 2nd solution 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoList(list1,list2):
    head = ListNode()
    newlist = head
    
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    while list1 or list2:
        if list1.val < list2.val:
            newlist.next = list1

            list1 = list1.next

        else:
            newlist.next = list2
            
            list2 = list2.next
        newlist = newlist.next  

    if list1 or list2:
        newlist.next = list1 if list1 else list2
    
    return head.next
    