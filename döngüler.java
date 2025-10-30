import java.util.Scanner;

public class döngüler {

	public static void main(String[] args) {

		Scanner girdi = new Scanner (System.in);
		System.out.println("Bir sayı giriniz: ");
		double sayi=girdi.nextDouble();
        if(sayi<0) 
        {
        	System.out.println("Sayı negatiftir");
        }
        
        else if(sayi>0)
        {
        	System.out.println("Sayı pozitiftir");
        }
        else if (sayi==0)
        {
        	System.out.println("Sayı 0 dır");
        }

	}

}
