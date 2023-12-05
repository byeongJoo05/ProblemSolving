package BOJ;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.Date;

public class BOJ10699 {
    public static void main(String[] args) {
        Date now = new Date();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("YYYY-MM-dd");

        String result = simpleDateFormat.format(now);

        System.out.println(result);
    }
}
