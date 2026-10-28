import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="TLB Performance Analyzer",
    page_icon="💻",
    layout="wide"
)

st.title("TLB Performance Analysis and Address Translation Simulator")
st.write("Group-8 | Computer Organization and Architecture")

st.sidebar.header("Simulator Settings")

capacity = st.sidebar.selectbox(
    "TLB Capacity",
    [2, 4, 8, 16],
    index=1
)

policy = st.sidebar.selectbox(
    "Replacement Policy",
    ["FIFO", "LRU"]
)

st.subheader("Virtual Address Translation")

address = st.number_input(
    "Enter Virtual Address (0–4095)",
    min_value=0,
    max_value=4095,
    value=100,
    step=1
)

page_size = 256

page_table = {
    0: 5, 1: 2, 2: 8, 3: 1,
    4: 6, 5: 3, 6: 9, 7: 4,
    8: 7, 9: 0, 10: 10, 11: 11,
    12: 12, 13: 13, 14: 14, 15: 15
}

page_number = address // page_size
offset = address % page_size
frame_number = page_table[page_number]
physical_address = frame_number * page_size + offset

col1, col2, col3 = st.columns(3)

col1.metric("Page Number", page_number)
col2.metric("Offset", offset)
col3.metric("Frame Number", frame_number)

st.success(f"Physical Address: {physical_address}")

st.info(
    f"Selected TLB Capacity: {capacity} | "
    f"Replacement Policy: {policy}"
)

st.subheader("Sample Performance Comparison")

capacities = [2, 4, 8, 16]
fifo_hits = [40, 55, 70, 85]
lru_hits = [50, 65, 80, 90]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(capacities, fifo_hits, marker="o", label="FIFO")
ax.plot(capacities, lru_hits, marker="s", label="LRU")
ax.set_xlabel("TLB Capacity")
ax.set_ylabel("Hit Ratio (%)")
ax.set_title("TLB Capacity vs Hit Ratio")
ax.set_ylim(0, 100)
ax.grid(True)
ax.legend()

st.pyplot(fig)

st.caption(
    "Note: Chart values are illustrative samples, not measured results. "
    "Address translation uses the project's page table."
)