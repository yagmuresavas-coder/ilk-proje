import java.util.Scanner;
public class sinavNotuHesaplama {

	public static void main(String[] args) {
		
		Scanner girdi = new Scanner (System.in);
        while (true) 
        {
            System.out.print("\nSınav Notunu Giriniz (Çıkmak için 'q' veya 'ç' tuşuna basın): ");
      
            String input = girdi.nextLine(); 
        if (input.equalsIgnoreCase("q") || input.equalsIgnoreCase("ç"))             
         {
                System.out.println("Programdan çıkılıyor...");
                break; 
         }
         try  {
         int not=Integer.parseInt(input);        
        if(not>100) 
        {
        	System.out.println("GEÇERSİZ NOT GİRDİNİZ!");
        }
        else if(not>=90)
        {
        	System.out.println("Sınav Derecesi AA'dır ");
        }
        else if(not<90 && not>=80)
        {
            System.out.println("Sınav Derecesi BA'dır ");
        }
        else if(not<80 && not>=70) 
        {
        	System.out.println("Sınav Derecesi BB'dır ");
        }
        else if(not<70 && not>=60) 
        {
        	System.out.println("Sınav Derecesi CC'dır ");
        }
        else if(not<60) 
        {
        	System.out.println("KALDINIZ");
        }
         }
         catch (NumberFormatException e)
         {
             System.out.println("Hatalı giriş! Lütfen bir sayı girin veya 'q'/'ç' ile çıkın.");
      }  
        girdi.close();
        System.out.println("Programı kullandığınız için teşekkürler.");   
        }
	}
}
