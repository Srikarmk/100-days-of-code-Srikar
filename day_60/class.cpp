#include<iostream>

using namespace std;

class Animal{
public:
    bool hasFur;
    int age;
};

int main()
{
    Animal dog;
    dog.age=5;
    cout<<dog.age<<endl;

}