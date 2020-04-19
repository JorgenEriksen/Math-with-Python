#include <iostream>
#include <cmath>

using namespace std;

int main(){



    int x = 204;            // 11001100
    x = x >> 2;
    cout << x;             // 00110011 = 51

    x = x&~(1<<0);         // clear bit nr. 0


    cout << endl << x;     // 00110010 = 50

    x = x | (1 << 3);      // set bit nr 3
    x = x | 8;             // kan også skrives sånn

    cout << endl << x;     // 00110010 = 58

    x = x ^ (1 << 3);      // flip/toggle bit nr 3

    cout << endl << x;






    return 0;
}
