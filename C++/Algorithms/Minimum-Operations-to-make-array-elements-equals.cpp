class Solution {
public:
    int minOperations(int n) {
        int mid = n/2;
        return mid*(mid+n%2);
    }
};
