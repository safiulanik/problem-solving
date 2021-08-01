#include <stdio.h>
#include <string.h>
using namespace std;

int dp[1000]; // initialize to -1 inside main()

int way(int n)
{
    if (n == 0 || n == 1)
        return 1;
    if (dp[n] != -1)
        return dp[n];
    return dp[n] = way(n - 1) + way(n - 2);
}

int main()
{
    memset(dp, -1, 1000);
    for (int i = 0; i < 10; i++)
        printf("%d\n", way(i));
    return 0;
}
