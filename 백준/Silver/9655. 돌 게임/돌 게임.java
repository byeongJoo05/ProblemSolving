import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        // 상근이가 이길 수 있는 법
        // 돌이 1개이거나
        // 3개씩 가져갔다고 쳤을 때
        // 몫이 홀수이면서, 나머지가 2일때
        // 몫이 홀수이면서, 나머지가 0일 때
        // 몫이 짝수이면서, 나머지가 1일 때
        int mok = n/3;
        int namoji = n%3;

        if (n >= 3) {
            if (mok % 2 == 1) {
                if (namoji % 2 == 0) {
                    System.out.println("SK");
                } else {
                    System.out.println("CY");
                }
            } else {
                if (namoji % 2 == 1) {
                    System.out.println("SK");
                } else {
                    System.out.println("CY");
                }
            }
        } else {
            if (n == 1) {
                System.out.println("SK");

            } else {
                System.out.println("CY");
            }
        }
    }
}
