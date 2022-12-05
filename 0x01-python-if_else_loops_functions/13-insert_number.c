#include "lists.h"

/**
 * insert_node - adds a node at the beginning of a list
 * @head: pointer to a pointer to listint_t
 * @number: integer
 * Return: the address of the new element or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->number = number;
	new->next = *head;
	*head = new;
	return (new);
}
