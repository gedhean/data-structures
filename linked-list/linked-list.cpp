#include <iostream>
using namespace std;

/* List node */
class Node
{
public:
	Node(int key);	/* Node constructor */
	int key;		/* Node value */
	Node *next;     /* Points to next Node */
};

Node::Node(int key) {
	this->key = key;
	this->next = nullptr;
}

/* Linked List (LL)*/
class LinkedList
{
public:
	LinkedList();				/* Linked List constructor */
	void push_back(int key)	;	/* Insert a Node at the end of the LL */
	void push_front(int key);	/* Insert a Node at the begin of the LL */
	void print();				/* DEBUG: print all LL elements */
private:
	int _size;					/* Number of elements in the LL	*/
	Node *head;					/* Points to the first LL element */
	Node *tail;					/* Points to the last LL element */
};

LinkedList::LinkedList() {
	this->_size = 0;
	this->head = nullptr;
}

void LinkedList::push_back(int key) {
	Node *node = new Node(key);   	// create a new Node MUST use 'new' keyword

	if (this->head == nullptr) {
		this->head = node; 			// point to new Node
		this->tail = node;
		this->_size += 1;
 	}
	else {
		this->tail->next = node;
		this->tail = node;
		this->_size += 1;
	}
}

void LinkedList::push_front(int key) {
	Node *node = new Node(key);   	// create a new Node MUST use 'new' keyword

	if (this->head == nullptr) {
		this->head = node; 			// point to new Node
		this->tail = node;
		this->_size += 1;
 	}
	else {
		node->next = this->head;
		this->head = node;
		this->_size += 1;
	}
}

void LinkedList::print() {
	Node *currentNodePtr = this->head;

	while (currentNodePtr != nullptr) {
		cout << "Element: " << currentNodePtr->key;
		cout << " Nexy Ptr: " <<  currentNodePtr->next << endl;
		currentNodePtr = currentNodePtr->next;
	}
}


int main() {
	LinkedList ll;

	ll.push_back(9);
	ll.push_back(8);
	ll.push_back(7);
	ll.push_back(6);
	ll.push_front(10);
	ll.push_front(11);

	ll.print();

	return 0;
}
