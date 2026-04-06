import streamlit as st

st.title("Student To-Do App")

# Initialize the task list in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ── Add a task ──────────────────────────────────────────────
st.subheader("Add a Task")
task_name = st.text_input("Task name")

if st.button("Add Task"):
    if task_name.strip() == "":
        st.warning("Please enter a task name.")
    else:
        st.session_state.tasks.append({"task": task_name, "done": False})
        st.success(f"Task '{task_name}' added!")

# ── View / manage tasks ─────────────────────────────────────
st.subheader("Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")
else:
    for index, item in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6, 2, 2])

        # Task name + status
        status = "✅" if item["done"] else "⬜"
        col1.write(f"{status} {item['task']}")

        # Mark as done button
        if not item["done"]:
            if col2.button("Done", key=f"done_{index}"):
                st.session_state.tasks[index]["done"] = True
                st.rerun()
        else:
            col2.write("Completed")

        # Delete button
        if col3.button("Delete", key=f"delete_{index}"):
            removed = st.session_state.tasks.pop(index)
            st.success(f"Deleted '{removed['task']}'")
            st.rerun()