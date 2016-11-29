### input

和pwn没啥关系，就是用各种方法去过掉check


附：别人成功的脚本http://rickgray.me/2015/07/24/toddler-s-bottle-writeup-pwnable-kr.html

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main() {
    char* argv[101] = {[0 ... 99] = "A"};
    argv['A'] = "\x00";
    argv['B'] = "\x20\x0a\x0d";
    argv['C'] = "31337";

    char* envp[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe"};

    int pipe1[2], pipe2[2];
    if(pipe(pipe1) < 0 || pipe(pipe2) < 0) {
        printf("pipe error!\n");
        exit(-1);
    }

    FILE* fp = fopen("\x0a", "wb");
    if(!fp) {
        printf("file create error!\n");
        exit(-1);
    }
    fwrite("\x00\x00\x00\x00", 4, 1, fp);
    fclose(fp);

    if(fork() == 0) {
        // Parent processing
        printf("Parent processing is here...\n");
        dup2(pipe1[0], 0);
        close(pipe1[1]);

        dup2(pipe2[0], 2);
        close(pipe2[1]);

        execve("/home/input/input", argv, envp);
    } else {
        // Child processing
        printf("Parent processing is here...\n");
        write(pipe1[1], "\x00\x0a\x00\xff", 4);
        write(pipe2[1], "\x00\x0a\x02\xff", 4);

        sleep(30);
    }


    return 0;
}
```

```python
python -c "print '\xde\xad\xbe\xef'" | nc 127.0.0.1 31337
```

flag
`Mommy! I learned how to pass various input in Linux :)`
