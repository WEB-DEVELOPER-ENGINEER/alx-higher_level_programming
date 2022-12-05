#include "lists.h"

/**
 * insert_node - adds a node at the beginning of a list
 * @head: pointer to a pointer to listint_t
 * @n: integer
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

/**
 * add_nodeint_end - adds a new node at the end of a list
 * @head: pointer to a pointer to listint_t
 * @n: integer
 * Return: the address of the new element, or NULL if it failed
 */

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *dum;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	dum = *head;
	while (dum->next)
	{
		dum = dum->next;
	}
	dum->next = new;
	return (new);
}
