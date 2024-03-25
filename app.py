import streamlit as st

from genai import write_caption


def show_app():
    """
    App Page
    """

    # initialise the session state
    st.session_state["input_image"] = None
    st.session_state["state"] = (
        "initial"  # initial, image_selected, generate_caption, caption_generate_complete
    )
    st.session_state["generated_caption"] = None

    with st.container():
        st.title("📸 Insta Caption Generator")

        st.header("1️⃣ Select an Image")

        image_upload, image_camera = None, None

        file_upload, camera_input = st.tabs(["File Upload", "Camera Input"])

        # Tab - File Upload
        with file_upload:
            image_camera = st.file_uploader(
                "Choose an image file",
                type=["jpg", "jpeg", "png"],
                accept_multiple_files=False,
            )

        # Tab - Camera Input
        with camera_input:
            image_upload = st.camera_input("Take a picture", label_visibility="hidden")

        # if image is available via one of file upload or camera input, update the session state and display the image 
        if image_upload or image_camera:
            st.session_state["state"] = "image_selected"
            st.session_state["input_image"] = image_upload or image_camera
            st.image(st.session_state["input_image"], use_column_width=True)

        st.header("2️⃣ Generate Caption")
        st.caption("Powered by Google Gemini ✨")

        # if button clicked, set the state as 'generate_caption'
        if st.button("✨ Generate Caption", use_container_width=True, type="primary", disabled=st.session_state["state"] != "image_selected"):
            st.session_state["state"] = "generate_caption"

        # if state is set as 'generate_caption', generate caption using long running process behind the spinner
        if st.session_state["state"] == "generate_caption":
            with st.spinner("Generating caption..."):
                st.session_state["generated_caption"] = write_caption(
                    st.session_state["input_image"].getvalue(),
                    st.session_state["input_image"].type,
                )
                st.session_state["state"] = "caption_generate_complete"

        st.divider()

        # if completed, display the result along with flying balloons
        if st.session_state["state"] == "caption_generate_complete":
            st.caption("✨ Generated Caption")
            st.markdown(st.session_state["generated_caption"])
            st.balloons()
