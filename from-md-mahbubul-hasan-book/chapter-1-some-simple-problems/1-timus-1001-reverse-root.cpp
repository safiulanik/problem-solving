#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

int main()
{
    vector<long long> v;
    long long a;
    while (scanf("%lld", &a) != EOF)
    {
        v.push_back(a);
    }
    for (int i = v.size() - 1; i >= 0; i--)
    {
        printf("%.4lf\n", sqrt(v[i]));
    }
    return 0;
}