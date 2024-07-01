import java.util.List;
import java.util.ArrayList;
class Solution {
    public static int numJewelsInStones(String jewels, String stones) {
        int result = 0;
        List<String> listJ = new ArrayList<>(Arrays.asList(jewels.split("")));
        List<String> listS = new ArrayList<>(Arrays.asList(stones.split("")));

        for (String jewel : listJ) {
            while (listS.contains(jewel)) {
                listS.remove(jewel);
                result++;
            }
        }
        return result;
    }
}