import streamlit as st
import requests

# Replace with your actual API Gateway URL
API_BASE = "https://00kudus378.execute-api.us-east-2.amazonaws.com"

st.title("📝 Serverless To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add Task Form
with st.form("Add Task"):
    title = st.text_input("Title")
    description = st.text_area("Description")
    submitted = st.form_submit_button("Add Task")
    if submitted:
        response = requests.post(f"{API_BASE}/tasks", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("✅ Task added!")
        else:
            st.error("❌ Failed to add task. Check API or Lambda logs.")

# Refresh Task List
if st.button("🔄 Refresh Task List"):
    res = requests.get(f"{API_BASE}/tasks")
    if res.status_code == 200:
        st.session_state.tasks = res.json()
    else:
        st.error("❌ Failed to fetch tasks.")

# Show Task List
for task in st.session_state.tasks:
    st.markdown(f"**📌 {task['title']}** — {task['description']} (Status: `{task['status']}`)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mark as Completed", key=f"done-{task['task_id']}"):
            requests.put(f"{API_BASE}/tasks/{task['task_id']}", json={"status": "completed"})
            st.experimental_rerun()
    with col2:
        if st.button("🗑️ Delete", key=f"del-{task['task_id']}"):
            requests.delete(f"{API_BASE}/tasks/{task['task_id']}")
            st.experimental_rerun()
