#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int  gradefunction(double avg){
    if (avg>= 90) return 'a';
    else if(avg>=80) return 'b';
    else if (avg>=70) return 'c';
    else return 'f';
  

}
enum 
int main(){
    char x = gradefunction(400);
    printf("mark : %c",x);
    return 0;
}




