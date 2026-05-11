import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Smart Task AI Dashboard",
    layout="wide"
)

# =========================
# SESSION STORAGE
# =========================

if "pending_tasks" not in st.session_state:
    st.session_state.pending_tasks = []

if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []

if "notifications" not in st.session_state:
    st.session_state.notifications = True

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# =========================
# CUSTOM CSS
# =========================

st.markdown("""

<style>

.main {
    background-color: #0f172a;
    color: white;
}

.task-card {
    background: #1e293b;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
}

.metric-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
}

.big-font {
    font-size: 35px;
    font-weight: bold;
}

</style>

""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🚀 Smart Task AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Tasks",
        "Settings"
    ]
)

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    st.title("📊 Task Management Dashboard")

    total_tasks = (
        len(st.session_state.pending_tasks)
        +
        len(st.session_state.completed_tasks)
    )

    completed = len(st.session_state.completed_tasks)

    pending = len(st.session_state.pending_tasks)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Tasks</h3>
            <div class="big-font">{total_tasks}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Completed</h3>
            <div class="big-font">{completed}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Pending</h3>
            <div class="big-font">{pending}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 3D PIE CHART

    fig = go.Figure(data=[go.Pie(
        labels=["Completed", "Pending"],
        values=[completed, pending],
        hole=0.4
    )])

    fig.update_layout(
        title="🔥 Task Completion Analytics",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# ANALYTICS
# =========================

elif menu == "Analytics":

    st.title("📈 Advanced AI Analytics")

    completed = len(st.session_state.completed_tasks)
    pending = len(st.session_state.pending_tasks)

    # =========================
    # 3D BAR GRAPH
    # =========================

    fig_bar = go.Figure(data=[go.Bar(
        x=["Completed", "Pending"],
        y=[completed, pending],
        marker_color=[
            "green",
            "red"
        ]
    )])

    fig_bar.update_layout(
        title="🚀 3D Productivity Graph",
        height=500
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    # =========================
    # 3D LINE GRAPH
    # =========================

    timeline = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri"
    ]

    productivity = [2, 5, 4, 7, completed]

    fig_line = go.Figure(data=[go.Scatter3d(
        x=timeline,
        y=[1, 2, 3, 4, 5],
        z=productivity,
        mode='lines+markers',
        marker=dict(
            size=8,
            color=productivity,
            colorscale='Viridis'
        ),
        line=dict(
            width=5
        )
    )])

    fig_line.update_layout(
        title="🔥 Real-Time 3D Performance",
        height=700
    )

    st.plotly_chart(fig_line, use_container_width=True)

    # =========================
    # SURFACE GRAPH
    # =========================

    import numpy as np

    x = np.outer(
        np.linspace(-2, 2, 30),
        np.ones(30)
    )

    y = x.copy().T

    z = np.sin(x ** 2 + y ** 2)

    fig_surface = go.Figure(data=[
        go.Surface(
            z=z
        )
    ])

    fig_surface.update_layout(
        title="🌊 AI Surface Analytics",
        height=700
    )

    st.plotly_chart(fig_surface, use_container_width=True)

# =========================
# TASKS
# =========================

elif menu == "Tasks":

    st.title("✅ Smart Task Manager")

    task = st.text_input(
        "Enter New Task"
    )

    if st.button("➕ Add Task"):

        if task != "":

            st.session_state.pending_tasks.append(task)

            st.success("Task Added Successfully")

            if st.session_state.notifications:
                st.toast("🔥 New Task Added")

    st.markdown("---")

    st.subheader("⏳ Pending Tasks")

    for i, t in enumerate(
        st.session_state.pending_tasks
    ):

        col1, col2 = st.columns([4,1])

        with col1:
            st.markdown(f"""
            <div class="task-card">
            {t}
            </div>
            """, unsafe_allow_html=True)

        with col2:

            if st.button(
                f"✅ Complete {i}"
            ):

                completed_task = (
                    st.session_state.pending_tasks.pop(i)
                )

                st.session_state.completed_tasks.append(
                    completed_task
                )

                st.success("Task Completed")

                st.toast("🎉 Task Completed")

                st.rerun()

    st.markdown("---")

    st.subheader("🏆 Completed Tasks")

    for t in st.session_state.completed_tasks:

        st.markdown(f"""
        <div class="task-card"
             style="background:green;">
        {t}
        </div>
        """, unsafe_allow_html=True)

# =========================
# SETTINGS
# =========================

elif menu == "Settings":

    st.title("⚙️ Settings")

    st.subheader("🌙 Theme")

    dark = st.toggle(
        "Enable Dark Mode",
        value=True
    )

    st.session_state.dark_mode = dark

    st.subheader("🔔 Notifications")

    notify = st.toggle(
        "Enable Notifications",
        value=True
    )

    st.session_state.notifications = notify

    st.subheader("👤 User Profile")

    st.text_input(
        "User Name",
        "Aman Yadav"
    )

    st.text_input(
        "Role",
        "Python Developer"
    )

    st.success(
        "Settings Saved Successfully"
    )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "🚀 Smart Task AI Dashboard | Internship Level Project"
)