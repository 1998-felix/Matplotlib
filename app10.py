import matplotlib.pyplot as pt

t = range(0, 20)
s = range(30, 10, -1)

grid_size = '22'

figure = pt.figure()
position = grid_size + '1'
print("Adding subplot 1 with position,", position)
axis1 = figure.add_subplot(int(position))
axis1.set(title='subplot 2,2,1')
axis1.plot(t, s)

position = grid_size + '2'
print("Adding subplot 2 with position,", position)
axis2 = figure.add_subplot(int(position))
axis2.set(title="subplot 2,2,2")
axis2.plot(t, s)

position = grid_size + '3'
print("Adding subplot 3 with position,", position)
axis3 = figure.add_subplot(int(position))
axis3.set(title='subplot 2,2,3')
axis3.plot(t, s)

position = grid_size + '4'
print("Adding subplot 4 with position,", position)
axis4 = figure.add_subplot(int(position))
axis4.set(title="subplot 2,2,4")
axis4.plot(t, s)

pt.show()
