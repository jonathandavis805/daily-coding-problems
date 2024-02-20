from daily_coding_problems.linked_list import LinkedList


def test_reverse_linked_list():
    linked_list = LinkedList()
    for i in range(0, 10):
        linked_list.insertAtEnd(i)
    linked_list.reverse_in_place()
    i = 9
    node = linked_list.head
    while node.next:
        print(node.data)
        print(i)
        assert node.data == i
        node = node.next
        i -= 1
