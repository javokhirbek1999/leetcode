class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) 
    {
        set<int> powerfull;
        
        for (size_t i = 1; i <= bound; i *= x)
        {
            for (size_t j = 1; i + j <= bound; j *= y)
            {
                powerfull.insert(i + j);
                
                if (y == 1)
                    break;
            }
            if (x == 1)
                break;
        }
        
        return vector(powerfull.begin(), powerfull.end());
    }
};
