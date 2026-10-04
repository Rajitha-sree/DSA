class Solution {
    public int countDigits(int num) {
        int temp = num;
        int c = 0;
        while(num>0){
            int r = num%10;
            if(temp%r==0)
            {
                c+=1;
            }
            num=num/10;
        }
        return c;
    }
}