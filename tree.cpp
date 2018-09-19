/* Binary Tree Data Structure implementation */
#include <iostream>
// Tree Node 
class Node
{
private:
  int value;          /* Value store at this Node */
  Node *leftChild;    /* Left Node Child */
  Node *rightChild;   /* Right Node Child */
public:
  Node(int value);
  Node(int value, Node *leftChild, Node *rightChild);
  int getValue();                 /* Node stored value */
  void setLeftChild(int value);   /* Set Node left child  */
  void setRightChild(int value);  /* Set Node right child  */
  Node* getLeftChild();
  Node* getRightChild();
};

Node::Node(int value)
{
  this->value = value;
  this->leftChild = nullptr;
  this->rightChild = nullptr;
}

Node::Node(int value, Node *leftChild, Node *rightChild) {
  this->value = value;
  this->leftChild = leftChild;
  this->rightChild = rightChild;
}

int Node::getValue() {
  return this->value;
}

void Node::setLeftChild(int value) {
  this->leftChild = new Node(value);
}
void Node::setRightChild(int value) {
  this->rightChild = new Node(value);
}

Node* Node::getLeftChild() {
  return this->leftChild;
}
Node* Node::getRightChild() {
  return this->rightChild;
}

class Tree
{
private:
  Node *root;     /* Root Tree Node */
public:
  Tree();
  Tree(Node* n);
  bool empty(); 
  void print();
  Node* getRoot() { return this->root; };
};

Tree::Tree()
{
  this->root = nullptr;
}

Tree::Tree(Node* n) {
  this->root = n;
}

bool Tree::empty() {
  return this->root == nullptr;
}

void printTree(Node* T) {
  if (T == nullptr) {
    return;
  }
  std::cout << "Value: " << T->getValue() << std::endl;
  printTree(T->getLeftChild());
  printTree(T->getRightChild());
}

void Tree::print() {
  printTree(this->root);
}

int main(int argc, char const *argv[])
{
  std::cout << "Hello Trees /o\\" << std::endl;
  /* code */
  Tree T(new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3)));

  T.print();
  std::cout << "Tree is empty: " << T.empty() << std::endl;

  return 0;
}
