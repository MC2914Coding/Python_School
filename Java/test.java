public class Ur_mom {
  public static void main(String[] args) {

    int num1 = 6;
    int num2 = 12;

    for(int i = 1; i <= num1*num2; i++){
      if(i % num1 == 0 && i % num2 == 0){
        printf("%d", i);
        break;
      }
    }

  }
}