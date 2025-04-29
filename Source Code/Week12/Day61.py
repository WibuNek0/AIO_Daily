import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("data/advertising.csv")
X = df[["TV", "Radio", "Newspaper"]].values
y = df["Sales"].values.reshape(-1, 1)

X = (X - X.mean(axis=0)) / X.std(axis=0)

def train_linear_regression(X, y, lr=0.01, epochs=100):
    # Khởi tạo trọng số và bias
    n_samples, n_features = X.shape
    w = np.zeros((n_features, 1))
    b = 0
    loss_history = []
    
    # Gradient Descent
    for epoch in range(epochs):
        # y_hat = X.w + b
        y_pred = np.dot(X, w) + b
        
        # MSE
        loss = np.mean((y_pred - y) ** 2)
        loss_history.append(loss)
        
        # Tính gradient của w và b
        dw = (2/n_samples) * np.dot(X.T, (y_pred - y))
        db = (2/n_samples) * np.sum(y_pred - y)
        
        # Cập nhật trọng số và bias
        w -= lr * dw
        b -= lr * db
        
    return w, b, loss_history

st.title("Huấn luyện Linear Regression với Numpy")

lr = st.slider("Learning rate", 0.001, 0.1, 0.01)
epochs = st.slider("Số epoch", 10, 1000, 200)

if st.button("Train model"):
    w, b, loss_history = train_linear_regression(X, y, lr, epochs)

    st.subheader("Loss theo epoch")
    fig, ax = plt.subplots()
    ax.plot(loss_history)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("MSE Loss")
    st.pyplot(fig)

    st.write("Trọng số cuối cùng (w):", w.flatten())
    st.write("Bias (b):", b)