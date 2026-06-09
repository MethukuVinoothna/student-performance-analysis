import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd





df = pd.read_csv("students.csv")


df = df[df["Name"].notna()]
df = df[df["Name"] != "None"]

df.to_csv("students.csv", index=False)
st.title("Student Performance Analysis")
st.dataframe(df)
topper = df.loc[

    (df["Maths"] +

     df["Physics"] +

     df["Chemistry"]).idxmax()
]



st.success(f"Topper: {topper['Name']}")


fig, ax = plt.subplots()

ax.bar(
    df["Name"],
    df["Maths"],
    color="red"
)

ax.set_title("Maths Scores")

st.pyplot(fig)


st.subheader("Subject Average")

fig, ax = plt.subplots()

subjects = ["Maths", "Physics", "Chemistry"]

averages = [
    df["Maths"].mean(),
    df["Physics"].mean(),
    df["Chemistry"].mean()
]

ax.bar(
    subjects,
    averages,
    color="green"
)

ax.set_title("Subject Average")

st.pyplot(fig)

st.subheader("Heatmap")

fig, ax = plt.subplots(figsize=(6,4))

sns.heatmap(
    df[["Maths","Physics","Chemistry"]],
    annot=True,
    cmap="YlGnBu",
    ax=ax
)

st.pyplot(fig)



st.subheader("Add New Student")

name = st.text_input("Student Name")

maths = st.number_input("Maths", 0, 100)

physics = st.number_input("Physics", 0, 100)

chemistry = st.number_input("Chemistry", 0, 100)

if st.button("Add Student"):

    if name.strip() == "":
        st.error("Please enter student name")

    else:
        new_student = pd.DataFrame({
            "Name":[name],
            "Maths":[maths],
            "Physics":[physics],
            "Chemistry":[chemistry]
        })

        df = pd.concat([df,new_student],
                       ignore_index=True)

        df.to_csv("students.csv",
                  index=False)

        st.success("Saved Successfully!")

        st.rerun()		
st.subheader("Delete Student")

student_to_delete = st.selectbox(
    "Select Student",
    df["Name"]
)

if st.button("Delete Student"):
    df = df[df["Name"] != student_to_delete]

    df.to_csv("students.csv", index=False)

    st.success(f"{student_to_delete} deleted!")

    st.rerun()
