keyboard = (("q,w,e,r,t,y,u,i,o,p"),
            ("a,s,d,f,g,h,i,j,k,l"),
            ("z,x,c,v,b,n,m,<,>,?"))
for row in keyboard:
    for char in row:
        print(char,end=" ")
    print()