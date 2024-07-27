import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        Map<String, Integer> name = new HashMap<>();
        String answer = "";
        int failCnt = 0;

        int n = scanner.nextInt();

        for (int i = 0; i < n ; i++) {
            String[] playerName = scanner.next().split("");
            String firstName = playerName[0];
            if (name.containsKey(firstName)) {
                name.put(firstName, name.get(firstName) +1 );
            } else {
                name.put(firstName, 1);
            }
        }

        for (String firstName : name.keySet()) {
            int cnt = name.get(firstName);
            if (cnt >= 5) {answer += firstName;}
            else {failCnt += 1;}
        }

        if (failCnt == name.size()) {System.out.println("PREDAJA"); return;};

        System.out.println(answer);
    }
}