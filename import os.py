# this is a work with "os" module. Hope it will help me in the future

# lets start: import os module
import os


# here we goo! Printing system. My system is posix == macOS
print("system:", os.name)

# print curent user(NOT NAME!) My is "root" because i logged in as root(Ghh-jb)
print(os.getlogin())

# print pid(Process identifier). Very simple/.
print(os.getpid())

# this is more complicated:/ "posix.uname_result"
# sysname, nodename(MacBook-Air---Ghh.local), release, version(kernel), root(XNU), machine(x86_64)
print(os.uname())

# os.access - check if file exists, r/w/x permissions check. Lol better to usse chmod but still. Useful thing:)
print(os.access("/Users/overlord/dualra1n/dualboot.sh", os.X_OK))
# flags instead os.X_OK :
# os.F_OK == if file exist -> BOOL
# os.R_OK == if file readable -> BOOL
# os.W_OK == if file writable -> BOOL
# os.X_OK == if file executable -> BOOL

# os.chdir and os.getcwd
# os.chdir is changind directory(cd)
# os.getcwd is used to get working dir(pwd)
print(os.getcwd()) # this will show the directory OF THE FILE! NOT OF THE USER!
os.chdir("../")
print(os.getcwd())
os.chdir("./dualra1n")
print(os.getcwd())
os.chdir("../wing")

# os.listdir print list of files in directory(ls)
print(os.listdir("../dualra1n"))

# os.mkdir create directory(mkdir)
os.mkdir("../dualra1n/iPhone_8.4_64bit") #if dir exist, will fail with OSError
print(os.listdir("../dualra1n"))
# also try with mkdirs:)
os.rmdir("../dualra1n/iPhone_8.4_64bit") #remove !!!EMPTY!!! dirs
# also try with rmdirs



# os.rename(src, dst) # rename files and dirs easy:)

# exec system cmd
os.system("moon-buggy") 


# # os.system - run cmd from system(for ex. pwd - print working directory)
# print(os.system("pwd"))
# # "0" means no error
# # "1" == error


# os.chmod and os.chown are simple i will only show the syntax
# path = "/Users/overlord/dualra1n/dualboot.sh"
# mode = 777
# os.chmod(path, mode, dir_fd = None, effective_ids=False, follow_symlinks=True) sama in chown:)


# os.link == make a hardlink 
# os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
# os.symlink == make a symlink. Syntax as in hardlink  
# os.system("rmdir ../dualra1n/iPhone_8.4_64bit")