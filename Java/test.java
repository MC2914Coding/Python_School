public class sub {
    public static void sub() {
        int minuend = 11; //Integer wert
        int subtrahend = 5; //Integer wert

        minuend--; //minuend um 1 veringern. nun ist minuend 10

        //Vriante1:
        System.out.println("Die differenz ist: " + (minuend - subtrahend));
        
        //Variante 2:
        minuend -= subtrahend; //subtrahend von minuend abziehen
        System.out.println("Die differenz ist: " + minuend);
    }
} 