from daily_coding_problems.linked_list import LinkedList, merge_sorted, merge_2_sorted

def test_merge_2_lists():
    list_1 = LinkedList()
    list_2 = LinkedList()
    for i in range(0,10,2):
        list_1.insertAtEnd(i)
        list_2.insertAtEnd(i + 1)
    result = merge_2_sorted(list_1, list_2)
    result.visualize()
    assert result.sizeOfLL() == 10
    assert False
    

def test_sort_linked_lists():
    l_lists: list[LinkedList] = []
    quantity = 5
    length = 20
    for _ in range(quantity):
        l_list = LinkedList()
        for i in range(length):
            l_list.insertAtEnd(i)
            # l_list.visualize()
        l_lists.append(l_list)
    
    sorted_lists = merge_sorted(l_lists)
    sorted_lists.visualize()
    assert sorted_lists.sizeOfLL() == quantity * length 