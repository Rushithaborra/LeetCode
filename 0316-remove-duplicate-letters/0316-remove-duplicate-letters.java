class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        boolean[] used = new boolean[26];

        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        StringBuilder stack = new StringBuilder();

        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            count[idx]--;

            if (used[idx]) {
                continue;
            }

            while (stack.length() > 0 &&
                   stack.charAt(stack.length() - 1) > c &&
                   count[stack.charAt(stack.length() - 1) - 'a'] > 0) {

                char removed = stack.charAt(stack.length() - 1);
                stack.deleteCharAt(stack.length() - 1);
                used[removed - 'a'] = false;
            }

            stack.append(c);
            used[idx] = true;
        }

        return stack.toString();
    }
}