import java.util.*;

class Main{
    public static void main(String[] args){
        // 入力
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        int[] querys = new int[Q+1];
        String[] x = new String[Q+1];

        for (int i=1; i<=Q; i++){
            querys[i] = sc.nextInt();
            if (querys[i] == 1){
                x[i] = sc.next();
            }
        }
        // クエリ処理
        Stack<String> S = new Stack<>(); // スタックの定義
        for (int i=1; i<=Q; i++){
            if (querys[i]==1){
                S.push(x[i]);
            }
            if (querys[i]==2){
                System.out.println(S.peek()); // peek
            }
            if (querys[i]==3){
                S.pop();
            }
        }
    }
}