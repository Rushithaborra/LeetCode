/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node* copyRandomList(struct Node* head) {
    if (head == NULL) return NULL;

    // Create array to store original and copied nodes
    struct Node *orig[1000], *copy[1000];
    int count = 0;

    struct Node *temp = head;

    // First pass: create copy nodes
    while (temp != NULL) {
        orig[count] = temp;

        copy[count] = (struct Node*)malloc(sizeof(struct Node));
        copy[count]->val = temp->val;
        copy[count]->next = NULL;
        copy[count]->random = NULL;

        count++;
        temp = temp->next;
    }

    // Connect next pointers
    for (int i = 0; i < count - 1; i++) {
        copy[i]->next = copy[i + 1];
    }

    // Connect random pointers
    for (int i = 0; i < count; i++) {
        if (orig[i]->random != NULL) {
            for (int j = 0; j < count; j++) {
                if (orig[j] == orig[i]->random) {
                    copy[i]->random = copy[j];
                    break;
                }
            }
        }
    }

    return copy[0];
}