#include <stdio.h>

int kgV(int num1, int num2);

int main(){
  int num1 = 6;
  int num2 = 12;

  kgV(num1, num2);
}

int kgV(int num1, int num2){
  for(int i = 1; i <= num1*num2; i++){
    if(i % num1 == 0 && i % num2 == 0){
      printf("%d", i);
      break;
    }
  }
  return 0;
}