import h5py


f = h5py.File('path/filename.h5', 'r')
for k in f.keys():
    print(k)

b = f['bndbox']
i = f['imgname']
p = f['part']
print(b.shape)
print(i.shape)
print(p.shape)
