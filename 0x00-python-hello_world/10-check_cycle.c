#include "lists.h"
/**
 * check_cycle - check if a linked list has a cycle
 * @h: head of the linked list
 *
 * Return: 1 if cycled and 0 otherwise
 */
int check_cycle(listint_t *h)
{
	const listint_t *head;
	const listint_t *current;

	current = h;
	head = h;

	while (current != NULL)
	{
		if (current->next == head)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
