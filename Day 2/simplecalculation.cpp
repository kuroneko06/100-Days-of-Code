#include <iostream>
using namespace std;

int main (){
    int target;
    float val1;
    float val2;
    double total;

    cout << "=====Welcome in simple Calculator=====" << endl;
    cout << "1. Choose 1 for plus calculation" << endl;
    cout << "2. Choose 2 for minus calculation" << endl;
    cout << "3. Choose 3 for multiplication calculation" << endl;
    cout << "4. Choose 4 for divided calculation" << endl;
    cout << "======================================" << endl;
    cout << "Choose your calculation please : ";
    cin >> target;
    cout << "Input the first value : ";
    cin >> val1;
    cout << "Input the second value : ";
    cin >> val2;

    switch (target)
    {
    case 1:
        total = val1 + val2;
        cout << "Result of Plus Calculation : " << total << endl;
        break;
    case 2:
        total = val1 - val2;
        cout << "Result of Minus Calculation : " << total << endl;
        break;
    case 3:
        total = val1 * val2;
        cout << "Result of Multiplication Calculation : " << total << endl;
        break;
    case 4:
        total = val1 / val2;
        cout << "Result of Divided Calculation : " << total << endl;
        break;
    default:
        break;
    }

}
