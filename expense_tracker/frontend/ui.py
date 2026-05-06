import pandas as pd
import plotly.express as px
import streamlit as st

TEXTS={"vi":{"toggle":"🌐 English","title":"KA Smart Expense System","auth":"Đăng nhập / Đăng ký","username":"Tên đăng nhập","password":"Mật khẩu","login":"Đăng nhập","register":"Đăng ký","logout":"Đăng xuất","reset":"Reset hệ thống (giữ data)","input":"Nhập giao dịch","save":"Phân tích & lưu","history":"Lịch sử giao dịch","empty":"Chưa có dữ liệu","ok_login":"Đăng nhập thành công","bad_login":"Sai tài khoản/mật khẩu","ok_reg":"Đăng ký thành công (mật khẩu >= 6 ký tự)","bad_reg":"Đăng ký thất bại","monthly":"Thu nhập vs Chi tiêu theo tháng","category":"Phân bổ danh mục","api_key":"OpenAI API Key","api_help":"Chỉ dùng trong phiên hiện tại"},"en":{"toggle":"🌐 Tiếng Việt","title":"KA Smart Expense System","auth":"Login / Register","username":"Username","password":"Password","login":"Login","register":"Register","logout":"Logout","reset":"Reset system (keep data)","input":"Enter transaction","save":"Analyze & Save","history":"Transaction History","empty":"No data","ok_login":"Login successful","bad_login":"Invalid credentials","ok_reg":"Registration successful (password >= 6 chars)","bad_reg":"Registration failed","monthly":"Monthly Income vs Expense","category":"Category split","api_key":"OpenAI API Key","api_help":"Used in current session only"}}

def t(key): return TEXTS[st.session_state.get("lang","vi")][key]

def render_logo_and_header(): st.markdown('<div class="ka-logo">KA</div>', unsafe_allow_html=True); st.title(t("title"))

def render_charts(df):
    if df.empty: st.info(t("empty")); return
    st.dataframe(df,use_container_width=True); df["date"]=pd.to_datetime(df["date"])
    monthly=df.groupby([pd.Grouper(key="date",freq="M"),"type"],as_index=False)["amount"].sum()
    st.plotly_chart(px.bar(monthly,x="date",y="amount",color="type",barmode="group",title=t("monthly")),use_container_width=True)
    cat=df[df["type"]=="expense"].groupby("category",as_index=False)["amount"].sum()
    if not cat.empty: st.plotly_chart(px.pie(cat,names="category",values="amount",title=t("category")),use_container_width=True)
