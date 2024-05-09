import streamlit as st
from utils import *
from components.main_table import main_table
from components.tabs_child_table import tabs_child_table

def turn_dataframes():
    main_table()
    tabs_child_table()