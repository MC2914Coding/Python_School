public class Ur_mom {
  public static void main(String[] args) {
    int n1, n2, i, gcd;

    n1 = 6;
    n2 = 12;

    for(i=1; i <= n1 && i <= n2; ++i)
    {
        // Checks if i is factor of both integers
        if(n1%i==0 && n2%i==0)
            gcd = i;
    }

    System.out.println(gcd);
  }
}