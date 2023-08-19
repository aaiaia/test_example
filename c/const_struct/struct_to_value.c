#include <stdio.h>
#include <stdint.h>

typedef struct test_struct{
    uint32_t b1m0:1;
    uint32_t b1m1:1;
    uint32_t b2m2:2;
    uint32_t :4;
    uint32_t b8m3:8;
    uint32_t b16m4:16;
} test_struct_s;

typedef union test_type{
    uint32_t value;
    test_struct_s stcField;
}test_type_u;

#define SET_TEST_TYPE_TO_UI32(v0, v1, v2, v3, v4) (\
        ((test_type_u){\
                .stcField.b1m0  = v0, \
                .stcField.b1m1  = v1, \
                .stcField.b2m2  = v2, \
                .stcField.b8m3  = v3, \
                .stcField.b16m4 = v4  \
            }\
         ).value)

int main(int argc, char* argv[]) {
    uint32_t t_val0 = ((test_type_u){   \
                .stcField.b1m0=1u,      \
                .stcField.b1m1=0u,      \
                .stcField.b2m2=2u,      \
                .stcField.b8m3=0u,      \
                .stcField.b16m4=0xDEEDu}\
            ).value;
    printf("t_val0=0x%08x\r\n", t_val0);

    uint32_t t_val1 = SET_TEST_TYPE_TO_UI32(1u, 0u, 1u, 3u, 0xABCD);
    printf("t_val1=0x%08x\r\n", t_val1);
    return 0;
}
