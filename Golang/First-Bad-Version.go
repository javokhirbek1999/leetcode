/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    low := 1
    high := n
    
    badVersion := -1
    for low <= high {
        mid := (low+high)/2
        
        version := mid
        
        if isBadVersion(version) {
            badVersion = mid
        }
        
        if isBadVersion(version) {
            high = mid-1
        } else {
            low = mid + 1
        }
    }
    
    return badVersion
}
