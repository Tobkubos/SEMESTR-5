import tensorflow as tf           #ladowanie biblioteki
mnist = tf.keras.datasets.mnist


(x_train, y_train),(x_test, y_test) = mnist.load_data()     # ladowanie zbioru uczaczego i testowego
x_train, x_test = x_train / 255.0, x_test / 255.0           # normalizacja danych

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),            # 1 warstwa, splaszcza do wektora jednowymiarowego
  tf.keras.layers.Dense(128, activation='relu'),            # 2 warstwa, neuron kazdy z kazdym, 128 neuronow
  tf.keras.layers.Dropout(0.2),                             # 3 warstwa, wylacza losowe 20% neuronow
  tf.keras.layers.Dense(10, activation='softmax')           # 4 warstwa, 10 neuronow, finalny wynik 0-9 jako prawdopodobienstwo dzieki softmax
])

model.compile(optimizer='adam',                             # optymalizacja gradientowa
  loss='sparse_categorical_crossentropy',                   # funkcja bledu
  metrics=['accuracy'])                                     # wynik procentowy skutecznosci modelu

model.fit(x_train, y_train, epochs=5)                       # ladowanie danych do modelu
model.evaluate(x_test, y_test)                              # uruchomienie

