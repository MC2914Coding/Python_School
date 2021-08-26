#include <stdio.h>

int main(){
  int num1 = 2;
  int num2 = 3;
  int sum;
  for(int count = 0; count <= num2; count = count + 1){
    sum = sum+num1;
    printf("%d", sum);
  }
  printf("%d", sum);
}