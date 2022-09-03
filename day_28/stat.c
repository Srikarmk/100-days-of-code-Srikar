#include<stdio.h>

int add(int n){
	static sum=0;
	sum+=n;
	return sum;
}
int main(){
	int a=add(5);
	printf("%d\n",a);
	a=add(5);
	printf("%d\n",a);
	a=add(5);
	printf("%d",a);
	
	
}
