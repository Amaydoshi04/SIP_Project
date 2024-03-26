import streamlit as st

st.set_page_config(page_title="Canny Edge Detection", page_icon="", layout="wide")
st.title("Canny Edge Detection")
st.markdown("##### R004 - R006 -R007")



with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### Original Image")
            image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
            if image:
                st.image(image, caption="Uploaded Image", use_column_width=True)

    with col2:
        st.markdown("### Canny Edge Detection")
        if st.button("Detect Edges"):
            st.write("Edge detected image will be displayed here.")
