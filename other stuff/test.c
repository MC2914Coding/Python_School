#include <stdio.h>

int try(int tries);

int main(void){
  int tries = 0;
  try(tries);
}

int try(int tries){
  int user;
  int n = 1;
  
  while (tries >= 3){
    printf("num plz");
    scanf("%d", &user);
    
    if(user == n){
      printf("Correct");
    } else{
      printf("Try again");
      tries++;
      try(tries);
    }
  }
  return tries;
}