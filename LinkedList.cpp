// linked list và code cho nó

#include <bits/stdc++.h>

using namespace std;
struct node{
    int data;
    node *next;
};

// hàm để thêm node vào cuối danh sách liên kết

void append(node*& head, int value){
    node* newNode = new node;
    newNode->data=value;
    newNode->next=nullptr;
// nếu danh sách liên kết của ta rỗng thì gán head=newNode
    if (head==nullptr){
        head=newNode;
    }
    node* temp = head;
    while (temp->next != nullptr){
        temp=temp->next;
    }
    temp->next=newNode;
}

// hàm duyệt qua danh sách 
void printList(node *head){
    node *temp=head;
    while (temp!=nullptr){ //nếu ta dùng temp->next != nullptr thì ta sẽ không in ra được phần tử cuối cùng của danh sách liên kết
        cout << temp->data << " --> ";
        temp=temp->next;
    }
    cout << "nullptr" << endl;
}

// hàm chèn một node vào giữa danh sách liên kết đơn
void InsertAt(node*& head, int position, int value){
    node* newNode= new node;
    newNode->data=value;
    newNode->next=nullptr;
    if (position==0){
        newNode->next=head;
        head=newNode;
        return;
    }
    node *temp=head;
    int index=0;
//duyệt tới vị trí cần chèn
    while (temp!=nullptr && index<position-1){
        temp = temp -> next;
        index++;
    }
    if (temp==nullptr){
        cout << "Position out of range" << endl;
        delete newNode; // giải phóng bộ nhớ
        return;
    }
    newNode->next=temp->next;
    temp->next=newNode;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    node *head = new node;
    node *node2 = new node;
    node *node3 = new node;
    // gán dữ liệu:
    head->data = 1;
    head->next=node2;
    node2->data=2;
    node2->next=node3;
    node3->data=3;
    node3->next=nullptr;
    // duyệt và in ra danh sách 
    InsertAt(head,0,99);
    append(head,4);
    printList(head);
    return 0;
}

// output: 99 --> 1 --> 2 --> 3 --> 4 --> nullptr
