import org.junit.Test;
import sun.font.TrueTypeFont;

import java.util.*;

/*
二维数组，数组长度为n（偶数），两列数组分别取分别取n/2个数，且取的索引不重复，使得两列数各自取的总和最大
 */

public class SumOfDiff {
    public int sum(int[] arrA, int[] arrB){
        TreeMap<Integer, List> treeMap = new TreeMap();
        // 获得两个数组的差值，右减左
        for (int i = 0; i < arrA.length; i++) {
            int d = arrB[i] - arrA[i];
            if (treeMap.containsKey(d)){
                List temp = new ArrayList();
                for (int j = 0; j < treeMap.get(d).size(); j++) {
                    temp.add(treeMap.get(d).get(j));
                }
                temp.add(i);
                treeMap.put(d, temp);
            }else{
                treeMap.put(d, Arrays.asList(i));
            }
        }

        List<Integer> index = new ArrayList();
        while (true){
            if (treeMap.isEmpty()){
                break;
            }
            List list = treeMap.remove(treeMap.lastKey());
            index.addAll(list);
        }
        
        // 最大和为res
        int res = 0;
        for (int i = 0; i < arrA.length / 2; i++) {
            res += (arrB[index.get(i)] + arrA[index.get(i+arrA.length / 2)]);
        }
        return res;
    }


    @Test
    public void test(){
        int[] arr1 = new int[]{2, 3, 6, 8};
        int[] arr2 = new int[]{3, 9, 7, 2};

//        List list1 = Arrays.asList(arr1);
//        List list2 = Arrays.asList(arr2);

        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
        int res = sum(arr1, arr2);
        System.out.println(res);
    }
}
