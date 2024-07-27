import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); // 남아 있는 개행 문자를 소비
        String[] cmpStrings = scanner.nextLine().split("\\*");
        String frontStr = cmpStrings[0];
        String endStr = cmpStrings[1];

        for (int i = 0; i < n; i++) {
            String str = scanner.nextLine();
            boolean start = true;
            boolean end = true;


        if (frontStr.length() + endStr.length() > str.length()) {
            System.out.println("NE");
            continue;
        }

            start = str.startsWith(frontStr);
            end = str.endsWith(endStr);

            if (start && end) System.out.println("DA");
            else System.out.println("NE");
        }
    }
}