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
	int size();					/* Return the number of LL elements */
	bool empty();				/* Return true if LL is empty or false otherwise*/
	int value_at(int n);		/* Return the nth value in the LL (start at 1 for first) */
	int pop_front();			/* Remove first element and return its value */
	int pop_back();				/* Remove last element and return its value */
	int front();				/* Get a value at the front of the LL */
	int back();				/* Get a value at the back of the LL */
	void print();				/* DEBUG: print all LL elements */

private:
	Node *head;					/* Points to the first LL element */
	Node *tail;					/* Points to the last LL element */
};

LinkedList::LinkedList() {
	this->head = nullptr;
}

void LinkedList::push_back(int key) {
	Node *node = new Node(key);   		/* create a new Node MUST use 'new' keyword */

	if (this->head == nullptr) {
		this->head = node; 				/* point to new Node */
		this->tail = node;
 	}
	else {
		this->tail->next = node;
		this->tail = node;
	}
}

void LinkedList::push_front(int key) {
	Node *node = new Node(key);   	// create a new Node MUST use 'new' keyword

	if (this->head == nullptr) {
		this->head = node; 			// point to new Node
		this->tail = node;
 	}
	else {
		node->next = this->head;
		this->head = node;
	}
}

int LinkedList::size() {
	int size = 0;
	Node *currentNodePtr = this->head;

	while(currentNodePtr) {
		size++;
		currentNodePtr = currentNodePtr->next;
	}

	return size;
}

bool LinkedList::empty() {
	return this->head == nullptr;
}

int LinkedList::value_at(int n) {
	if(this->size() < n || n < 1) {
		cerr << "LinkedList size is less then n or n is negative";
		exit(1);
	}

	int i = 1;
	Node *currentNodePtr = this->head;

	while (i < n) {
		currentNodePtr = currentNodePtr->next;
		i++;
	}

	return currentNodePtr->key;
}

int LinkedList::pop_front() {
	if (this->empty()) {
		cerr << "Can not pop front. List is empty" << endl;
		exit(1);
	}

	Node *currentNodePtr = this->head;

	this->head = this->head->next;

	return currentNodePtr->key; 
}

int LinkedList::pop_back() {
	if (this->empty()) {
		cerr << "Can not pop back. List is empty" << endl;
		exit(1);
	}

	Node *prevNodePtr = this->head; 
	Node *currentNodePtr = this->head->next;				

	while (currentNodePtr) {
		// cout << "Current " << prevNodePtr << ": " << prevNodePtr->key << " - Next " << currentNodePtr << ": " << currentNodePtr->key << endl;
		
		if (currentNodePtr->next == nullptr) break; /* currentNodePtr points to lest element now */
		prevNodePtr = currentNodePtr;
		currentNodePtr = currentNodePtr->next;
	}

	this->tail = prevNodePtr;
	prevNodePtr->next = nullptr; 					/* Points to penultimate element*/

	return currentNodePtr->key;						/* Points to last element*/
}

int LinkedList::front() {
	if (this->empty()) {
		cerr << "Can not get item at front of list.List is empty" << endl;
		exit(1);
	}
	return this->head->key;
}

int LinkedList::back() {
	if (this->empty()) {
		cerr << "Can not get item at back of list.List is empty" << endl;
		exit(1);
	}
	return this->tail->key;
}

void LinkedList::print() {
	Node *currentNodePtr = this->head;

	cout << "---------------------------------------------" << endl;

	while (currentNodePtr != nullptr) {
		cout << "Element: " << currentNodePtr->key;
		cout << " Nexy Ptr: " <<  currentNodePtr->next << endl;
		currentNodePtr = currentNodePtr->next;
	}

	cout << "2th element: " << this->value_at(2) << endl;
	cout << "List size: " << this->size() << endl;

	cout << "Front: " << this->front() << endl;
	cout << "Back: " << this->back() << endl;
}


int main() {
	LinkedList ll;

	ll.push_back(9);
	ll.push_back(8);
	ll.push_back(7);
	ll.push_front(10);
	ll.push_front(11);

	ll.print();

	cout << "pop_front: " << ll.pop_front() << endl;

	ll.print();

	cout << "pop_back: " << ll.pop_back() << endl;

	ll.print();

	return 0;
}
