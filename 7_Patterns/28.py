    #      *
    #     * *
    #    * * *
    #   * * * *
    #  * * * * *
    #   * * * *
    #    * * *
    #     * *
    #      *



n=5
for i in range(0,2*n):
    if i<n:
         x=i
    else:
         x=n-(i-n)   

    y=n-x

    for k in range(0,y):
         print(' ',end='')

    for j in range(0,x):
         print('* ',end='')
    print('')
