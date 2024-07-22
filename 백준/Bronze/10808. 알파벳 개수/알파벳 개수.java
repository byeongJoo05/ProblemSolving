import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int arr[] = new int[26];

        String in = new Scanner(System.in).nextLine();

        for (int i = 0; i < in.length(); i++) {
            char ch =in.charAt(i);
            int asc = ch-97;

            arr[asc] += 1; 
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
    }
}