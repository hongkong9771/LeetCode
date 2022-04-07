class Solution {
    public int getSum(int a, int b) {
        // sum用来求和，carry用来进位
        int sum, carry;
        while (b!=0){       // 当还有进位时，继续下面操作
            sum = a ^ b;    // 异或 用于求和
            carry = (a & b) << 1;  // 与 用于进位
            a = sum;
            b = carry;
        }
        return a;

    }
}