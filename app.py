import streamlit as st

def main():
    st.title('Birthday Wishes ')
    st.markdown('### my warm wishes to my friend Naveen!')

    # Specify the path to your friend's image file
    image_path = 'WhatsApp.jpeg'  # Replace with your actual file path

    # Display the image
    st.image(image_path, caption='Your friend', use_column_width=True)

    # Birthday message textarea
    st.markdown('### Happy BirthDay My dear friend live a happy life and party hard')
    birthday_message = st.text_area('Message', 'Happy Birthday! Wishing you a fantastic year ahead.')

    # Sender's name input
    sender_name = st.text_input('Venkatesh', '')


if __name__ == '__main__':
    main()
