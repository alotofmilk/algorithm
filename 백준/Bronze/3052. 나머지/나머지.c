#include<stdio.h>

int main()

{

    int arr[10];

    int arr2[42] = { 0, };

    int i;

    int num = 0;//입력한 수를 42로 나눈 나머지값(인덱스로사용)

    int cnt = 0;

    for (i = 0; i < 10; i++)

    {

        scanf(" %d", &arr[i]);

        num = arr[i] % 42;

        arr2[num]++;

    }

    for (i = 0; i < 42; i++)

    {

        if (arr2[i]>0)

            cnt++;

    }

    printf("%d", cnt);

    

}
