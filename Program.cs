internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Lütfen ilk sayıyı giriniz: ");
        string alinan_sayi = Console.ReadLine();
        double sayi = double.Parse(alinan_sayi);
        Console.WriteLine("Lütfen ikinci sayıyı giriniz: ");
        string alinan_sayi1 = Console.ReadLine();
        double sayi1 = double.Parse(alinan_sayi1);
        Console.WriteLine("Lütfen Yapmak İstediğiniz İşlemi Seçiniz(+,-,*,/):");
        string kullanıcıdan_Alinan = Console.ReadLine();
        char islem;
        islem = kullanıcıdan_Alinan[0];
        double sonuc;
        if (islem == '+')
        {
            sonuc = sayi + sayi1;
            Console.WriteLine("Sonuç = " + sonuc);

        }
        else if (islem == '-')
        {
            sonuc = sayi - sayi1;
            Console.WriteLine("Sonuç = " + sonuc);

        }
        else if (islem == '*')
        {
            sonuc = sayi * sayi1;
            Console.WriteLine("Sonuç = " + sonuc);

        }
        else if (islem == '/')
        {
            if (sayi1 == 0)
            {
                Console.WriteLine("Sonuç Tanımsızdır(Syntax Error)");
            }
            else
            {
                sonuc = sayi / sayi1;
                Console.WriteLine("Sonuç = " + sonuc);
            }
        }
    }
}