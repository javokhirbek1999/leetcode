class Solution {
    public boolean halvesAreAlike(String s) {
        char[] a = new char[s.length()/2];
        char[] b = new char[s.length()/2];
        String d = "aeiouAEIOU";
        for(int i = 0; i<s.length()/2; i++){
            a[i] = s.charAt(i);
        }
        int j = s.length()/2;
        for(int i = 0; i<s.length()/2; i++,j++){
            b[i] = s.charAt(j);
        }
        int ac = 0;
        int bc = 0;
        for(char c:a){
            if(d.contains(String.valueOf(c))){
                ac++; 
            } 
        }
        for(char c:b){
            if(d.contains(String.valueOf(c))){
                bc++; 
            } 
        }
        return ac==bc;
    }
}
