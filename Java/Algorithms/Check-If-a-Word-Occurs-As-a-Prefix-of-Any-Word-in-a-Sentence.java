class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] rep = sentence.split(" "); 
        for(int i = 0; i<rep.length; i++){
            if(rep[i].startsWith(searchWord)){
                return i+1;
            }
        }
        return -1;
    }
}
