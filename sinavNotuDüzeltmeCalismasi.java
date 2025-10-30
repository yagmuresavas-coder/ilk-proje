import java.util.Scanner;
public class sinavNotuDüzeltmeCalismasi {

	public static void main(String[] args) {
		Scanner girdi = new Scanner (System.in);
		System.out.println("Sınav notunu sayısal değer olarak giriniz");
		double not = girdi.nextDouble();
        while(true)
        {
        	if (not>100)
        	{
        		System.out.println("GEÇERSİZ NOT GİRDİNİZ");
        		
        	}
        	else if(not>=90 && not<100)
        	{
        		System.out.println("Aldığınız Sınav Derecesi AA'dır");
        	}
        	else if(not<90 && not>=80) 
        	{
        		System.out.println("Aldığınız Sınav Derecesi BA'dır");
        	}
        	else if(not>=70 && not<80)
        	{
        		System.out.println("Aldığınız Sınav Derecesi BB'dır");
        	}
        	else if(not>=60 && not<70)
        	{
        		System.out.println("Aldığınız Sınav Derecesi CC'dır");
        		
        	}
        	else if(not<60)
        	{
        		System.out.println("KALDINIZ!");
        	}
        	break;
        }
		
	}

}
