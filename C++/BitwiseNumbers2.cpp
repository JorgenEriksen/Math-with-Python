#include <iostream>
#include <cmath>
#include <stdint.h>
#include <stdlib.h>

using namespace std;

int main(){
    int x = 44;  // 101100
    x = x&(x-1); // fjerner 1'ern som er lengst til høyre
                 // clear the least significant set bit
                 // x = 101000 = 40





    x=40;
    int c = 0;
    while(x){
        x = x&(x-1);
        c++;
    }
    cout << endl << c; // number of set bits

    x = 'a';
    cout << endl << x; // 97


    bool prop[64]; // lagrer 64 bits
    unsigned long long prop2; // samme som bool prop[64]


    // ASCII eksempel:
    // 0  1  2  3  4  5  6  7  8  9
    // 48,49,50,51,52,53,54,55,56,57

    //A..Z
    //65..90

    //a..z
    //97..122

    //128..255
    // special characters

    //0...31
    //controll characters ( esc, backspace, return osv.)

    //32 - whitespace

    //32..255 er da pritable characters


    // A : 0100 0001 => 65
    // a : 0110 0001 => 97

    // Z : 0101 1010 => 90
    // z : 0111 1010 => 122
    // sjekk bit nummer 5(6) om det er stor eller liten bokstav


    // string s = "123";
    // x = atoi(s);       // x = 123



    // TWOS COMP

    x = 10;
    cout << endl << x;
    x = ~x +1; // -10 -> two's complement of 10
    cout << endl << x;

    // a) Compute twos complement of 5 and write it hexadecimally.
    x = 5;
    x = ~x +1; // FFFB

    // b) Compute the twos complement of 7 and write it hexadecimally
    int y = 7;
    y = ~y +1;

    // c) Add together the two answers from a) and b) (hexadecimally)
    cout << endl << x+y; // 0xFFF4
    unsigned int a;
    a = 20;
    unsigned int n = ~( (~0) >> 1);
    cout << endl << n;

    if(a & n) {
        a = (~a) + 1;
    }

    cout << endl << a;



    return 0;
}
