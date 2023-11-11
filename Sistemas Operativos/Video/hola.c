#include<windows.h>
#include<stdio.h>

int main(void){
    int value = MessageBoxW(
        NULL,
        L"My firsts Message",
        L"Hello World",
        MB_YESNOCANCEL | MB_ICONEXCLAMATION
    );
    printf("%d",value);
    return EXIT_SUCCESS;
}