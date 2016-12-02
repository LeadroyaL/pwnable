#include <error.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include<stdio.h>
int main(){
	char * s =  "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong";
	int fd = syscall(2,s, O_RDONLY);
	if(fd==-1)
		printf("error");
	char buf[1024];
	syscall(0,fd,buf,1024);
	syscall(1,1,buf,1024);
//	int fd = open(s,O_RDONLY);
//	read(fd,buf,1024);
//	write(1,buf,1024);
//	close(fd);
	return 0;
}
