import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💼 Personal Finance Dashboard")

# Input income
income = st.number_input("Enter your monthly income", min_value=0.0)

# Input number of expenses
n = st.number_input("Number of expense categories", min_value=1, step=1)

categories = []
amounts = []

for i in range(int(n)):
    cat = st.text_input(f"Category {i+1}", key=i)
    amt = st.number_input(f"Amount for {cat if cat else 'Category'}", key=i+100)
    
    categories.append(cat)
    amounts.append(amt)

# Button
if st.button("Analyze"):
    df = pd.DataFrame({
        "Category": categories,
        "Amount": amounts
    })

    total = df["Amount"].sum()
    savings = income - total

    st.subheader("📊 Summary")
    st.write(df)

    st.write("💰 Total Expense:", total)
    st.write("💵 Savings:", savings)

    if savings < 0:
        st.error("You are overspending!")
    elif savings < income * 0.3:
        st.warning("Try to save more money.")
    else:
        st.success("Good financial management!")

    # Graph
    fig, ax = plt.subplots()
    ax.pie(df["Amount"], labels=df["Category"], autopct="%1.1f%%")
    ax.set_title("Expense Distribution")

    st.pyplot(fig)