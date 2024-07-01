import static java.lang.Math.abs;
class Solution {
    public static int findPermutationDifference(String s, String t) {
        int result = 0;
        for(int i = 0; i < s.length(); i++) {
            result = result + abs(i - t.indexOf(s.charAt(i)));
        }
        return result;
    }
}