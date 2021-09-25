#include <iostream>
using namespace std;

int main (){
    int data[] = {5,3,4,2,1};
    int a, b;

    cout << "before : ";
    for (int k = 0; k < sizeof(data)/sizeof(data[0]); k++)
    {
        cout << data[k] << " ";
    }
    cout << endl;

    for (int i = 0; i < sizeof(data)/sizeof(data[0]); i++)
    {
        for (int j = 0; j < sizeof(data)/sizeof(data[0])-1; j++)
        {
            a = data[j];
            b = data[j+1];
            if (a > b)
            {
                data[j] = b;
                data[j+1] = a;
            }
        }
    }

    cout << "after : ";
    for (int k = 0; k < sizeof(data)/sizeof(data[0]); k++)
    {
        cout << data[k] << " ";
    }
    cout << endl;
    
}
