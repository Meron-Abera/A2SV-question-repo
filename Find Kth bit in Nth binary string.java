class Solution {
    public char findKthBit(int n, int k) {
     
        if (n == 1 && k == 1) return '0';
        if (n == 2 && k == 2) return '1';
        if (n == 2 && k == 3) return '1';
        int len = (int) (Math.pow(2, n)) - 1;
        if (k == len / 2 + 1) return '1';
        if (k <= len / 2) return findKthBit(n - 1, k);
        int nk = len - k + 1;
        return findKthBit(n - 1, nk) - '0' == 0 ? '1' : '0';
    }
}
