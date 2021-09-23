#include <iostream>
using namespace std;

int main () {
    /*
    Rumus bangun ruang bola
    Rumus Volume Bola = 4/3 x phi x jari-jari x jari-jari x jari-jari
    Rumus Luas Bola = 4 x phi x jari-jari x jari-jari
    Phi = 3,14 atau 22/7
    */

   double const phi = 3.14;
   float r;
   int target;

   cout << "=============Bola===============" << endl;
   cout << "1. Volume Bola" << endl;
   cout << "2. Luas Bola" << endl;
   cout << "================================" << endl;
   cout << "Choose your option : " << endl;
   cin >> target;

   switch (target)
   {
   case 1:
       cout << "Input jari-jari bola : ";
       cin >> r;
       cout << "Volume Bola adalah : " << (4/3) * phi * r * r * r << endl;
       break;
   case 2:
       cout << "Input jari-jari bola : ";
       cin >> r;
       cout << "Luas Bola adalah : " << 4 * phi * r * r << endl;
       break;
   default:
       cout << "Your Input doesn't match";
       break;
   }

}
