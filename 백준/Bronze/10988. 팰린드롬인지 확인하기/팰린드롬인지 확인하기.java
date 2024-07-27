import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        String[] str = scanner.next().split("");
        int len = str.length;
        int mid = len / 2;
        int flag = 1;
        for (int i =0; i < mid ; i++) {
            if (!str[i].equals(str[len-1-i])) {
                flag = 0;
                break;
            }
        }

        System.out.println(flag);
    }
}