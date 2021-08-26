#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int main(void){
  int num1 = 2;
  int num2 = 3;
  int sum;

  for(int count = 0; count <= num2; count = count + 1){
    sum = sum+num1;
  }

  printf("%d", sum);

  return 0;
}