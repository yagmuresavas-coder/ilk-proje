import java.util.Scanner; // Scanner sınıfını kullanmak için import ediyoruz

public class yagmur { // Kodu çalıştırmak için bir class içinde olmalı

    public static void main(String[] args) {
        
   
        Scanner girdi = new Scanner(System.in);
        
       
        while (true) {
            
            
            System.out.print("\nSınav Notunu Giriniz (Çıkmak için 'q' veya 'ç' tuşuna basın): ");
            
           
            String input = girdi.nextLine(); 

            
            if (input.equalsIgnoreCase("q") || input.equalsIgnoreCase("ç")) {
                System.out.println("Programdan çıkılıyor...");
                break; 
            }

            // 6. Hata Kontrolü: Girilen değer bir sayı mı?
            try {
                // Girilen metni 'double' (ondalıklı sayı) tipine çevirmeyi dene
                double not = Double.parseDouble(input);

                // 7. Sizin not hesaplama mantığınız (biraz daha iyileştirildi)
                //    (Negatif sayıları da geçersiz saydık)
                if (not > 100 || not < 0) {
                    System.out.println("GEÇERSİZ NOT GİRDİNİZ! (Not 0-100 arasında olmalıdır)");
                } else if (not >= 90) { // 90-100
                    System.out.println("Sınav Derecesi AA'dır ");
                } else if (not >= 80) { // 80-89.9
                   System.out.println("Sınav Derecesi BA'dır ");
                } else if (not >= 70) { // 70-79.9
                    System.out.println("Sınav Derecesi BB'dır ");
                } else if (not >= 60) { // 60-69.9
                    System.out.println("Sınav Derecesi CC'dır ");
                } else { // 0-59.9
                    System.out.println("KALDINIZ");
                }

            } catch (NumberFormatException e) {
                // Eğer kullanıcı 'q' dışında sayı olmayan bir şey girerse (örn: "merhaba")
                // Double.parseDouble hataya düşer ve bu blok çalışır.
                System.out.println("Hata: Geçersiz giriş. Lütfen bir sayı girin veya 'q' ile çıkın.");
            }
        }
        
        // 8. Döngü bittikten sonra kaynakları kapat
        girdi.close();
        System.out.println("Programı kullandığınız için teşekkürler.");
    }
}

