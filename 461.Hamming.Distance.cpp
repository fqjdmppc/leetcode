#include <bitset>
class Solution {
public:
    int hammingDistance(int x, int y) {
        bitset<32> ret(x^y);
        return ret.count();
    }
};