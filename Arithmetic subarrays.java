class Solution {
        public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
            int m = l.length;
            List<Boolean> res = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                Boolean item = isArithmetic(Arrays.copyOfRange(nums, l[i], r[i] + 1));
                res.add(item);
            }
            return res;
        }

        public Boolean isArithmetic(int[] nums) {
            Arrays.sort(nums);
            int len = nums.length;
            int d = nums[1] - nums[0];
            for (int i = 2; i <= len - 1; i++) {
                if (nums[i] - nums[i - 1] != d) {
                    return false;
                }
            }
            return true;
        }
    }
