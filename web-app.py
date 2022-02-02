import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('LogRegressionModel.pkl', 'rb'))


def pred(mail):
    res = loaded_model.predict(mail)
    if res[0] == 1:
        return "Ham Mail"
    else:
        return "Spam Mail"


def main():
    # page title
    st.title('Spam-Ham Mail Prediction App')

    input_mail = st.text_input("Enter the mail to be checked : ")

    # prediction code
    result = ''

    # button for prediction
    if st.button('Check'):
        result = pred([input_mail])

    # printing the result
    if result == "Spam":
        st.error(result)
    else:
        st.success(result)


if __name__ == '__main__':
    main()
