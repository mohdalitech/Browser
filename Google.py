import streamlit as st
import requests
st.title("Open Website Without Browser")
tld=[".com",".org",".net",".edu",".gov",".mil",".io",".ai",".co",".in"]
websiteName=st.text_input("Enter name of website:",placeholder="youtube")
if(st.button("Submit the Name",type="primary")):
    websiteNameLower=websiteName.lower()
    for extension in tld:
        url=f"https://www.{websiteNameLower}{extension}"
        try:
            response=requests.get(url,timeout=10)
            status_code=response.status_code
            if(status_code>=200 and status_code<=299):
                st.write("✅ Website found successfully..!")
                st.write(f"Predicted URL : {url}")
                break
            elif status_code==403:
                st.write("⚠️ Website found but access restricted:")
                st.write(url)
            elif status_code==429:
                st.write("⚠️ Too many requests. Please try again later.")
                break
            elif status_code==500:
                st.write("⚠️ Server problem while checking:")
                st.write(url)
            
            elif status_code==404:
                continue
        except requests.exceptions.RequestException:
            continue

