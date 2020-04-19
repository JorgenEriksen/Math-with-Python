#include <iostream>
#include <Eigen/Dense>

using namespace std;

using Eigen::MatrixXf;
using Eigen::VectorXf;

int main(){
    MatrixXf m1(3,3);
    VectorXf m2(3);

    // acess by m(row, column)
    m1(0,0) = 3;
    m1(1,0) = 2.5;

    // stream overload
    m1 << 1, 2, 3,
          4, 5, 6,
          7, 8, 9;



    // slicing 2x2 block starting at (1,1)
    m1.block<2,2>(1,1) << 0,0,0,0;
    cout << m1;


    return 0;
}
