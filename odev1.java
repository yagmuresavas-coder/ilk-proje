import java.util.Scanner; 
public class odev1 {
   // its my computer programming lesson homework all written codes are arranged according to pleasure
	public static void main(String[] args) {
		Scanner girdi = new Scanner (System.in);// we want to a min 5 character user name
		System.out.println("En AZ 5 Karakterli Kullanıcı Adını Giriniz");
		String isim = girdi.nextLine();
		char ilkHarf = isim.charAt(0);

        if (ilkHarf == '*' || ilkHarf == '?' || ilkHarf == '!')// we can't use this char
        {
	      System.out.println("Kullanıcı Adının İlk Karakterini Geçersiz Karakter Girdiniz(Lütfen '*,?,!' karakterlerini ilk karakter girmeyiniz)");
	      
        }		
       if(isim.length()<5)
       {
    	   System.out.println("Girdiğiniz Ad 5 Karakterden Az tekrar Deneyiniz");
       }
        else if(isim.length()>=5) 
       {
    	   System.out.println("Girdiğiniz kullanıcı adı geçerlidir");// if user name access is successful we want to password
    	   Scanner girdi1=new Scanner(System.in);
    	   System.out.println("En AZ 6 Karakterli Bir Şifre Belirleyiniz(İçinde @ karakteri kullanınız)");
    	   String sifre=girdi1.nextLine();
    	   String sifreKucuk = sifre.toLowerCase(); 
    	   char ilkHarfKucuk = sifreKucuk.charAt(0); //LowerCasei nasıl kullanacağımı çözemedim ekledim 
           char sonHarfKucuk = sifreKucuk.charAt(sifreKucuk.length() - 1);
    	   char ilkHarf1 = sifre.charAt(0);
           char sonHarf = sifre.charAt(sifre.length() - 1);
           
           if(sifre.length()<6) // we want to use min 6 character for password
    	   {
    		   System.out.println("Şifrenizin 6 karakterden uzun olması gerekli");
    	   }
    	   if(sifre.length()>=6)
    	   {
    	   if (sifre.indexOf('@') == -1) // we must to use @ char in password
        	   {
                   System.out.println("Şifreniz @ işareti içermelidir");
               }
    	   
    	       if(ilkHarfKucuk==sonHarfKucuk)// And fist character and last character is same we show the error
    	       {
    	    	   System.out.println("Şifreniz Geçersizdir İlk ve Son Karakterleri Farklı olmalıdır");
    	       }
    	       
    	       else if (ilkHarfKucuk!=sonHarfKucuk) 
    	       {
    	    	   System.out.println("Şifreniz Geçerlidir");
               }
    	       
    		   else if (ilkHarf1 == sonHarf) 
               {
    			   System.out.println("Şifreniz Geçersizdir İlk ve Son Karakterleri Farklı olmalıdır");
    	       }
               if (ilkHarf1 != sonHarf)
               {
            	   System.out.println("Şifreniz Geçerlidir");
               }
    	   }
       }
	}

}
