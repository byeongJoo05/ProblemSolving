import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int a, b, c;
        int[] timeZone = new int[100];
        int sum = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        
        a = Integer.parseInt(input[0]);
        b = Integer.parseInt(input[1]) * 2;
        c = Integer.parseInt(input[2]) * 3;

        for (int i= 0; i < 3; i++) {
            String[] time = br.readLine().split(" ");

            for (int j = Integer.parseInt(time[0]); j < Integer.parseInt(time[1]) ; j++) {
                timeZone[j] += 1;
            }
        }

        for (int i=0; i < timeZone.length; i++) {
            if (timeZone[i] == 1) sum+=a;
            else if (timeZone[i] == 2) sum+=b;
            else if (timeZone[i] == 3) sum+=c;
        }

        System.out.println(sum);
    }
}