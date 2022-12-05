#include "lists.h"

/**
 * insert_node - adds a node at the beginning of a list
 * @head: pointer to a pointer to listint_t
 * @number: integer
 * Return: the address of the new element or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to listint_t
 */

void free_listint(listint_t *head)
{
	listint_t *dum;
	while (head)
	{
		dum = head->next;
		free(head);
		head = dum;
	}
}
