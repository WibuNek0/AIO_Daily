import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Phân tích dữ liệu từ file CSV")

uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dữ liệu ban đầu")
    st.dataframe(df.head())
    st.write("Số dòng:", df.shape[0])
    st.write("Số cột:", df.shape[1])

    st.write("Các thống kê cơ bản:")
    st.dataframe(df.describe())
    st.write("Kiểu dữ liệu:")
    st.write(df.dtypes)
    st.write("Số giá trị thiếu:")
    st.write(df.isnull().sum())

    st.subheader("Lọc dữ liệu theo nhiều cột")
    columns = df.columns.tolist()
    filter_cols = st.multiselect("Chọn cột để lọc (có thể chọn nhiều)", columns)
    filtered_df = df.copy()
    for col in filter_cols:
        vals = filtered_df[col].unique().tolist()
        selected_vals = st.multiselect(f"Chọn giá trị cho cột {col}", vals, default=vals)
        if selected_vals:
            filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]
    st.write("Dữ liệu sau khi lọc:")
    st.dataframe(filtered_df)

    st.subheader("Biểu đồ tương quan giữa các cột số")
    numeric_columns = filtered_df.select_dtypes(include='number').columns.tolist()
    if numeric_columns:
        selected_num_cols = st.multiselect("Chọn các cột số để phân tích tương quan", numeric_columns, default=numeric_columns)
        if len(selected_num_cols) > 1:
            fig, ax = plt.subplots()
            sns.heatmap(filtered_df[selected_num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.write("Vui lòng chọn ít nhất 2 cột số để vẽ heatmap.")
    else:
        st.write("Không có cột số để phân tích.")

    st.subheader("Tải dữ liệu đã lọc")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Tải dữ liệu đã lọc", data=csv, file_name="filtered_data.csv")

    # st.subheader("Phân tích dữ liệu tương tác với PygWalker")
    # pyg_html = pyg.walk(df, return_html=True)
    # components.html(pyg_html, height=1000, scrolling=True)