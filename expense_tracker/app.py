import streamlit as st

from expense_tracker.backend.service import create_and_store_transaction, get_user_transactions
from expense_tracker.database.repository import authenticate_user, register_user
from expense_tracker.frontend.theme import inject_modern_theme
from expense_tracker.frontend.ui import render_charts, render_logo_and_header, t

st.set_page_config(page_title="KA Expense System", layout="wide")
st.markdown(inject_modern_theme(), unsafe_allow_html=True)
for k,v in {"lang":"vi","user":None,"api_key":""}.items():
    if k not in st.session_state: st.session_state[k]=v

c1,c2=st.columns([1,6])
with c1:
    if st.button(t("toggle")): st.session_state.lang="en" if st.session_state.lang=="vi" else "vi"; st.rerun()
with c2: render_logo_and_header()

with st.sidebar:
    st.text_input(t("api_key"), type="password", key="api_key", help=t("api_help"))
    if st.session_state.user and st.button(t("logout")): st.session_state.user=None; st.rerun()
    if st.button(t("reset")):
        lang=st.session_state.lang; st.session_state.clear(); st.session_state.lang=lang; st.session_state.user=None; st.session_state.api_key=""; st.rerun()

if not st.session_state.user:
    st.subheader(t("auth")); a,b=st.columns(2)
    with a:
        u=st.text_input(t("username"), key="lu"); p=st.text_input(t("password"), type="password", key="lp")
        if st.button(t("login")):
            user=authenticate_user(u,p)
            if user: st.session_state.user=user; st.success(t("ok_login")); st.rerun()
            else: st.error(t("bad_login"))
    with b:
        u2=st.text_input(t("username"), key="ru"); p2=st.text_input(t("password"), type="password", key="rp")
        if st.button(t("register")): st.success(t("ok_reg")) if register_user(u2,p2) else st.error(t("bad_reg"))
else:
    text=st.text_input(t("input"))
    if st.button(t("save")) and text:
        try: st.success(create_and_store_transaction(st.session_state.user[0], text, api_key=st.session_state.api_key or None))
        except Exception as exc: st.error(str(exc))
    st.subheader(t("history")); render_charts(get_user_transactions(st.session_state.user[0]))
