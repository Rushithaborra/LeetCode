/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int* largestValues(struct TreeNode* root, int* returnSize) {

    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }

    struct TreeNode* queue[10000];
    int front = 0, rear = 0;

    queue[rear++] = root;

    int* result = (int*)malloc(sizeof(int) * 10000);
    int size = 0;

    while (front < rear) {

        int levelSize = rear - front;
        int maxValue = -2147483648;

        for (int i = 0; i < levelSize; i++) {

            struct TreeNode* node = queue[front++];

            if (node->val > maxValue) {
                maxValue = node->val;
            }

            if (node->left) {
                queue[rear++] = node->left;
            }

            if (node->right) {
                queue[rear++] = node->right;
            }
        }

        result[size++] = maxValue;
    }

    *returnSize = size;
    return result;
}