// #include <bits/stdc++.h>
// #define ll long long
// using namespace std;
// ll enumer = 0;
// ll valueOfCoins = 0;

// int main()
// {
//     ll valueOfM, n, valueOfI, valueOfJ;
//     cin >> valueOfM >> n;
//     string s;
//     vector<vector<ll>> v1(valueOfM, vector<ll>(n, 0));
//     vector<string> v(valueOfM);
//     for (valueOfI = 0; valueOfI < valueOfM; valueOfI++)
//         cin >> v[valueOfI];

//     for (valueOfI = 0; valueOfI < valueOfM; valueOfI++)
//     {
//         for (valueOfJ = 0; valueOfJ < n; valueOfJ++)
//         {
//             if (valueOfI == 0)
//             {
//                 if (v[valueOfI][valueOfJ] == 'C')
//                 {
//                     valueOfCoins++;
//                     v1[valueOfI][valueOfJ] = valueOfM - valueOfI - 1;
//                 }
//             }
//             else
//             {
//                 if (v[valueOfI][valueOfJ] == 'C')
//                 {
//                     valueOfCoins++;
//                     ll valueOfA = valueOfM - valueOfI - 1;
//                     v1[valueOfI][valueOfJ] = min(v1[valueOfI - 1][valueOfJ], -valueOfA);
//                 }
//                 else if (v[valueOfI][valueOfJ] == 'H')
//                 {
//                     if (v[valueOfI - 1][valueOfJ] == 'H')
//                         v1[valueOfI][valueOfJ] = v1[valueOfI - 1][valueOfJ];

//                     else
//                     {
//                         v1[valueOfI][valueOfJ] = valueOfM - valueOfI;
//                         if (v1[valueOfI - 1][valueOfJ] < 0)
//                         {
//                             v1[valueOfI][valueOfJ] = v1[valueOfI - 1][valueOfJ];
//                         }
//                     }
//                 }
//             }
//             for (valueOfI = 0; valueOfI < n; valueOfI++)
//             {
//                 if (v1[valueOfM - 1][valueOfI] < 0)
//                 {
//                     ll valueOfA = v1[valueOfM - 1][valueOfI];
//                     enumer += -valueOfA;
//                 }
//                 else
//                     enumer += v1[valueOfM - 1][valueOfI];
//             }
//             enumer = 2 * enumer;
//             cout << valueOfCoins << " " << enumer;
//             return 0;
//         }
//     }
// }

#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll coins = 0, ene = 0;
int main()
{
    ll m, n, i, j;
    cin >> m >> n;
    string s;
    vector<string> v(m);
    vector<vector<ll>> v1(m, vector<ll>(n, 0));
    for (i = 0; i < m; i++)
    {
        cin >> v[i];
    }
    /*for(i=0;i<n;i++){
       for(j=0;j<n;j++){
           cout<<v[i][j];
       }cout<<"\n";
    }*/
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (i == 0)
            {
                if (v[i][j] == 'C')
                {
                    coins++;
                    v1[i][j] = m - i - 1;
                }
            }
            else
            {
                if (v[i][j] == 'C')
                {
                    coins++;
                    ll a = m - i - 1;
                    v1[i][j] = min(v1[i - 1][j], -a);
                }
                else if (v[i][j] == 'H')
                {
                    if (v[i - 1][j] == 'H')
                    {
                        v1[i][j] = v1[i - 1][j];
                    }
                    else
                    {
                        v1[i][j] = m - i;
                        else if (v1[i - 1][j] < 0)
                        {
                            v1[i][j] = v1[i - 1][j];
                        }
                    }
                }
            }
            for (i = 0; i < n; i++)
            {
                if (v1[m - 1][i] < 0)
                {
                    ll a = v1[m - 1][i];
                    ene += -a;
                }
                else
                {
                    ene += v1[m - 1][i];
                }
            }
            ene = 2 * ene;
            cout << coins << " " << ene;

            return 0;
        }
    }
}