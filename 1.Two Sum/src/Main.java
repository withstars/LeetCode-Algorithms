/**
 * Created with IntelliJ IDEA.
 * Description:
 * User: withstars
 * Date: 2018-04-02
 * Time: 16:56
 * Mail: withstars@126.com
 */

/**
 *
 给定一个整数数列，找出其中和为特定值的那两个数。
 你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

 示例:
 给定 nums = [2, 7, 11, 15], target = 9
 因为 nums[0] + nums[1] = 2 + 7 = 9
 所以返回 [0, 1]
 */
public class Main {

    public int[] twoSum(int[] nums, int target) {
        int[] res=new int[2];
        for(int i =0;i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+nums[j] == target){
                    res[0]=i;
                    res[1]=j;
                    return res;
                }
            }
        }
        return res;
    }

}
