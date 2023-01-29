class MyLinkedList {
    class Node {
        public int val;
        public Node next;
        public Node prev;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.prev = null;
        }
    }

    private Node head;
    private Node tail;

    public MyLinkedList() {
        head = new Node(-1);
        tail = new Node(-1);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int index) {
        if(index < 0)
            return -1;

        int i = 0;
        Node p = head;
        for(; i < index && p.next != tail; i++) {
            p = p.next;
        }

        return p.next.val;
    }

    public void addAtHead(int val) {
        Node n = new Node(val);
        n.next = head.next;
        n.prev = head;
        head.next = n;
        n.next.prev = n;
    }

    public void addAtTail(int val) {
        Node n = new Node(val);
        n.next = tail;
        n.prev = tail.prev;
        tail.prev = n;
        n.prev.next = n;
    }

    public void addAtIndex(int index, int val) {
        int i = 0;
        Node p = head;
        for(; i < index && p.next != tail; i++) {
            p = p.next;
        }

        if(i != index)
            return;

        Node n = new Node(val);
        n.prev = p;
        n.next = p.next;
        p.next = n;
        n.next.prev = n;
    }

    public void deleteAtIndex(int index) {
        int i = 0;
        Node p = head;
        for(; i < index && p.next != tail; i++) {
            p = p.next;
        }

        if(p.next == tail)
            return;

        p.next = p.next.next;
        p.next.prev = p;
    }
}
