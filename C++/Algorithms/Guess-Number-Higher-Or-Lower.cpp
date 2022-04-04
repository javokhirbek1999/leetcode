/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        
        long long int low = 1;
        long long int high = n;
        
        while (low <= high) {
            
            long long int mid = (low+high)/2;
            long long int ans = guess(mid);
            
            if (ans == 0) {
                return mid;
            }
            
            if (ans == -1) {
                high = mid-1;
            }
            
            if (ans == 1) {
                low = mid+1;
            }
        }
        return -1;
    }
};
