#include <stdio.h>
#include <stdint.h>

typedef void(*FuncType0)(void);
#define FUNCTYPE_LEN    16u

static FuncType0 funcType0_addrChk = 0ul;
void type0_func00(void) {
    funcType0_addrChk = type0_func00;
    printf("[info] func addr:0x%p\r\n", type0_func00);
}
void type0_func01(void) {
    funcType0_addrChk = type0_func01;
    printf("[info] func addr:0x%p\r\n", type0_func01);
}
void type0_func02(void) {
    funcType0_addrChk = type0_func02;
    printf("[info] func addr:0x%p\r\n", type0_func02);
}
void type0_func03(void) {
    funcType0_addrChk = type0_func03;
    printf("[info] func addr:0x%p\r\n", type0_func03);
}
void type0_func04(void) {
    funcType0_addrChk = type0_func04;
    printf("[info] func addr:0x%p\r\n", type0_func04);
}
void type0_func05(void) {
    funcType0_addrChk = type0_func05;
    printf("[info] func addr:0x%p\r\n", type0_func05);
}
void type0_func06(void) {
    funcType0_addrChk = type0_func06;
    printf("[info] func addr:0x%p\r\n", type0_func06);
}
void type0_func07(void) {
    funcType0_addrChk = type0_func07;
    printf("[info] func addr:0x%p\r\n", type0_func07);
}
void type0_func08(void) {
    funcType0_addrChk = type0_func08;
    printf("[info] func addr:0x%p\r\n", type0_func08);
}
void type0_func09(void) {
    funcType0_addrChk = type0_func09;
    printf("[info] func addr:0x%p\r\n", type0_func09);
}
void type0_func10(void) {
    funcType0_addrChk = type0_func10;
    printf("[info] func addr:0x%p\r\n", type0_func10);
}
void type0_func11(void) {
    funcType0_addrChk = type0_func11;
    printf("[info] func addr:0x%p\r\n", type0_func11);
}
void type0_func12(void) {
    funcType0_addrChk = type0_func12;
    printf("[info] func addr:0x%p\r\n", type0_func12);
}
void type0_func13(void) {
    funcType0_addrChk = type0_func13;
    printf("[info] func addr:0x%p\r\n", type0_func13);
}
void type0_func14(void) {
    funcType0_addrChk = type0_func14;
    printf("[info] func addr:0x%p\r\n", type0_func14);
}
void type0_func15(void) {
    funcType0_addrChk = type0_func15;
    printf("[info] func addr:0x%p\r\n", type0_func15);
}

static FuncType0 funcType0_list[FUNCTYPE_LEN] = {
    type0_func00,       type0_func01,       type0_func02,       type0_func03,
    type0_func04,       (FuncType0)NULL,    type0_func06,       type0_func07,
    type0_func08,       type0_func09,       type0_func10,       (FuncType0)NULL,
    type0_func12,       type0_func13,       type0_func14,       type0_func15,
};

int main(int argc, char* argv[]) {
    printf("argc:%d\n", argc);
    for(unsigned int ui=0u; ui<argc; ui++) {
        printf("%s ", argv[ui]);
    }
    printf("\n");

    for(unsigned int ui=0u; ui<FUNCTYPE_LEN; ui++) {
        funcType0_addrChk = (FuncType0)NULL;
        printf("[info] idx:%02u, in list func addr:0x%p\n", ui, funcType0_list[ui]);
        if(funcType0_list[ui] != (FuncType0)NULL) {
            funcType0_list[ui]();
        } else {
            printf("[info] func pointer is NULL(=0x%p)\n", funcType0_list[ui]);
        }
        printf("[info] call function is \"%s\"\n", (funcType0_addrChk == funcType0_list[ui]?"OK":"NOT OK"));
    }
    return 0;
}
