import java.util.Scanner;
 public class calculator
 {
   public static void main(String[] args)
   {
     Scanner scan = new Scanner(System.in);
     System.out.println("İlk Sayıyı Giriniz:");
     double sayi=scan.nextDouble();
     System.out.println("İkinci Sayıyı Giriniz");
     double sayi1=scan.nextDouble();
     System.out.println("Yapmak İstediğiniz İşlemi Seçiniz(+,-,*,/):");
     String alinan_islem=scan.next();
     char islem=alinan_islem.charAt(0);
     double sonuc;
      if(islem=='+')
      {
        sonuc=sayi+sayi1;
        System.out.println("Sonuç:"+sonuc);
      }
      if (islem=='-')
      {
        sonuc=sayi-sayi1;
        System.out.println("Sonuç:"+sonuc);
      }
      if (islem=='*')
      {
        sonuc=sayi*sayi1;
        System.out.println("Sonuç:"+sonuc);
      }
      if (islem=='/')
      { 
        if(sayi1==0)
        {
            System.out.println("İşlem Tanımsızdır(Syntax Error:)");
        }
        else
        {
            sonuc=sayi/sayi1;
            System.out.println("Sonuç:"+sonuc);
        }
      }

     scan.close();

   }








 }