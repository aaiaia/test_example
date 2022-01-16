#!/bin/bash
echo "===================================="
echo ">>>>>>>>>>>>>>>>>>>"
echo ">>> cmp file1 file2"
echo ">>>>>>>>>>>>>>>>>>>"
cmp c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> cmp -l file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>"
cmp -l c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>"
diff c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff --brief file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
diff --brief c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -c file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -c c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -d file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -d c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -r file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -r c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -H file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -H c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -u file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -u c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> diff -y file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
diff -y c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>"
colordiff c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff --brief file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
colordiff --brief c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -c file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -c c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -d file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -d c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -r file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -r c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -H file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -H c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -u file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -u c_codes/lib0.h c_codes/lib1.h
echo "===================================="

echo "===================================="
echo ">>> colordiff -y file1 file2"
echo ">>>>>>>>>>>>>>>>>>>>>>>"
colordiff -y c_codes/lib0.h c_codes/lib1.h
echo "===================================="

