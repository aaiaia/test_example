#include <stdio.h>
#include <stdint.h>

typedef struct {
    uint32_t b1m0:1;            //[0:0]
    uint32_t b1m1:1;            //[1:1]
    uint32_t b2m2:2;            //[3:2]
    uint32_t :4;                //[7:4]
    uint32_t b8m3:8;            //[15:8]
    uint32_t b16m4:16;          //[32:16]
} test_struct_0_s;

typedef struct {
    uint32_t :4;            //[3]
    uint32_t b4_exclusive:4;    //[7:4]
    uint32_t :24;          //[32:8]
} test_struct_0_exc_s;

typedef struct {
    uint32_t b4RSVD0:4;         //[3:0]
    uint32_t b4m0:4;            //[7:4]
    uint32_t u24bRSVD1:24;      //[31:8]
} test_struct_1_s;

typedef union test_type{
    uint32_t value;
    test_struct_0_s fld0;
    test_struct_1_s fld1;
}test_type_u;

typedef union {
    uint32_t value;
    test_struct_0_s     base;
    test_struct_0_exc_s exclusive;
} test_type_exclusive;

int main(int argc, char* argv[]) {
    uint32_t t_val0;
    uint32_t t_val1_exclusive;
    test_struct_0_exc_s* p_exclusive;

    t_val0 = ((test_type_u){            \
                .fld0.b1m0=1u,          \
                .fld0.b1m1=0u,          \
                .fld0.b2m2=2u,          \
                .fld0.b8m3=0u,          \
                .fld0.b16m4=0xDEEDu,}   \
            ).value;
    printf("[non overlapped]    t_val0=0x%08x\r\n", t_val0);

    t_val0 = ((test_type_u){   \
                .fld0.b1m0=1u,          \
                .fld0.b1m1=0u,          \
                .fld0.b2m2=2u,          \
                .fld0.b8m3=0u,          \
                .fld0.b16m4=0xDEEDu,    \

                .fld1.b4m0=0xA,}        \
            ).value;
    printf("[overlapped]        t_val0=0x%08x\r\n", t_val0);

    t_val1_exclusive = ((test_type_exclusive){  \
                .base.b1m0=1u,                  \
                .base.b1m1=0u,                  \
                .base.b2m2=2u,                  \
                .base.b8m3=0u,                  \
                .base.b16m4=0xDEEDu,}           \
            ).value;
    printf("[exclusive, base]   t_val1_exclusive=0x%08x\r\n", t_val1_exclusive);
    p_exclusive = (test_struct_0_exc_s*)(&t_val1_exclusive);
    (p_exclusive->b4_exclusive) = 0xAu;
    printf("[mod exclusive]     t_val1_exclusive=0x%08x\r\n", t_val1_exclusive);

    return 0;
}
