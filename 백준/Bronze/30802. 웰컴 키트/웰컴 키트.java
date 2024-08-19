import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        solution();
    }

    private static void solution() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(bf.readLine(), " ");

        int[] sizes = new int[6];

        for (int i = 0; i < sizes.length; i++) {
            sizes[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        stringTokenizer = new StringTokenizer(bf.readLine(), " ");
        int t = Integer.parseInt(stringTokenizer.nextToken());
        int p = Integer.parseInt(stringTokenizer.nextToken());

        int tCnt = 0;
        for (int size : sizes) {
            if (size == 0) continue;
            if (size <= t) {
                tCnt++;
            } else {
                int mok = size / t;
                int namoji = size % t;
                tCnt += mok;

                if (namoji > 0) tCnt++;
            }
        }

        int pMok = n / p;
        int pNamoji = n % p;

        System.out.println(tCnt);
        System.out.println(pMok+ " " +pNamoji);

    }
}
