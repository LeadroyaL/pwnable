## checksec种类

在gdb-peda里，我们使用checksec可以看到当前程序的保护，有一下五条（随便找了一个程序）
- CANARY    : ENABLED
- FORTIFY   : disabled
- NX        : ENABLED
- PIE       : disabled
- RELRO     : Partial

### CANARY
CANARY意为金丝雀保护，主要为了防止栈溢出。

目的是在call一个function的时候，先在stack上存一个FLAG，在运行结束的时候再去check FLAG，若相同，则表示通过了校验；不同的话，程序就会炸掉。

通常这个无法绕过，除非泄露了CANARY的值。

### FORTIFY

### NX

### PIE

### RELRO

#### 参考文献
