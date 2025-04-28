import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Bài 1: Vẽ đồ thị hàm số cơ bản
def draw_basic_function():
    x = np.linspace(-10, 10, 400)
    y = np.sin(x)  # Thay đổi hàm tại đây nếu cần
    fig, ax = plt.subplots()
    ax.plot(x, y, label='sin(x)')
    ax.set_title('Đồ thị hàm sin')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.legend()
    st.pyplot(fig)

# Bài 2: So sánh 2 hàm số trên cùng một biểu đồ
def compare_two_functions():
    x = np.linspace(-10, 10, 400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='sin(x)')
    ax.plot(x, y2, label='cos(x)')
    ax.set_title('So sánh hàm sin và cos')
    ax.set_xlabel('x')
    ax.set_ylabel('Giá trị hàm')
    ax.legend()
    st.pyplot(fig)

# Bài 3: Vẽ đồ thị hàm bậc 2
def draw_quadratic_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    ax.set_title('Đồ thị hàm bậc 2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    st.pyplot(fig)

# Bài 4: Tương tác với Slider để khảo sát đồ thị
def interactive_slider():
    a = st.slider('Chọn giá trị a', -10.0, 10.0, 1.0)
    b = st.slider('Chọn giá trị b', -10.0, 10.0, 0.0)
    c = st.slider('Chọn giá trị c', -10.0, 10.0, 0.0)
    draw_quadratic_function(a, b, c)

# Bài 5: Vẽ Heatmap cho hàm z = x² + y²
def draw_heatmap():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    fig, ax = plt.subplots()
    sns.heatmap(Z, ax=ax, cmap='viridis')
    ax.set_title('Heatmap cho hàm z = x² + y²')
    st.pyplot(fig)

# Gọi các hàm để hiển thị
st.title('Các bài tập vẽ đồ thị')
draw_basic_function()
compare_two_functions()
interactive_slider()
draw_heatmap()