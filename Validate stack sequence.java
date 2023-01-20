class Solution {
   public boolean validateStackSequences(int[] pushed, int[] popped) {
    Deque<Integer> stack = new LinkedList<>();
    int j = 0;
    for (int i = 0; i < pushed.length; i++) {
      stack.push(pushed[i]);
      while (!stack.isEmpty() && popped[j] == stack.peek()) {
        j++;
        stack.pop();
      }
    }
    return stack.isEmpty();
  }
}
