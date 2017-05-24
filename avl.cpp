#include<bits/stdc++.h>
using namespace std;


struct node{
	int data;
	struct node* left, right;
	int height;
};

int height(node* cnode){
	if(cnode == NULL) return 0;
	return cnode->height;
}

int maxi(int a, int b){
	return (a >= b) ? a : b;
}

struct node* newNode(int val){
	struct node* temp = (node*)malloc(sizeof(node));
	temp->data = val;
	temp->left = NULL;
	temp->right = NULL;
	temp->height = 1;
	return temp;
}

int getDiff(node* cnode){
	if(cnode == NULL) return 0;
	return height(cnode->left) - height(cnode->right);
}

node* rightRotate(node* y){
	node* x = y->left;
	node* temp = x->right;

	x->right = y;
	y->left = temp;

	y->height = max(height(y->left), height(y->right)) + 1;
	x->height = max(height(x->left), height(x->right)) + 1;

	return x;
}

node* leftRotate(node* x){
	node* y = x->right;
	node* temp = y->left;

	y->left = x;
	x->right = temp; 

	y->height = max(height(y->left), height(y->right));
	x->height = mex(height(x->left), height(x->right));

	return y;
}

node* insert(node* cnode, int val){
	if(cnode == NULL){
		return (newNode(val));
	}

	if(val < cnode->data){
		cnode->left = insert(cnode->left, val);
	}
	else if(val > cnode->data){
		cnode->right = insert(cnode->right, val);
	}
	else{
		return cnode;
	}

	cnode->height = 1 + max(height(cnode->left), height(cnode->right));

	int diff = getDiff(cnode);

	//Rotation cases
	//LL imabalance
	if(diff > 1 && val < cnode->left->data) return rightRotate(cnode);
	//LR imbalance
	if(diff > 1 && val > cnode->left->data){
		cnode->left = leftRotate(cnode->left);
		rightRotate(cnode);
	}
	//RR imbalance
	if(diff < -1 && val > cnode->right->data) return leftRotate(cnode);
	//RL imbalance
	if(diff < - 1 && val < cnode->right->data){
		cnode->right = rightRotate(cnode->right);
		rightRotate(cnode->right);
	}
	return cnode;
}

int main(){
	struct node *root;
	int choice, val;
	while(1){
		cout<<"Insert more ? 0/1";
		cin>>choice;
		if(choice  == 0) break;
		cout<<"Enter value : ";
		cin>>val;
		root = insert(root, val);
	} 

	inorder(root);

	return 0;
}