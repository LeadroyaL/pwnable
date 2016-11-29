### random

问题在于直接使用了stdio.h的rand()，返回结果是1804289383

exp:
`python -c "print 1804289383^0xdeadbeef" | ./random`


flag:
`Mommy, I thought libc random is unpredictable...`
