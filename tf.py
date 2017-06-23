from keras.models import Sequential
from keras.layers import Dense, Activation

model=Sequential()
model.add(Dense(units=64, input_dim=308))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

mode.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

model.fit(xtrain,ytrain,epochs=5,batch_size=32)

model.train_on_batch(x_batch,y_batch)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
