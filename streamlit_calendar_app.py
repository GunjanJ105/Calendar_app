import streamlit as st
import calendar
import json
import os
from datetime import datetime

EVENTS_FILE = "events.json"

# ---------------------------
# Load & Save Events
# ---------------------------
def load_events():
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_events(events):
    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=4)

events = load_events()

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Calendar App", layout="wide")
st.title("📆 Streamlit Calendar App")

# ---------------------------
# Show Calendar
# ---------------------------
st.subheader("🔢 Enter a year to view the calendar")
year = st.number_input("Year", min_value=1900, max_value=2100, value=datetime.now().year)

if st.button("Show Calendar"):
    cal_html = calendar.HTMLCalendar().formatyear(year)
    st.markdown(f"<div style='overflow-x:auto'>{cal_html}</div>", unsafe_allow_html=True)

# ---------------------------
# Add Event Section
# ---------------------------
st.subheader("📝 Add Event")

date = st.date_input("Select Date")
event_desc = st.text_input("Event Description")

if st.button("Add Event"):
    date_str = str(date)
    events[date_str] = event_desc
    save_events(events)
    st.success(f"Event added for {date_str}")

# ---------------------------
# View Events
# ---------------------------
st.subheader("📚 All Events")
if events:
    for d, e in events.items():
        st.write(f"📅 **{d}** → {e}")
else:
    st.info("No events found. Add some!")
