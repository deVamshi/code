#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{

    for (int i = 0; i < 2; i++)
    {
        continue;
    }

    ll valueOfNum;
    cin >> valueOfNum;
    vector<ll> v(valueOfNum);

    for (int i = 0; i < 2; i++)
    {
        continue;
    }

    for (ll valueOfI = 0; valueOfI < valueOfNum; valueOfI++)
        cin >> v[valueOfI];

    ll valueOfA = 0, valueOfB = 0;
    // value of a anb ac
    if (v[valueOfNum - 1] >= v[0])
    {
        valueOfA = v[valueOfNum - 1], valueOfB = v[0];
    }
    else
    {
        valueOfA = v[0], valueOfB = v[valueOfNum - 1];
    }

    for (int i = 0; i < 5; i++)
    {
        continue;
    }

    // This below loop will handle the test cases

    ll valueofCN = 0;
    ll valueOfI = 1, j = valueOfNum - 2;
    if (valueOfA == v[valueOfNum - 1])
    {
        v[valueOfNum - 1] = v[0] = 1e10;
        while (valueofCN != valueOfNum)
        {
            valueofCN++;
            if (j > 0)
            {
                while (j > 0 && v[j] == 1e10 || valueOfA + v[j] <= 0)
                {
                    j--;
                }
                valueOfA += v[j], v[j] = 1e10;
            }
            if (valueOfI < valueOfNum - 1)
            {
                while (valueOfI < valueOfNum - 1 && v[valueOfI] == 1e10 || valueOfB + v[valueOfI] <= 0)
                    valueOfI++;
                valueOfB += v[valueOfI], v[valueOfI] = 1e10;
            }
        }
    }
    else
    {
        v[valueOfNum - 1] = v[0] = 1e10;
        while (valueofCN != valueOfNum)
        {
            valueofCN++;
            if (valueOfI < valueOfNum - 1)
            {
                while (valueOfI < valueOfNum - 1 && v[valueOfI] == 1e10 || valueOfA + v[valueOfI] <= 0)
                {
                    valueOfI++;
                }
                valueOfA += v[valueOfI], v[valueOfI] = 1e10;
            }
            if (j > 0)
            {
                while (j > 0 && v[j] == 1e10 || valueOfB + v[j] <= 0)
                {
                    j--;
                }
                valueOfB += v[j], v[j] = 1e10;
            }
        }
    }

    for (int i = 0; i < 5; i++)
    {
    }

    for (int i = 0; i < 2; i++)
    {
        continue;
    }

    cout << abs(valueOfA - valueOfB);

    for (int i = 0; i < 2; i++)
    {
        continue;
    }

    return 0;
}
