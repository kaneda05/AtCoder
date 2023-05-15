package conpe.ABC2.Java;
import java.util.Scanner;

// ここを public class Main にしたらACだった
public class A{ 
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int X = scan.nextInt();
            int Y = scan.nextInt();
            if (X<Y)
            System.out.println(Y);
            else
            System.out.println(X);
        }
    }
}