### codemap

nc pwnable.kr 9021

srand(0)导致随机数不随机，下文的srand()也是不随机的，debug时候拿关键值即可。

复制网上有人写好的ida脚本http://blog.csdn.net/hwz2311245/article/details/50555295

```
max eax: 99879, ebx: 2c91db0,
second eax: 99679, ebx: 2011310,
third eax: 99662, ebx: 30b47e8
```


| num | eax | ebx | string |
|--|---|--|--|
| 1 | 99879  | 0x02661DB0 | X12nM7yCJcu0x5u |
| 2 | 99679  | 0x019E1310 | roKBkoIZGMUKrMb |
| 3 | 99662  | 0x02A847E8 | 2ckbnDUabcsMA2s |



```c
#include <idc.idc>

static main(){

    auto max_eax, max_ebx, second_eax, second_ebx, third_eax, third_ebx;
    auto eax, ebx;

    max_eax = 0;
    second_eax = 0;
    third_eax = 0;
    max_ebx = 0;
    second_ebx = 0;
    third_ebx = 0;

    AddBpt(0x403E65);
    StartDebugger("","","");
    auto count;
    for(count = 0; count < 999; count ++){
        auto code = GetDebuggerEvent(WFNE_SUSP|WFNE_CONT, -1);
        eax = GetRegValue("EAX");
        ebx = GetRegValue("EBX");

        if(max_eax < eax){
            third_eax = second_eax;
            third_ebx = second_ebx;
            second_eax = max_eax;
            second_ebx = max_ebx;
            max_eax = eax;
            max_ebx = ebx;
        }else if(second_eax < eax){
            third_eax = second_eax;
            third_ebx = second_ebx;
            second_eax = eax;
            second_ebx = ebx;
        }else if(third_eax < eax){
            third_eax = eax;
            third_ebx = ebx;
        }
    }
    Message("max eax: %d, ebx: %x, second eax: %d, ebx: %x, third eax: %d, ebx: %x\n", max_eax, max_ebx, second_eax, second_ebx, third_eax, third_ebx);
}
```


flag
`select_eax_from_trace_order_by_eax_desc_limit_20`
