import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public static double[] solve(int k, double[] nums){
        double[] result = new double[nums.length];
        for(int i = 0; i <= nums.length - k; i++){
            double sum = 0;
           for(int j = i; j < i + k; j++){
              sum += nums[j];
           }
           result[i] = sum;
        }
        System.out.println(Arrays.toString(result));
    }
}

class Main {
    public static void main(String args[]){
        Solution.solve(5, new int[]{2,4,5,6,7,8,9,2});
    }
}

