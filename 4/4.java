import java.util.Scanner;
import java.io.PrintWriter;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int in_one = scanner.nextInt();
        out.println(in_one + "9" + (9-in_one));
        out.flush();
    }
}
