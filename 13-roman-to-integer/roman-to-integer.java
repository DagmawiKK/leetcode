import java.util.HashMap;
class Solution {
   public static int romanToInt(String s) {
        HashMap<Character, Integer>rTon = new HashMap<Character, Integer>();
        rTon.put('I', 1);
        rTon.put('V', 5);
        rTon.put('X', 10);
        rTon.put('L', 50);
        rTon.put('C', 100);
        rTon.put('D', 500);
        rTon.put('M', 1000);
        int result = 0;
        for(int i = 0; i < s.length(); i++) {
            if(i < s.length() - 1){
                if(rTon.get(s.charAt(i)) >= rTon.get(s.charAt(i+1))){
                    result = result + (rTon.get(s.charAt(i)));
                }
                else {
                    result = result + (rTon.get(s.charAt(i+1)) - rTon.get(s.charAt(i)));
                    i++;
                }
            }
            else {
                result = result + (rTon.get(s.charAt(i)));
            }

        }
        return result;
    }
}