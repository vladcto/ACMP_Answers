using System;

class app
{
    static void Main(string[] args)
    {
        double input = Convert.ToDouble(Console.ReadLine());

        if (input == 5)
        {
            Console.WriteLine("25");
        }
        else
        {
            Console.WriteLine(((input - 5) / 10) * ((input - 5) / 10 + 1) + "25");
        }

    }
}
