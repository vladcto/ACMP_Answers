import java.util.Scanner;
import java.io.PrintWriter;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int in_one;
        in_one = scanner.nextInt()/6;
        out.println(in_one + " " + in_one * 4 + " " + in_one);
        out.flush();
    }
}
