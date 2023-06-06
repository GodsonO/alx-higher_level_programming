#include <stdlib.h>
#include "lists.h"
/**
  * insert_node - inserts a number into a sorted singly linked list.
  * @head: A pointer to the head of the linked list..
  * @number: number to be inserted.
  * Return: a pointer to the new node or NULL if it fails.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head; 
	listint_t *new_Node;

	new_Node = malloc(sizeof(listint_t));
	if (new_Node != NULL)
	{
		new_Node->n = number;
		if (node == NULL || (node)->n >= new_Node->n)
		{
			new_Node->next = node;
			node = new_Node;
			return (new_Node);
		}
		else
		{
			while (node->next != NULL && node->next->n < new_Node->n)
				node = node->next;
			new_Node->next = node->next;
			node->next = new_Node;
			return (new_Node);
		}
	}
	return (NULL);
}
