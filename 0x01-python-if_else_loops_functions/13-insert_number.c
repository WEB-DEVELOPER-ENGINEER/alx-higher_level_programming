#include "lists.h"

/**
 * insert_node - adds a node at the beginning of a list
 * @head: pointer to a pointer to listint_t
 * @n: integer
 * Return: the address of the new element or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (n < < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < n)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
