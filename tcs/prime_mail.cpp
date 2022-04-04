#include <iostream>
using namespace std;

bool primeKanuko(int nValue)
{
    if (nValue == 1 || nValue == 0)
        return false;
    for (int iValue = 2; iValue < nValue; iValue++)
    {
        if (nValue % iValue == 0)
            return false;
    }
    return true;
}

int main()
{
    int valueOfCounter = 0;
    int nValue;
    int fValue = 1;
    int iValue;
    cin >> nValue;
    while (nValue > 1)
    {
        valueOfCounter = 0;
        fValue = fValue + 1;
        for (iValue = 1; iValue <= nValue; iValue++)
        {
            if (primeKanuko(iValue))
                valueOfCounter += 1;
        }
        nValue = nValue - valueOfCounter;
    }
    cout << fValue;
}
