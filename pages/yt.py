from pytube import YouTube
import streamlit as st

st.title("Youtube Downloader :smile:")

st.subheader("Enter the link of the youtube video")
query = st.text_input("")
bt = st.button('Download')
if bt:
    st.video(query)
    yt = YouTube(query,use_oauth=True,
             allow_oauth_cache=True)
    # Filter for audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    # Download audio
    audio_stream.download(filename=f'{yt.title}.mp3')
    st.write("Audio downloaded!")
    st.audio(f"{yt.title}.mp3")