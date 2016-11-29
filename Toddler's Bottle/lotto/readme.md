### lotto

问题出在这段，本来char[6]和char[6]比较只需要6次，他比较了36次，目标是让match=6
```c
for(i=0; i<6; i++){
        for(j=0; j<6; j++){
                if(lotto[i] == submit[j]){
                        match++;
                }
        }
}
```
lotto[]是纯随机的，submit[]可控，当后者是6个一样的时候，随便碰上一个就可以让match=6


禁用缓冲的部署方法：`socat tcp-listen:7890,fork exec:"stdbuf -i0 -o0 -e0 ./lotto"`

flag:
`sorry mom... I FORGOT to check duplicate numbers... :(`
