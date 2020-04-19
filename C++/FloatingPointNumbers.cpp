#include <iostream>
#include <cmath>
#include <stdint.h>
#include <stdlib.h>

using namespace std;

int main(){

    // Earn 1 coin per deci second, how much will I earn in one year?

    float earning = 1.0F;
    float fortune = 0.0F;

    for(int i=0; i<10*60*60*24*365; i++){
        fortune += earning;
    }

    // fortune is suppose to be 315 million
    // but fortune is 16.7 million?
    // if you add large number to a small number, the small number could become 0.
    // this is what happend here
    cout << fortune << endl;;



    // BAD - This will run forever
    /*
    for(float i = 100.0F; i != 0.0F; i-=0.01){
       // do something
    }
    */
    for(float i = 8; i != 0; i -= 0.125)
        cout << "1";
    for(float i = 10; i != 0; i -= 0.25)
        cout << "2";
    for(float i = 8; i != 0; i -= 0.1)
        cout << "3";
    for(int i = 8.12; i != 0; i -= 0.125)
        cout << "4";






    return 0;
}
