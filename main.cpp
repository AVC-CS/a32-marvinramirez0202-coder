#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  int numFemale, numMale, numOthers;
  double percF, percM, percO;

  cout << "Enter the number of students: Male, Female and Others";
  cin >> numMale >> numFemale >> numOthers;
  // TODO
  percM = float(numMale) / (numFemale + numMale + numOthers) * 100;
  percF = float(numFemale) / (numFemale + numMale + numOthers) * 100;
  percO = float(numOthers) / (numFemale + numMale + numOthers) * 100;
  // END TODO

  cout << setprecision(2) << fixed;
  cout << "Percentage of Male: " << percM << endl;
  cout << "Percentage of Female: " << percF << endl;
  cout << "Percentage of Others: " << percO << endl;
}
