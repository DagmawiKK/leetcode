import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public static int numJewelsInStones(String jewels, String stones) {
        long matches = 0;
        for(int i = 0; i < jewels.length(); i++) {
            Pattern pattern = Pattern.compile(String.valueOf(jewels.charAt(i)));
            Matcher matcher = pattern.matcher(stones);
            matches = matches + matcher.results().count();
        }
        return (int) matches;
    }
}