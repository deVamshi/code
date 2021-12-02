#include <iostream>

using namespace std;

int main()
{
    int n, ans;

    cout << "Enter the number: ";
    cin >> n;


    while n > 0{
        ans++;
        n = n / 10;
    }

    cout << "No of digits present :" << ans;

    return 0;
}
