import streamlit as st
from GPTanalysis import GPTanalysis
from reviewCollector import reviewCollector



def init_state():
    st.session_state.logged_in = False
    st.session_state.ASINkey = ""
    st.session_state.GPTAPIkey = ""



def login_page():


    ASINkey = st.text_input("ASINkey")
    GPTAPIkey = st.text_input("GPTAPIkey")


    if st.button("Submit Keys"):
        if authenticateKeys(ASINkey, GPTAPIkey):
            st.session_state.logged_in = True
            st.session_state.ASINkey = ASINkey
            st.session_state.GPTAPIkey = GPTAPIkey
            st.success("Keys Successful. Press Submit Again to Confirm Usage")

        else:
            st.error("Invalid username or password!")


def authenticateKeys(ASINkey, GPTAPIkey):

    validGPT = False
    validASIN = False
        
    testGPT = GPTanalysis(GPTAPIkey)
    if testGPT.testKey():
        validGPT = True
        st.session_state.GPTanalysis = testGPT

    testASIN = reviewCollector(ASINkey)
    if testASIN.testKey():
        validASIN = True
        st.session_state.reviewCollector = testASIN

    return validGPT and validASIN

   



def main():

    if not st.session_state:
        init_state()

    if not st.session_state.logged_in:
        login_page()

    else:
        product = st.text_input("Enter Product")

        if st.button("Research Reviews"):
            st.write("Collecting Reviews (1-3 Minutes)...")
                    
            df = st.session_state.reviewCollector.getReviews(product)
            st.write("Making Summary (~30 Seconds)...")
            insight = st.session_state.GPTanalysis.GPTinsight(df)

            st.write(insight)
            st.dataframe(df)



if __name__ == "__main__":
    main()







   


               




