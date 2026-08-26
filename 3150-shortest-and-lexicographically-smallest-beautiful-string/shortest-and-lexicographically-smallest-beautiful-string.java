class Solution {
    public String shortestBeautifulSubstring(String s, int k) {

        int n = s.length();

        String answer = "";

        int left = 0;
        int count = 0;

        for (int right = 0; right < n; right++) {

            if (s.charAt(right) == '1') {
                count++;
            }
            if (count == k) {
                while (s.charAt(left) == '0') {
                    left++;
                }

                String current = s.substring(left, right + 1);

                if (answer.equals("")) {
                    answer = current;
                }
                else if (current.length() < answer.length()) {
                    answer = current;
                }
                else if (current.length() == answer.length()
                        && current.compareTo(answer) < 0) {
                    answer = current;
                }
                left++;
                count--;
            }
        }

        return answer;
    }
}