from turtle import *

screensize(10_000, 10_000)
tracer(0)
lt(90)
m = 10

for i in range(2):
    fd(25 * m)
    rt(90)
    fd(10 * m)
    rt(90)

fd(3 * m)
lt(90)
fd(15 * m)
rt(90)

for i in range(2):
    fd(9 * m)
    rt(90)
    fd(32 * m)
    rt(90)

update()
done()
