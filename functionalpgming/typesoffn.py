def add(**args):
    print(args)
    res=0
    for k,v in args.items():
        res+=v
        print(res)



add(a=12,b=13,c=14)