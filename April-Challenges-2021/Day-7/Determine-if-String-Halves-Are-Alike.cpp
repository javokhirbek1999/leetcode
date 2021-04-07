class Solution {
public:
    bool isvowel(char a){
        
         if(a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
             return 1;
        
         return 0;
        
    }
    bool halvesAreAlike(string s) {
        
         int cnt1 = 0, cnt2 = 0,n = s.size();
        
         for(int i = 0; i < n; i++){
             
             if(isvowel( tolower(s[i]) ) && i < n/2) cnt1++;
             else if(isvowel(tolower(s[i]))) cnt2++;
             
         }
        
         return cnt1 == cnt2;
        
    }
};
