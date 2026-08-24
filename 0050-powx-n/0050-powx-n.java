class Solution {
    public double myPow(double x, int n) {
        long power = n;

        if (power < 0) {
            x = 1 / x;
            power = -power;
        }

        if (power == 0) {
            return 1;
        }

        double half = myPow(x, (int)(power / 2));

        if (power % 2 == 0) {
            return half * half;
        }

        return x * half * half;
    }
}