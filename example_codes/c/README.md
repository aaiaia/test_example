# Test sequence
## Shared library
1. Sequence(shell)
```bash
$ gcc -c SharedTest_0.c -I.
$ gcc -c SharedTest_1.c -I.
$ gcc -shared -fPIC -o libSharedTest.so SharedTest_0.o SharedTest_1.o
$ gcc -c AppTest.c -I.
$ gcc -o AppTestSharedLib AppTest.o -L. -lSharedTest
```

2. Set Env. and Run App
```bash
$ export LD_LIBRARY_PATH=./
$ ./AppTest
```

3. Console log
```bash
$ ./AppTest
arg[0] ./AppTest
add_0
4 + 2 = 6
sub_0
4 - 2 = 2
mul_0
4 * 2 = 8
div_0
4 / 2 = 2
add_1
4 + 2 = 6
sub_1
4 - 2 = 2
mul_1
4 * 2 = 8
div_1
4 / 2 = 2
```

4. Dependency Check
```bash
$ ll *.so
-rwxrwxrwx 1 pleya pleya 16456 Jan 13 18:19 libSharedTest.so*
$ mv libSharedTest.so _libSharedTest.o
$ ./AppTest
./AppTest: error while loading shared libraries: libSharedTest.so: cannot open shared object file: No such file or directory
```

5. Function list
```bash
$ nm ./libSharedTest.so
0000000000003e20 d _DYNAMIC
0000000000004000 d _GLOBAL_OFFSET_TABLE_
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
0000000000002210 r __FRAME_END__
0000000000002038 r __GNU_EH_FRAME_HDR
0000000000004028 d __TMC_END__
                 w __cxa_finalize@@GLIBC_2.2.5
00000000000010d0 t __do_global_dtors_aux
0000000000003e18 d __do_global_dtors_aux_fini_array_entry
0000000000004020 d __dso_handle
0000000000003e10 d __frame_dummy_init_array_entry
                 w __gmon_start__
0000000000001254 t _fini
0000000000001000 t _init
0000000000001119 T add_0
00000000000011b5 T add_1
0000000000004028 b completed.8060
0000000000001060 t deregister_tm_clones
000000000000118e T div_0
000000000000122a T div_1
0000000000001110 t frame_dummy
0000000000001167 T mul_0
0000000000001203 T mul_1
                 U puts@@GLIBC_2.2.5
0000000000001090 t register_tm_clones
0000000000001141 T sub_0
00000000000011dd T sub_1
```

## Static library

1. Sequence(shell)
```bash
$ gcc -c SharedTest_0.c -I.
$ gcc -c SharedTest_1.c -I.
$ ar rv -o libStaticTest.a SharedTest_0.o SharedTest_1.o
$ gcc -c AppTest.c -I.
$ gcc -o AppTestStaticLib AppTest.o -L. -lStaticTest
```

2. Function list
```bash
$ nm ./libSharedTest.a
SharedTest_0.o_normal:
                 U _GLOBAL_OFFSET_TABLE_
0000000000000000 T add_0
0000000000000075 T div_0
000000000000004e T mul_0
                 U puts
0000000000000028 T sub_0
 
SharedTest_1.o:
                 U _GLOBAL_OFFSET_TABLE_
0000000000000000 T add_1
0000000000000075 T div_1
000000000000004e T mul_1
                 U puts
0000000000000028 T sub_1
```
