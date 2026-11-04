# coding: utf-8
"""PL05.02: real Keras 3 multi-backend demo with PyTorch, not metadata-only."""
import os
os.environ["KERAS_BACKEND"] = "torch"  # must be set before importing keras
import keras
import keras.ops as ops
import numpy as np
import torch
import h5py

assert keras.backend.backend() == "torch"
x = torch.tensor([-2.0, 0.0, 3.0], requires_grad=True)
value = ops.sum(ops.square(x))
value.backward()
torch.testing.assert_close(x.grad, torch.tensor([-4.0, 0.0, 6.0]))

keras.utils.set_random_seed(2026)
train_x = np.array([[-2.], [-1.], [0.], [1.], [2.]], dtype=np.float32)
train_y = 2 * train_x + 1
model = keras.Sequential([
    keras.Input(shape=(1,)),
    keras.layers.Dense(1, kernel_initializer="zeros", bias_initializer="zeros"),
])
model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.05), loss="mse")
initial_loss = float(model.evaluate(train_x, train_y, verbose=0))
model.fit(train_x, train_y, epochs=40, batch_size=5, shuffle=False, verbose=0)
final_loss = float(model.evaluate(train_x, train_y, verbose=0))
pred = float(model.predict(np.array([[3.]], dtype=np.float32), verbose=0)[0, 0])
assert final_loss < initial_loss * 0.05, (initial_loss, final_loss)
assert abs(pred - 7.0) < 0.3, pred
print("KERAS_TORCH_DEMO_PASS", round(initial_loss, 6), round(final_loss, 6), round(pred, 6))
