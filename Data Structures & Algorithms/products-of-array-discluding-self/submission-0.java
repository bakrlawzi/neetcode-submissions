class Solution {
    public int[] productExceptSelf(int[] nums) {
          int[] a = new int[nums.length];
         int i=0;int k=0;int sum=1;
         while(i<nums.length){
             sum=1;
             while(k!=i){
                 sum*=nums[k];
                 k++;
             }
             k=0;
             int j = 0;
             if(i<nums.length-1){
                 j=i+1;
                 while(j<nums.length){
                 sum*=nums[j];
                 j++;
             }
             }
             a[i] = sum;
             i++;
         }
         return a;
    }
}  
