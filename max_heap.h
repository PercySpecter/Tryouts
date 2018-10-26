#include <stdio.h>
#include <stdlib.h>

#define LCHILD(x) 2 * x + 1
#define RCHILD(x) 2 * x + 2
#define PARENT(x) (x - 1) / 2

typedef struct node 
{
    int data;
} node;

typedef struct maxHeap 
{
    int size;
    node *elements;
} maxHeap;

maxHeap createMaxHeap(int size) 
{
    maxHeap hp;
    hp.size = 0;
    hp.elements = (node *)malloc(size * sizeof(node));
    return hp;
}

void swap(node *n1, node *n2) 
{
    node temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}

void heapify(maxHeap *hp, int i) 
{
    int largest = (LCHILD(i) < hp->size && hp->elements[LCHILD(i)].data > hp->elements[i].data) ? LCHILD(i) : i;
    if(RCHILD(i) < hp->size && hp->elements[RCHILD(i)].data > hp->elements[largest].data) 
	{
        largest = RCHILD(i);
    }
    if(largest != i) 
	{
        swap(&(hp->elements[i]), &(hp->elements[largest]));
        heapify(hp, largest);
    }
}

void insertNode(maxHeap *hp, int data) 
{
    node nd;
    nd.data = data;

    int i = (hp->size)++;
    while(i && nd.data > hp->elements[PARENT(i)].data) 
	{
        hp->elements[i] = hp->elements[PARENT(i)];
        i = PARENT(i);
    }
    hp->elements[i] = nd;
	//printf("Inserted %d\n\n" , data);
}

int deleteNode(maxHeap *hp , int *value) 
{
	if(hp->size == 0)
	{
		//printf("Heap is empty!!\n\n");
		return 0;
	}
	//printf("Deleting node %d\n\n", hp->elements[0].data);
	*value = hp->elements[0].data;
    hp->elements[0] = hp->elements[--(hp->size)];
    heapify(hp, 0);
	return 1;
}

void levelOrderTraversal(maxHeap *hp) 
{
    int i;
    for(i = 0; i < hp->size; i++)
		printf("%d ", hp->elements[i].data);
}

