import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        solution();
    }

    private static void solution() throws IOException {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        if (n == 1) {
            System.exit(0);
        }

        isPrime = new boolean[n+1];

        Arrays.fill(isPrime, true);

        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if(isPrime[i]) {
                for (int j = i*i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        while (n != 1) {
            for (int i = 2; i <= isPrime.length; i++) {
                if (isPrime[i]) {
                    if (n % i == 0) {
                        System.out.println(i);
                        n /= i;
                        break;
                    }
                }
            }
        }
    }
}
