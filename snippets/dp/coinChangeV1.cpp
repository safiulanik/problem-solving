#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    bool possible[1000];
    memset(possible, false, 1000);
    possible[0] = 1;
    int coin[3] = {4, 7, 10};
    int n = 16, k = 3;
    for (int i = 1; i <= n; i++)
        for (int j = 0; j < k; j++)
            if (i >= coin[j])
                possible[i] |= possible[i - coin[j]];
    for (int i = 1; i <= n; i++)
        printf("%d: %d\n", i, possible[i]);
    return 0;
}
