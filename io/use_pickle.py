# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
import pickle
d = dict(name='Bob', age=20, score=86)
p = pickle.dumps(d)
print(p)
