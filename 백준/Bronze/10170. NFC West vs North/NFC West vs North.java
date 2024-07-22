public class Main {
    public static void main(String[] args) {
        StringBuilder sBuilder = new StringBuilder()
        .append("NFC West       W   L  T\n")
        .append("-----------------------\n")
        .append("Seattle        13  3  0\n")
        .append("San Francisco  12  4  0\n")
        .append("Arizona        10  6  0\n")
        .append("St. Louis      7   9  0\n\n")
        .append("NFC North      W   L  T\n")
        .append("-----------------------\n")
        .append("Green Bay      8   7  1\n")
        .append("Chicago        8   8  0\n")
        .append("Detroit        7   9  0\n")
        .append("Minnesota      5  10  1");

        System.out.println(sBuilder);
    }
}