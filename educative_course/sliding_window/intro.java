import java.utils.Arrays

class Solution {
    // Brute force
    public static double[] solve(int k, double[] nums){
        double[] result = new double[nums.length - k + 1];
        for(int i = 0; i <= nums.length; i++){

            if((i + k) > nums.length) break;
            double _sum = 0;
            for(int j = i; j < i + k; j++){
                   _sum += nums[j];
            }
            result[i] = _sum / k;
        }
        System.out.println("Result is ": Arrays.toString(result));
    } 
}

