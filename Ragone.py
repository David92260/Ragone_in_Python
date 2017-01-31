"""
Ragone Diagram.
"""
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# x => specific energy (Wh/kg)
# y => specific power (W/kg)
x = np.arange(0,600)
y_001C = 0.01 * x
y_01C = 0.1 * x
y_1C = x
y_10C = 10 * x
y_100C = 100 * x
y_1000C = 1000 * x

fig, axs = plt.subplots()

axs.set_label('s')
plt.axis([0,600,1,100000])
plt.axhline(y=0.007, xmin=0, xmax=1, linestyle='dotted', color='0.5')
plt.xlabel('Specific Energy (Wh/kg)')
plt.ylabel('Specific Power (W/kg)')
axs.plot(x, y_001C, '0.5', linestyle='-')
axs.plot(x, y_01C, '0.5', linestyle='-')
axs.plot(x, y_1C, '0.5', linestyle='-')
axs.plot(x, y_10C, '0.5', linestyle='-')
axs.plot(x, y_100C, '0.5', linestyle='-')
axs.plot(x, y_1000C, '0.5', linestyle='-')
axs.set_yscale('log')
axs.set_title('Ragone Chart')
axs.grid(True, 'both')
plt.text(550, 7, '0.01C', color='0.5')
plt.text(550, 70, '0.1C', color='0.5')
plt.text(550, 700, '1C', color='0.5')
plt.text(550, 7000, '10C', color='0.5')
plt.text(550, 70000, '100C', color='0.5')

Path2 = mpath.Path
path2_data = [
    (Path2.MOVETO, (252, 3)),
    (Path2.LINETO, (271, 3.5)),
    (Path2.CURVE3, (220, 700)),
    (Path2.CURVE3, (117, 2300)),
    (Path2.LINETO, (100, 2000)),
    (Path2.CURVE3, (220, 300)),
    (Path2.CURVE3, (252, 3)),
    (Path2.CLOSEPOLY, (252, 3)),
    ]
codes2, verts2 = zip(*path2_data)
path2 = mpath.Path(verts2, codes2)
patch2 = mpatches.PathPatch(path2, facecolor='b', alpha=0.5)
axs.add_patch(patch2)
plt.text(190, 150, 'Li/SO2', color='k')

