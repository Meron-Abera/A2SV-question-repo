class Solution {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> nums = new ArrayList<>();
        for (; head != null; head = head.next) {
            nums.add(head.val);
        }

        int[] ans = new int[nums.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < nums.size(); i++) {
            while (!stack.isEmpty() && nums.get(i) > nums.get(stack.peek())) {
                ans[stack.pop()] = nums.get(i);
            }
            stack.push(i);
        }
        return ans;
    }
}
