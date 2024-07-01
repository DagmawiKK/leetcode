import java.util.List;
import java.util.ArrayList;
class Solution {
    public static int numJewelsInStones(String jewels, String stones) {
        int result = 0;
        List<String> listJ = new ArrayList<String>(Arrays.asList(jewels.split("")));
        System.out.println(listJ);
        List<String> listS = new ArrayList<String>(Arrays.asList(stones.split("")));
        System.out.println(listS);
        int i = 0;
        while(i < listJ.size()) {
            while(listS.contains(listJ.get(i))) {
                System.out.println(listS.contains(listJ.get(i)));
                listS.remove(listJ.get(i));
                System.out.println(listS);
                result++;
            }
            i++;
        }
        return result;
    }
}