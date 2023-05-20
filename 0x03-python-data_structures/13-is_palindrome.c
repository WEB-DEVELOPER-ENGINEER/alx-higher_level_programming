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
	listint_t *h, *f_half, *s_half, *temp = NULL;
	int i = 0, j, c = 0;

	if (head && *head)
	{
		h = *head;
		if (!h->next)
			return (1);
		while (h->next)
		{
			h = h->next;
			i++;
		}
		h = *head;
		if ((i + 1) % 2 == 0)
		{
			j = i / 2;
			f_half = *head;
			for (s_half = *head; c < j; c++)
			{
				s_half = s_half->next;
				f_half = f_half->next;
			}
			s_half = s_half->next;
			f_half->next = NULL;
			f_half = *head;
			while(f_half)
			{
				h = f_half->next;
				f_half->next = temp;
				temp = f_half;
				f_half = h;
			}
			f_half = temp;
			while (f_half && s_half)
			{
				if (f_half->n != s_half->n)
					return (0);
				f_half = f_half->next;
				s_half = s_half->next;
			}
			return (1);
		}
		else
                {
                        j = (i) / 2;
                        f_half = *head;
                        for (s_half = *head; c < j - 1; c++)
                        {
                                s_half = s_half->next;
                                f_half = f_half->next;
                        }
                        s_half = s_half->next->next;
                        f_half->next = NULL;
                        f_half = *head;
                        while(f_half)
                        {
                                h = f_half->next;
                                f_half->next = temp;
                                temp = f_half;
                                f_half = h;
                        }
                        f_half = temp;
                        while (f_half && s_half)
                        {
				if (f_half->n != s_half->n)
                                        return (0);
                                f_half = f_half->next;
                                s_half = s_half->next;
                        }
                        return (1);
		}
	}
	return (1);
}
