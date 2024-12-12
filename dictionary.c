#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in the hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Word count
unsigned int count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to get an index
    int index = hash(word);

    // Traverse the linked list at that index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Case-insensitive comparison
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + tolower(c);
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }

    // Buffer to hold each word
    char word[LENGTH + 1];

    // Read words from the file
    while (fscanf(source, "%s", word) != EOF)
    {
        // Allocate memory for a new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(source);
            return false;
        }

        // Copy the word into the node
        strcpy(n->word, word);
        n->next = NULL;

        // Hash the word to find the correct index
        int index = hash(word);

        // Insert the node into the hash table
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }

        // Increment word count
        count++;
    }

    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Traverse each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            // Free nodes in the linked list
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
