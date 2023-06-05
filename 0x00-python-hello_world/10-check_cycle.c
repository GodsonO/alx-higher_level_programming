#include "lists.h"
/**
 * check_cycle - the program checks if a singly linked list
 * has a cycle in it
 * @list: linked list to check
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *beginning, *look_thru;

	beginning = list;
	look_thru = list;
	if (list == NULL)
		return 0;
	while (beginning != NULL && look_thru->next != NULL
		&& look_thru->next->next != NULL)
	{
		beginning = beginning->next;
		look_thru = look_thru->next->next;
		if (beginning == look_thru)
			return (1);
	}
	return (0);
}
