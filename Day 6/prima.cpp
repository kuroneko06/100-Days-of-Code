#include <iostream>
using namespace std;

int main(){
    int min = 1;
    int max = 10;
    int check;

    cout << "=======Find the Prima's Number=======" << endl;

    for (int i = min; i < max; i++)
    {
        for (int k = min; k < max; k++)
        {
            if (i % k == 0)
            {
                check++;
            }
        }
        if (i != 0 && check == 2)
        {
            cout << i << " ";
        }
        check = 0;
    }
    
}
