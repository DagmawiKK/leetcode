import java.util.List;
import java.util.ArrayList;
class Solution {
    public static int numJewelsInStones(String jewels, String stones) {
        int result = 0;
        List<String> listJ = new ArrayList<String>(Arrays.asList(jewels.split("")));
        List<String> listS = new ArrayList<String>(Arrays.asList(stones.split("")));
        int i = 0;
        while(i < listJ.size()) {
            while(listS.contains(listJ.get(i))) {
                listS.remove(listJ.get(i));
                result++;
            }
            i++;
        }
        return result;
    }
}