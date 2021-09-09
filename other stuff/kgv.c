#include <stdio.h>

int kgV(int num1, int num2);

int main(){
  int num1 = 8;
  int num2 = 5;

  kgV(num1, num2);
}

int kgV(int num1, int num2){
  int start;

  //Start the for loop with the bigger number
  if(num1 > num2){
      start = num1;
  } else {
      start = num2;
  }

  //Check for the smallest number that is divisible by num1 and num2
  for(int i = start; i <= num1*num2; i++){
    if(i % num1 == 0 && i % num2 == 0){
      printf("The %d\n", i);
      break;
    }
  }
  return 0;
}