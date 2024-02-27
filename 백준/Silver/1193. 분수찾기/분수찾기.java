import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int target = Integer.parseInt(br.readLine());

		// 1, 2, 4, 7 , 11 , 15

		int bunmo = 0;
		int bunja = 0;

		int seq = 1; // 대각선의 첫 값
		int count = 0; // 해당 대각선의 최댓값

		while (count < target) {
			count += seq;
			seq++;
		} // <- target보다 한 층 더 다음 것으로 올라가서 멈춤

		if((seq-1)%2 == 0) { // 짝수일 때
			bunja = (seq-1) - (count-target);
			bunmo = 1 + (count - target);
		}else { // 홀 수 일 때
			bunja = 1 + (count - target);
			bunmo = (seq-1) - (count-target);
		}

		System.out.println(bunja + "/" + bunmo);
	}
}