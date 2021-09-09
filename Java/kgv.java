public class Ur_mom {
  public static void main(String[] args) {

    int start;

  //Check if one of the given numbers is 0
  if(num1 > 0 && num2 > 0){

    //Start the for loop with the bigger number
    if(num1 > num2){
        start = num1;
    } else {
        start = num2;
    }

    //Check for the smallest number that is divisible by num1 and num2
    for(int i = start; i <= num1*num2; i++){
      if(i % num1 == 0 && i % num2 == 0){
        printf("The smallest common multible is %d\n", i);
        break;
      }
    }
  } else {
    printf("The smallest common multible is 0\n");
  }
  return 0;
}