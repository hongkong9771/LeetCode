class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    public List<List<Integer>> combine(int n, int k) {
        backtrack(n, k, 1);
        return res;
    }

    public void backtrack(int n, int k, int startIndex){
        if(path.size() == k){
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = startIndex; i <= n - (k - path.size())+1 ; i++) {    // 剪枝操作
            path.add(i);
            backtrack(n, k, i+1);
            path.remove(path.size()-1);
        }
    }
}