Path = mpath.Path
path_data = [
    (Path.MOVETO, (0, 80)),
    (Path.LINETO, (4.3, 3000)),
    (Path.CURVE3, (50, 7000)),
    (Path.CURVE3, (149, 10000)),
    (Path.LINETO, (152, 3000)),
    (Path.LINETO, (155, 3000)),
    (Path.LINETO, (155, 1500)),
    (Path.LINETO, (160, 1500)),
    (Path.LINETO, (160, 400)),
    (Path.CURVE3, (50, 200)),
    (Path.CURVE3, (0, 80)),
    (Path.CLOSEPOLY, (0, 80)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='#ff00ff', alpha=0.5)
axs.add_patch(patch)
plt.text(150, 9000, 'Thermal batteries', color='k')

Path1 = mpath.Path
path1_data = [
    (Path1.MOVETO, (410, 0.8)),
    (Path1.LINETO, (460, 0.8)),
    (Path1.CURVE3, (440, 10)),
    (Path1.CURVE3, (200, 110)),
    (Path1.LINETO, (160, 110)),
    (Path1.CURVE3, (380, 10)),
    (Path1.CURVE3, (410, 0.8)),
    (Path1.CLOSEPOLY, (410, 0.8)),
    ]
codes1, verts1 = zip(*path1_data)
path1 = mpath.Path(verts1, codes1)
patch1 = mpatches.PathPatch(path1, facecolor='g', alpha=0.5)
axs.add_patch(patch1)
plt.text(310, 12, 'Li/SOCl2 Spiral', color='k')

Path3 = mpath.Path
path3_data = [
    (Path3.MOVETO, (113.6, 0.7)),
    (Path3.LINETO, (138.6, 0.7)),
    (Path3.CURVE3, (80, 60)),
    (Path3.CURVE3, (36.4, 90)),
    (Path3.LINETO, (9.1, 90)),
    (Path3.CURVE3, (80, 20)),
    (Path3.CURVE3, (113.6, 0.7)),
    (Path3.CLOSEPOLY, (113.6, 0.7)),
    ]
codes3, verts3 = zip(*path3_data)
path3 = mpath.Path(verts3, codes3)
patch3 = mpatches.PathPatch(path3, facecolor='#ffff00', alpha=0.5)
axs.add_patch(patch3)
plt.text(15, 10.5, 'Zn/MnO2', color='k')

Path4 = mpath.Path
path4_data = [
    (Path4.MOVETO, (125, 7)),
    (Path4.LINETO, (154.5, 7)),
    (Path4.CURVE3, (125, 300)),
    (Path4.CURVE3, (86.4, 1500)),
    (Path4.LINETO, (54.5, 1500)),
    (Path4.CURVE3, (100, 200)),
    (Path4.CURVE3, (125, 7)),
    (Path4.CLOSEPOLY, (125, 7)),
    ]
codes4, verts4 = zip(*path4_data)
path4 = mpath.Path(verts4, codes4)
patch4 = mpatches.PathPatch(path4, facecolor='#babe00', alpha=0.5)
axs.add_patch(patch4)
plt.text(75, 150, 'AgO/Zn', color='k')

Path5 = mpath.Path
path5_data = [
    (Path5.MOVETO, (163.6, 1)),
    (Path5.LINETO, (190.9, 1)),
    (Path5.CURVE3, (200, 3500)),
    (Path5.CURVE3, (31.8, 10500)),
    (Path5.LINETO, (6.8, 10500)),
    (Path5.CURVE3, (170, 2000)),
    (Path5.CURVE3, (163.6, 1)),
    (Path5.CLOSEPOLY, (163.6, 1)),
    ]
codes5, verts5 = zip(*path5_data)
path5 = mpath.Path(verts5, codes5)
patch5 = mpatches.PathPatch(path5, facecolor='r', alpha=0.5)
axs.add_patch(patch5)
plt.text(30, 10000, 'Li-ion', color='k')

Path6 = mpath.Path
path6_data = [
    (Path6.MOVETO, (149, 6)),
    (Path6.LINETO, (160, 6)),
    (Path6.CURVE3, (150, 300)),
    (Path6.CURVE3, (127, 950)),
    (Path6.LINETO, (115.2, 700)),
    (Path6.CURVE3, (135, 200)),
    (Path6.CURVE3, (149, 6)),
    (Path6.CLOSEPOLY, (149, 6)),
    ]
codes6, verts6 = zip(*path6_data)
path6 = mpath.Path(verts6, codes6)
patch6 = mpatches.PathPatch(path6, facecolor='#00ffff', alpha=0.5)
axs.add_patch(patch6)
plt.text(120, 5, 'Li-Polymer', color='k')

Path7 = mpath.Path
path7_data = [
    (Path7.MOVETO, (293, 1)),
    (Path7.LINETO, (318.5, 1)),
    (Path7.CURVE3, (325, 8)),
    (Path7.CURVE3, (94, 160)),
    (Path7.LINETO, (76.8, 120)),
    (Path7.CURVE3, (305, 6)),
    (Path7.CURVE3, (293, 1)),
    (Path7.CLOSEPOLY, (293, 1)),
    ]
codes7, verts7 = zip(*path7_data)
path7 = mpath.Path(verts7, codes7)
patch7 = mpatches.PathPatch(path7, facecolor='#99ff99', alpha=0.5)
axs.add_patch(patch7)
plt.text(260, 1.5, 'Li/MnO2', color='k')

#axs.plot(225, 1650, marker='D', color='k')
#plt.text(220, 2000, 'Li-S (Sion Power)', color='k')

plt.show()
