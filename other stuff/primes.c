#include <stdio.h>

int main(void){
  int n = 4;
  int sol = 0;

  //Include 2
  if(n >= 2){
    sol++;
  }

  //Sorting out primes
  for(int j = 0; j <= n; j++){ 
    if(j > 1){ 
      for(int i = 2; i <= j/2; i++){
        if(j % i == 0){
          break;
        } else {
          sol+=1;
          break;
        }
      }
    }
  }
  printf("\nPrime count: %d", sol);
  return 0;
}