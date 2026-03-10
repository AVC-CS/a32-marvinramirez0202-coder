#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  int numFemale, numMale, numOthers;
  double percF, percM, percO;
  double total;

  cout << "Enter the number of students: Male, Female and Others";
  cin >> numMale >> numFemale >> numOthers;
  // TODO

  total = numMale + numFemale + numOthers;
  percM = (numMale / total) * 100;
  percF = (numFemale / total) * 100;
  percO = (numOthers / total) * 100;

  cout << fixed << setprecision(2);
  cout << "Percentage of Male: " << percM << endl;
  cout << "Percentage of Female: " << percF << endl;
  cout << "Percentage of Others: " << percO << endl;
}
