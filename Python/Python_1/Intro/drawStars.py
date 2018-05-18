def draw_stars(arr):
    x = len(arr)
    for i in range(0,x):
        if isinstance(arr[i],int) == True:
            y = ''
            for i in range(0,arr[i]):
                y = y + '*'
            print y
        elif isinstance(arr[i],str) == True:
            y = ''
            z = arr[i]
            zz = len(z)
            for i in range(0,zz):
                y = y + z[0]
            print y.lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)