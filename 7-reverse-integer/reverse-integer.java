class Solution {
    public static int reverse(int x) {
        long y = 0L;
        boolean isNegative = x < 0;

        if (isNegative) {
            x = -x;
        }

        y = worker(x);

        if (isNegative) {
            y = -y;
        }
        if (y < Integer.MIN_VALUE || y > Integer.MAX_VALUE) {
            return 0;
        } else {
            return (int) y;
        }
    }

    public static long worker(int x) {
        long reversed = 0L;

        while (x != 0) {
            int digit = x % 10; 
            reversed = reversed * 10 + digit;
            x /= 10;
        }

        return reversed;
    }
}