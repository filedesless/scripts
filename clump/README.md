# Clump

This small program aggregates lines fed in standard input with an optional delimiter (defaults to a space).

Here are some examples:

```
filedesless@AirBook:~$ cat test.txt 
a a
a b
a c
b a
b b
c a
c b
filedesless@AirBook:~$ cat test.txt | ./clump 
a a b c
b a b
c a b
filedesless@AirBook:~$ cat test.txt | tr ' ' '/' 
a/a
a/b
a/c
b/a
b/b
c/a
c/b
filedesless@AirBook:~$ cat test.txt | tr ' ' '/' | ./clump /
a/a/b/c
b/a/b
c/a/b
```