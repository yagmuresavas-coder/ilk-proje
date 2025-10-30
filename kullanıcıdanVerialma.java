import java.util.Scanner;

public class kullanıcıdanVerialma {

	public static void main(String[] args) {
		Scanner girdi = new Scanner (System.in);
		System.out.println("isim giriniz");
		String isim = girdi.nextLine();
		
        Scanner girdi1 = new Scanner (System.in);
        System.out.println("Yaşınızı Giriniz");
		int sayi=girdi1.nextInt();
		
		Scanner girdi2 = new Scanner (System.in);
		System.out.println("Boyunuzu Girin");
		double boy=girdi2.nextDouble();
		
		System.out.println("Bu sizin adınız:"+isim+"\nYaşınız: " +sayi+"\nBu da boyunuz:"+boy);
  
	   double pi=3.14;
	   
	   Scanner girdi3 = new Scanner (System.in);
	   System.out.println("Yarıçapı Giriniz");
	   double yaricap=girdi3.nextDouble();
	   
	   double cevre=2*pi*yaricap;
	   double alan=pi*yaricap*yaricap;
	   
	   System.out.println("Dairenin çevresi:"+cevre+"\nDairenin Alanı:"+alan);

	}

}
