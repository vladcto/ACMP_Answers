using System;
using System.IO;

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("INPUT.txt");
            StreamWriter writer = new StreamWriter("OUTPUT.txt");
            byte index_reader = Convert.ToByte(reader.ReadLine().Trim());
            byte[] Cost_in_index_day = new byte[index_reader];
            string[] string_cost = reader.ReadLine().Trim().Split(' ');
            byte max_value = 0;
            byte number_roud_max_value = 0;
            int answer = 0;
            reader.Close();
            for (int i=index_reader-1; i>0; i--)
            {
                Cost_in_index_day[i] = Convert.ToByte(string_cost[i]);
                if (Cost_in_index_day[i] > max_value)
                {
                    answer += max_value * number_roud_max_value;
                    max_value = Cost_in_index_day[i];
                    number_roud_max_value = 1;
                }
                else
                {
                    number_roud_max_value++;
                }
            }
            Cost_in_index_day[0] = Convert.ToByte(string_cost[0]);
            if (Cost_in_index_day[0] > max_value)
            {
                answer += max_value * number_roud_max_value + Cost_in_index_day[0];
            }
            else
            {
                answer += max_value * (number_roud_max_value+1);
            }
            writer.WriteLine(answer);
            writer.Close();
        }
    }
}
