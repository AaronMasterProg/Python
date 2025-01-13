import tensorflow as tf

# Declaramos las 2 matricez
matrizA = [1,2,-3],[4,0,2]
matrizB = [3,1],[2,4],[-1,5]

# Multiplicamos las matricez
product = tf.matmul(matrizA, matrizB)

print(product.numpy())

# Esta era la forma en que se declaraba la salida para Tensorflow version 1.X
# Actualmente esta descontinuada esta forma y solo se usa print con numpy
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()
