#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdarg.h>

void printf_success(char* format, ...) {
    printf("\x1b[1;32m");
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    printf("\x1b[0m");
    return;
}

void show_usage() {
	printf("=== Management utility ===\n");
	printf_success("Usage:\n");
	printf("1. Exec /bin/bash with root privileges\n");
	printf("2. Unblock iptables OUTPUT restrictions\n");
	printf("3. Start unlocked firefox\n");
	printf("4. Add user in wheel group\n");
	printf("5. Delete already added user\n");
	printf("6. (...) More to be added?\n");
	printf("write your suggestions to /.flag.txt\n");
	return;
}

int give_me_uid(uid_t uid) {
	int ret = setuid(uid);
	if (ret == 0) {
		if (uid == 0) {
			printf("[+] We are root!\n");
			return 0;
		}
		printf_success("[+] We are uid: %i\n", uid);
	} else {
		printf("[-] FAIL: Something went wrong, setuid returned: %i\n", ret);
		exit(-1);
	}
}

void shellcode(void) {
	// Noreturn?
	give_me_uid(0);
	execve("/bin/bash", NULL, NULL);
}
int allow_send(void) {
	give_me_uid(0);
	system("/usr/sbin/iptables -P OUTPUT ACCEPT");
	system("systemctl restart iptables.service");
	printf_success("[+] Send operation: allowed\n");
	return 0;
}

void kickstart_firefox(void) {
	system("http_proxy= https_proxy= ftp_proxy= setsid firefox");
	printf_success("[+] firefox starting...\n");
	exit(0);
}

int add_wheel_user(void) {
	give_me_uid(0);
	system("/usr/sbin/useradd -N -M work");
	system("/usr/sbin/usermod -aG wheel work");
	printf("[*] System user {work} created");
	printf("[*] Setting password: {password}\n");
	system("echo 'work:password' | /usr/sbin/chpasswd");
	printf_success("[+] {work} user password: {password}\n");
	printf_success("[+] Try to enter via tty3\n");
	// DONE: Add automatic password setting
	return 0;
}

int delete_wheel_user(void) {
	give_me_uid(0);
	system("/usr/sbin/userdel work");
	printf("[*] Deleted system user: {work}\n");

	system("rm -rf /var/spool/mail/work");
	printf("[*] Removed mail\n");
	// system("rm -rf /home/work"); // I do not create home directory by default
	printf_success("[+] Done!");
	return 0;
}

int main(int argc, char const *argv[])
{
	show_usage();
	int ch = 0;
	scanf("%i", &ch);
	if (ch == 0) {
		printf("error\n");
		return -1;
	}
	else if (ch == 1) {
		shellcode();
	}
	else if (ch == 2) {
		return allow_send();
	}
	else if (ch == 3) {
		kickstart_firefox();
	}
	else if (ch == 4) {
		return add_wheel_user();
	}
	else if (ch == 5) {
		return delete_wheel_user();
	}
	else {
		printf("[-] FAIL: unk_error\n");
		return -1;
	}
}
