Y=(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))


# Now Let's Pass a factorial function in this recursion function :

fd=lambda f: lambda yt: (1 if yt<2 else yt*f(yt-1))
print(Y(fd)(5))

