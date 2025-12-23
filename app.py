import streamlit as st
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="Image Button App", page_icon="🌄")

# عنوان رئيسي
st.title("زر + صورة 🔥")

# تحميل الصورة
img_path = "كيفك.jfif"  # بدلي هنا باسم الصورة ديالك
img = Image.open(img_path)

# الزر
if st.button("اضغط هنا"):
    st.image(img, caption="هادي الصورة ديالك 😎", use_column_width=True)
