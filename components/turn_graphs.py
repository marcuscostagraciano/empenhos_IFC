import streamlit as st
from utils import *
from components.main_graph import main_graph
from components.tabs_child_graph import tabs_child_graph

def turn_graphs():
    main_graph()
    tabs_child_graph()