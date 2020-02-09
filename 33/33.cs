//Первый недострелял на 1 меньше отстреленных вторым
//Для второго ровно противоположно
using System;
using System.IO;
namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamWriter writer = new StreamWriter("Output.txt");
            StreamReader reader = new StreamReader("Input.txt");
            string str = reader.ReadLine();
            reader.Close();
            writer.WriteLine(Int32.Parse(str.Substring(str.IndexOf(" ")+1))-1 + " "+ (Int32.Parse(str.Substring(0,str.IndexOf(" ")))-1) );
            writer.Close();
        }
    }
}
