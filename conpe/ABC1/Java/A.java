package conpe.ABC1.Java;
import java.util.Scanner;

// ここを public class Main にしたらACだった
public class A{ 
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int h1 = scan.nextInt();
            int h2 = scan.nextInt();
            System.out.println(h1-h2);
        }
    }
}