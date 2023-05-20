import java.util.*;
import java.util.HashSet;
import java.util.Set;


class Main{
    public static void main(String[] args){
        // 入力
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();

        Set<Integer> set = new HashSet<Integer>();  // Setの定義
        set.add(a);
        set.add(b);

		int K = sc.nextInt();
		int[] P = new int[K];

        for (int i=0; i < K; i++){
            P[i] = sc.nextInt();        // contains：含んでいるかどうかを調べる
            if (!set.contains(P[i])){   // !set.contains：含んでいないならばFalseを返す
                set.add(P[i]);
            }else{
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }
}