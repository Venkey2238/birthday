import streamlit as st

def main():
    st.title('Birthday Wishes App')
    st.markdown('### Send your warm wishes to your friend!')

    # Specify the path to your friend's image file
    image_path = 'WhatsApp.jpeg'  # Replace with your actual file path

    # Display the image
    st.image(image_path, caption='Your friend', use_column_width=True)

    # Birthday message textarea
    st.markdown('### Happy BirthDay My dear friend live a happy life and party hard')
    birthday_message = st.text_area('Message', 'Happy Birthday! Wishing you a fantastic year ahead.')

    # Sender's name input
    sender_name = st.text_input('Venkatesh', '')

    # Display the message and sender's name
    if st.button('Send Wishes'):
        if birthday_message and sender_name:
            st.success(f"Dear {sender_name}, your message: '{birthday_message}' has been sent to your friend!")

if __name__ == '__main__':
    main()
