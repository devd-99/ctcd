public class LinkedList {
    Node head;

    static class Node {

        int value;
        Node next;

        Node (int v) {
            value = v;
        }
    }

    public static LinkedList InsertNodeAtEnd(LinkedList llist, int value){
        Node newNode = new Node(value);
        newNode.next = null;

        // Node currentNode = llist.head;

        if(llist.head == null){
            llist.head = newNode;
        }
        else {
            //else traverse until the last node
            Node last = llist.head;
            while(last.next != null){
                last = last.next;
            }
            last.next = newNode;
        }

        return llist;
    }

    public static LinkedList DeleteFirstNodeByValue(LinkedList llist, int data) {

        Node cVal = llist.head;
        if(cVal ==null){
            return null;
        }
        else if (cVal.value == data) {
            cVal.value = cVal.next.value;
            cVal.next = cVal.next.next;
            return llist;
        }
        else {
            while(cVal.next != null) {

                if (cVal.next.value == data) {
                    
                    cVal.next = cVal.next.next;
                    return llist;
                    
                }

                cVal = cVal.next;
            }
            return null;
        }

    }

    public static void printList(LinkedList list){

        Node currentNode = list.head;

        System.out.println("LinkedList: ");

        while(currentNode != null){
            System.out.print(currentNode.value+ ", ");
            currentNode = currentNode.next;
        }

    }

    public static void main(String args[]){
        LinkedList list = new LinkedList();
        list = InsertNodeAtEnd(list, 1);
        list = InsertNodeAtEnd(list, 2);
        list = InsertNodeAtEnd(list, 3);
        list = InsertNodeAtEnd(list, 4);
        list = InsertNodeAtEnd(list, 5);
        list = InsertNodeAtEnd(list, 6);
        list = DeleteFirstNodeByValue(list, 6);
        printList(list);
    }
}