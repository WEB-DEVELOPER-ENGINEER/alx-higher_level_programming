#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp1;
	listint_t *temp2;
	listint_t *temp3;

	if (head && *head)
	{
		temp1 = *head;
		while (temp1->next)
		{
			temp1 = temp1->next;
		}
		for (temp2 = *head; temp2 != temp1 && temp2->next; temp2 = temp2->next)
		{
			if (temp2->n != temp1->n)
				return (0);
			for (temp3 = *head; temp3->next != temp1; temp3 = temp3->next)
				;
			temp1 = temp3;
		}
		return (1);
	}
	return (0);
}
