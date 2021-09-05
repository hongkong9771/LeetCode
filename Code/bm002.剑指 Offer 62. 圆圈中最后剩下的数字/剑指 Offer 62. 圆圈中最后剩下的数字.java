class Solution {
    public int lastRemaining(int n, int m) {
		
		/*
		每次所要删除元素的位置位于（index+m-1）% l处，其中l为当前数组的长度
		*/
        ArrayList<Integer> list = new ArrayList(n);
        for(int i=0; i<n; i++){
            list.add(i);
        }
        int index = 0;
        int l = list.size();
        while(l > 1){
            
            index = (index + m - 1) % l;
            list.remove(index);
            l = list.size();
        }
        return list.get(0);
    }
}