#include <stdio.h>

int main(void){
  int num, rev_num = 0;
  int digitsSize = 3;
  int returnSize[3] = {};
  int digits[] = {1,2,3};
    
  //Get the array into a number
  for(int i = 0; i < digitsSize; i++){
    num = num + digits[i];
    num = num*10;
  }
  num = num/10;
  
  //add 1 to that number
  num++;
  
  //reverse the number
  int c, a;
  a = num;
  while (num != 0) { //reverse integer algorythm
    c = num % 10;
    rev_num = rev_num * 10 + c;
    num /= 10;
  }
  //printf("%d", rev_num);
  

  //get that number back into a array
  for(int i = 0; i < sizeof(returnSize); i++){
    int last_num = rev_num % 10;
    returnSize[i] = last_num;
    if(rev_num > 10){
      rev_num /= 10;
    }

    if(last_num == 1 || rev_num == 1){
      break;
    }
  }
  
  for(int i = 0; i < 3; i++){
    printf("%d", returnSize[i]);  
    printf(" | ");
  }

  return 0;
}
