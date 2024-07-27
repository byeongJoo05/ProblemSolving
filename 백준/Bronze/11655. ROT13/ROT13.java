import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c >= 'A' && c <= 'Z') {
                if (c + 13 > 'Z') {
                    result.append((char) (c + 13 - 26));
                } else {
                    result.append((char) (c + 13));
                }
            }
            else if (c >= 'a' && c <= 'z') {
                if (c + 13 > 'z') {
                    result.append((char) (c + 13 - 26));
                } else {
                    result.append((char) (c + 13));
                }
            }
            else {
                result.append(c);
            }
        }

        System.out.println(result.toString());
    }
}