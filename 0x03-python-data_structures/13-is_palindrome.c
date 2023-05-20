#include <stdint.h>
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
	int arr[1000];
	listint_t *current = *head;
	int i = 0;
	int left = 0;
	int right;

	while (current)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	right = i - 1;
	while (left < right)
	{
		if (arr[left] != arr[right])
			return (0);
		left++;
		right--;
	}
	return (1);
}
