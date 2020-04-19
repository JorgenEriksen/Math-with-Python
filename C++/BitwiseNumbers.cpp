#include <iostream>
#include <cmath>
#include <stdint.h>

using namespace std;

int main(){


    int a = 0;


    // A - Set bit 12 in a
    a = a | (1 << 12);
    cout << endl << a;

    // B - Set bits 2 and 5 in a
    a = a | 0x24;
    cout << endl << a;

    // C - Set all bits except bit 3 in a
    a = a | ~(a & 0);
    a = a&~(1<<3);
    // evt  a = (a | ~(a & 0))&~(8<<0);
    cout << endl << a;

    // D - Set all bits in a
    a = a | ~(a & 0);
    cout << endl << a;

    // E - Clears bit 12 in a
    a = a&~(1 << 12);
    cout << endl << "E: " << a;

    // F - Clears bits 2 and 5 in a.
    a = a&~(0x24 << 0);
    cout << endl << a;

    // G - Clears all bits except bit 4 in a.
    a = (a & ~a) | 0x10;
    cout << endl << a;

    // H - Clears all bits in a.
    a &= ~a;
    cout << endl << a;

    // I - Toggles bit 12 in a.
    a = a^(1 << 12);
    cout << endl << a;

    // J - Toggles bits 2 and 5 in a.
    a ^= 36;
    cout << endl << a;

    // K - Toggles all bits except bit 4 in a
    a = (a^-1) ^(1 << 4);
    cout << endl << a;

    // I - Toggles all bits in a.
    a = ~a;
    cout << endl << a;

    // M - Set bits 3 and 13 in a using shift
    a = a | (1 << 3) | (1 << 13);
    cout << endl << a;

    // N - Clear bits 4 in a using shift
    a = a&~(1 << 4);

    // O - Toggle bits 14 and 11 in a using shift
    a = a^(9<<11);
    // P - Clear bit 4 and set bit 23 in using shift
    a = a = a &~(1 << 4) | (1 << 23);

    // Q - Branch if bit 11 is equal to 0
    if((a & (1 << 3)) == 0){
            cout << endl << "bit 11 is set to 0";
    }

    // R - Branches if bit 11 and bit 12 is set to 1
    if((a & (1 << 11)) != 0 && (a & (1 << 12)) != 0){
        cout << endl << "bit 11 and 12 is set to 1";
    }

    // S - Branches if bit 2 and bit 4 are different (hint: xor and shift)
    if( (a&(1 << 2)) ^ (a&(1 << 4)) != 0 ){
        cout << endl << "bit 2 and 4 are different";
    }

    // T - Branches if bit 10 is 0 and bit 11 is 1.
    if( (a & (1 << 10)) == 0 && a & (1 << 11) != 0 ){
        cout << endl << "bit 10 is 0 and bit 11 is 1";
    }

    // U - Multiplies a by 128 using bit-manipulation
    a = (a << 7);
    cout << endl << a;

    // V - divides a by 64 using bit-manipulation
    a = (a >> 6);
    cout << endl << a;

    // W -  Calculates a modulo 1024 using bit-manipulation
    // 0x3FF = 1024-1
    a = a & 0x3FF;
    cout << endl << a;






    return 0;
}
