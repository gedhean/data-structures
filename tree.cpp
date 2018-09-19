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
};

Node::Node(int value)
{
  this->value = value;
}

Node::Node(int value, Node *leftChild, Node *rightChild) {
  this->value = value;
  this->leftChild = leftChild;
  this->rightChild = rightChild;
}

class Tree
{
private:
  Node *root;     /* Root Tree Node */
public:
  Tree();
  bool empty();
};

Tree::Tree()
{
  this->root = nullptr;
}

bool Tree::empty() {
  return this->root == nullptr;
}

int main(int argc, char const *argv[])
{
  /* code */
  std::cout << "Hello Trees /o\\" << std::endl;

  return 0;
}
