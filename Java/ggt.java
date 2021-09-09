public class GCD {
  public static void GCD() {
    int n1, n2, i, gcd;
    n1 = 6;
    n2 = 12;

    //loop from two till GCD
    for(i=2; i <= n1 && i <= n2; ++i)
    {
        // Checks if i is a factor of both integers
        if(n1%i==0 && n2%i==0)
            gcd = i;
    }
    System.out.println(gcd);
  }
}