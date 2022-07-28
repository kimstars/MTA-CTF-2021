// C implementation of Sleep Sort
#include <stdio.h>
#include <windows.h>
#include <process.h>

void SleepFunc(int a1)
{
    int v1;
    if ((a1 & 1) != 0)
        v1 = 66 * a1 + 5;
    else
        v1 = a1 * (a1 % 10 + 132);
    Sleep(v1 / 5000);
}

int count = 0;

int key[24] = {0x0EA,0x0C, 0x0A5,0x13, 0x0E6,0x7E, 0x0FE, 9, 0x0AE,0x2E,0x94, 7, 0x0B8, 0x0BC,0x10, 0x132, 0x0B7, 0x16B, 0x174, 0x0D9,0x96, 0x0CC,0x94,0x151};
void routine(void *a)
{
    int n = *(int *)a;
    count++;
    printf("%d ", n ^ key[count]);
}

void sleepSort(int arr[], int n)
{

    HANDLE threads[n];

    // Create the threads for each of the input array elements
    for (int i = 0; i < n; i++)
        threads[i] = (HANDLE)_beginthread(&routine, 0, &arr[i]);

    // Process these threads
    WaitForMultipleObjects(n, threads, TRUE, INFINITE);
    return;
}

// Driver program to test above functions
int main()
{
    // Doesn't work for negative numbers
    int arr[] = {283, 171, 159, 78, 112, 299, 76, 166, 257, 145, 124, 72, 170, 300, 149, 132, 86, 231, 219, 96, 239, 224, 190, 197};
    int n = sizeof(arr) / sizeof(arr[0]);

    sleepSort(arr, n);

    return (0);
}
