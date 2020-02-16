using System;

class app
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split(' ');
        // S одной панели = a*b
        // S всей поверхности = a*b*n
        // С двеух сторон поэтому ansewr = 2*S_все_поверх.
        Console.WriteLine(Convert.ToInt32(input[1]) * Convert.ToInt32(input[2]) * 2 * Convert.ToInt32(input[0]));
    }
}
