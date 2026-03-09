# dashboard_proud_living_complete_fixed.py
# รันด้วย: streamlit run dashboard_proud_living_complete_fixed.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proud Living Dashboard", layout="wide", page_icon="🏠")

# CSS เพื่อความสวยงาม
st.markdown("""
    <style>
        .stMetric {
            background-color: #1e1e1e;
            padding: 16px;
            border-radius: 12px;
            text-align: center;
            margin: 8px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        h1 { color: #ffffff !important; margin-bottom: 0.5rem; }
        h3 { color: #e0e0e0 !important; margin: 1.8rem 0 0.8rem 0; font-size: 1.5rem; }
        hr { margin: 2.2rem 0; border-color: #444; }
        .empty-notice {
            color: #aaaaaa;
            font-style: italic;
            padding: 1.2rem;
            background: #1a1a1a;
            border-radius: 10px;
            margin: 1.5rem 0;
            border-left: 4px solid #555;
        }
        .rank-table th {
            background-color: #2a2a2a;
            color: #ffffff;
            padding: 8px 12px;
        }
        .rank-table td {
            padding: 8px 12px;
        }
        .kpi-section {
            background-color: #1a1a2e;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ─── HEADER ────────────────────────────────────────────────────────────────
st.title("🏠 Proud Living Community Dashboard")
st.caption("ข้อมูลสรุปล่าสุด ณ 31 ตุลาคม 2568 (V2) • ICRHH • VEHHA • Ari")
st.markdown("---")

# ─── SIDEBAR ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("ตัวกรองโครงการ")
    selected_project = st.selectbox(
        "เลือกโครงการ",
        options=["ทั้งหมด", "ICRHH", "VEHHA", "Ari"],
        index=0
    )
    st.markdown("---")

# ─── DATASETS ทั้งหมด ─────────────────────────────────────────────────────
months = ["Jul", "Aug", "Sep", "Oct"]

df_users = pd.DataFrame({
    "โครงการ": ["ICRHH", "VEHHA", "Ari"],
    "All Users": [307, 229, 2],
    "Units": [261, 366, 2],
    "Owner": [212, 135, 2],
    "co-Owner": [50, 40, 0],
    "Residents": [55, 49, 0],
    "Tenant": [10, 5, 0]
})

df_news_ic = pd.DataFrame({"เดือน": months, "News Posted": [5,5,2,6], "Viewed": [455,424,66,210]})
df_news_vh = pd.DataFrame({"เดือน": months, "News Posted": [4,10,4,5], "Viewed": [128,388,151,195]})

# ─── Top 5 News ────────────────────────────────────────────────────────────
df_top_news_ic = pd.DataFrame({
    "อันดับ": [1, 2, 3, 4, 5],
    "หัวข้อข่าว": [
        "ประกาศแผนการซ่อมบำรุงประจำเดือนกรกฎาคม",
        "กิจกรรม Community Day สิงหาคม 2568",
        "แจ้งเตือนงานทาสีอาคารชั้น B1–B3",
        "ประกาศปรับเวลาให้บริการ Fitness",
        "สรุปผลการประเมินความพึงพอใจ Q2"
    ],
    "ยอดเข้าชม": [210, 185, 163, 142, 98]
})

df_top_news_vh = pd.DataFrame({
    "อันดับ": [1, 2, 3, 4, 5],
    "หัวข้อข่าว": [
        "กิจกรรม Pool Party เดือนสิงหาคม",
        "ประกาศการปรับปรุงสวนส่วนกลาง",
        "แจ้งกำหนดการฉีดพ่นยากันแมลง",
        "อัปเดตนโยบายการจอดรถสำหรับผู้เยี่ยมชม",
        "ประชาสัมพันธ์บริการนวดแผนไทย"
    ],
    "ยอดเข้าชม": [175, 142, 121, 108, 89]
})

# ─── Repair Request (อัปเดตตามรูปที่แนบ) ─────────────────────────────────
df_repair_ic = pd.DataFrame({
    "เดือน": months,
    "Repair Request": [16, 53, 15, 35],
    "รอดำเนินการ": [0, 0, 0, 4],
    "กำลังดำเนินการ": [0, 0, 0, 0],
    "นัดหมาย": [0, 0, 0, 2],
    "เสร็จสิ้น": [0, 0, 0, 3],
    "ปิดงาน": [16, 53, 15, 26]
})

df_repair_vh = pd.DataFrame({
    "เดือน": months,
    "Repair Request": [207, 231, 242, 283],
    "รอดำเนินการ": [3, 2, 51, 95],
    "กำลังดำเนินการ": [0, 0, 3, 9],
    "นัดหมาย": [0, 0, 0, 0],
    "เสร็จสิ้น": [109, 91, 47, 45],
    "ปิดงาน": [95, 138, 141, 133]
})

# ─── Top 5 Repair ──────────────────────────────────────────────────────────
df_top_repair_ic = pd.DataFrame({
    "อันดับ": [1, 2, 3, 4, 5],
    "ประเภทงานซ่อม": [
        "ระบบไฟฟ้าและแสงสว่าง",
        "ระบบประปาและสุขาภิบาล",
        "งานซ่อมแซมประตู/หน้าต่าง",
        "ระบบปรับอากาศ",
        "งานทั่วไปในห้องพัก"
    ],
    "จำนวนครั้ง": [42, 35, 21, 15, 6]
})

df_top_repair_vh = pd.DataFrame({
    "อันดับ": [1, 2, 3, 4, 5],
    "ประเภทงานซ่อม": [
        "ระบบประปาและสุขาภิบาล",
        "ระบบไฟฟ้าและแสงสว่าง",
        "ระบบปรับอากาศ",
        "งานซ่อมแซมประตู/หน้าต่าง",
        "พื้นและฝ้าเพดาน"
    ],
    "จำนวนครั้ง": [385, 298, 187, 62, 31]
})

df_sat_ic = pd.DataFrame({"ด้าน": ["ความสะอาด","การแก้ไข","ความรวดเร็ว"], "5": [35,35,32], "4": [1,1,3], "3": [0,0,1], "2": [0,0,0], "1": [0,0,0]})
df_sat_vh = pd.DataFrame({"ด้าน": ["ความสะอาด","การแก้ไข","ความรวดเร็ว"], "5": [471,473,473], "4": [8,9,9], "3": [1,3,1], "2": [2,2,1], "1": [17,15,18]})

df_pay_ic = pd.DataFrame({
    "เดือน": months,
    "Pending": [0, 1, 4, 76],
    "Complete": [243, 11, 165, 34],
    "QR": [184, 3, 101, 22],
    "Cash": [132, 7, 46, 10],
    "Credit": [22, 1, 18, 2],
    "Amount": [491177, 40562, 38639, 24384]
})

df_pay_vh = pd.DataFrame({
    "เดือน": months,
    "Pending": [0, 4, 31, 60],
    "Complete": [0, 87, 0, 0],
    "QR": [0, 0, 0, 0],
    "Cash": [0, 87, 0, 8],
    "Credit": [0, 87, 0, 0],
    "Amount": [0, 134494, 37100, 33840]
})

pay_ic_total = df_pay_ic.sum(numeric_only=True)
pay_vh_total = df_pay_vh.sum(numeric_only=True)
payment_categories = ["Pending", "Complete", "QR", "Cash", "Credit"]

df_parcel_ic = pd.DataFrame({
    "เดือน": months,
    "ทั้งหมด": [35,23,25,40],
    "รับแล้ว": [35,22,25,29],
    "คงค้าง": [0,1,0,10]
})

df_parcel_vh = pd.DataFrame({
    "เดือน": months,
    "ทั้งหมด": [55,91,47,27],
    "รับแล้ว": [16,39,47,21],
    "คงค้าง": [39,52,0,6]
})

df_service_ic = pd.DataFrame({
    "เดือน": months,
    "บริการแม่บ้าน": [202, 223, 192, 212],
    "บริการซักรีด": [110, 121, 85, 89],
    "บริการสปาเด็ก": [0, 0, 0, 0],
    "บริการอาหารและเครื่องดื่ม": [4, 1, 0, 0],
    "บริการดูแลเด็ก": [0, 0, 0, 0],
    "Fitness Personal Trainer": [4, 4, 2, 1],
    "บริการนวด": [0, 0, 0, 0],
    "บริการช่วยเหลือผู้สูงอายุ": [0, 0, 0, 2]
})

df_service_vh = pd.DataFrame({
    "เดือน": months,
    "บริการล้างแอร์": [0, 0, 0, 0],
    "บริการอาหารและเครื่องดื่ม": [0, 0, 0, 0],
    "บริการสปาเด็ก": [0, 0, 0, 0],
    "บริการดูแลผู้สูงอายุ": [0, 0, 0, 0],
    "บริการนวด": [6, 0, 39, 9],
    "บริการทำความสะอาด": [13, 1, 2, 2],
    "บริการส่งเสริมสุขภาพและออกกำลังกาย": [0, 1, 4, 6],
    "บริการอาบแดด": [0, 4, 6, 13]
})

service_ic_total = df_service_ic.drop(columns="เดือน").sum().reset_index()
service_ic_total.columns = ["บริการ", "จำนวนครั้งรวม"]
service_ic_total = service_ic_total[service_ic_total["จำนวนครั้งรวม"] > 0].sort_values("จำนวนครั้งรวม", ascending=False).head(5).reset_index(drop=True)
service_ic_total.index = service_ic_total.index + 1
service_ic_total.index.name = "อันดับ"

service_vh_total = df_service_vh.drop(columns="เดือน").sum().reset_index()
service_vh_total.columns = ["บริการ", "จำนวนครั้งรวม"]
service_vh_total = service_vh_total[service_vh_total["จำนวนครั้งรวม"] > 0].sort_values("จำนวนครั้งรวม", ascending=False).head(5).reset_index(drop=True)
service_vh_total.index = service_vh_total.index + 1
service_vh_total.index.name = "อันดับ"

df_fac_ic = pd.DataFrame({"เดือน": months, "จำนวนการจอง": [9,7,5,27]})
df_fac_vh = pd.DataFrame({"เดือน": months, "จำนวนการจอง": [0,0,5,14]})

# ฟังก์ชันตรวจสอบข้อมูล
def has_data(df, col=None):
    if col:
        return df[col].sum() > 0 if col in df.columns else False
    return df.iloc[:, 1:].sum().sum() > 0 if len(df.columns) > 1 else False

# ─── ผู้ใช้งาน ─────────────────────────────────────────────────────────────
st.subheader("👥 สรุปผู้ใช้งาน")

if selected_project == "ทั้งหมด":
    total_users = 566
    inactive_users = 83
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("จำนวนผู้ใช้งานทั้งหมด", f"{total_users:,} คน")
    with c2:
        st.metric("ไม่ได้ Login ภายใน 3 เดือน", f"{inactive_users:,} คน")
    with c3:
        st.metric("จำนวนโครงการ", "3")

    st.markdown("##### รายละเอียดแยกตามโครงการ")
    col_ic, col_vh = st.columns(2)
    user_fields = ["All Users", "Units", "Owner", "co-Owner", "Residents", "Tenant"]

    with col_ic:
        st.markdown("**ICRHH**")
        row_ic = df_users[df_users["โครงการ"] == "ICRHH"].iloc[0]
        st.dataframe(
            pd.DataFrame({"รายการ": user_fields, "จำนวน": [row_ic[f] for f in user_fields]}).set_index("รายการ"),
            use_container_width=True
        )

    with col_vh:
        st.markdown("**VEHHA**")
        row_vh = df_users[df_users["โครงการ"] == "VEHHA"].iloc[0]
        st.dataframe(
            pd.DataFrame({"รายการ": user_fields, "จำนวน": [row_vh[f] for f in user_fields]}).set_index("รายการ"),
            use_container_width=True
        )

elif selected_project == "Ari":
    st.markdown('<div class="empty-notice">โครงการ Ari มีผู้ใช้งานเพียง 2 ราย (Owner) ณ ขณะนี้</div>', unsafe_allow_html=True)
    df_ari = df_users[df_users["โครงการ"] == "Ari"][["โครงการ","All Users","Units","Owner","co-Owner","Residents","Tenant"]].set_index("โครงการ")
    st.dataframe(df_ari, use_container_width=True)

else:
    row = df_users[df_users["โครงการ"] == selected_project].iloc[0]
    user_fields = ["All Users", "Units", "Owner", "co-Owner", "Residents", "Tenant"]
    st.dataframe(
        pd.DataFrame({"รายการ": user_fields, "จำนวน": [row[f] for f in user_fields]}).set_index("รายการ"),
        use_container_width=True
    )

st.markdown("---")

# ─── News ───────────────────────────────────────────────────────────────────
if has_data(df_news_ic, "Viewed") or has_data(df_news_vh, "Viewed"):
    st.subheader("📰 ข่าวสารและยอดเข้าชม")
    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)
    col1 = cols[0]
    col2 = cols[1] if selected_project == "ทั้งหมด" else None

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_news_ic, "Viewed"):
        with col1:
            fig = px.bar(df_news_ic.melt(id_vars="เดือน", var_name="ประเภท", value_name="จำนวน"),
                         x="เดือน", y="จำนวน", color="ประเภท", barmode="group", title="ICRHH")
            st.plotly_chart(fig, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_news_vh, "Viewed"):
        target = col2 if selected_project == "ทั้งหมด" else col1
        with target:
            fig = px.bar(df_news_vh.melt(id_vars="เดือน", var_name="ประเภท", value_name="จำนวน"),
                         x="เดือน", y="จำนวน", color="ประเภท", barmode="group", title="VEHHA")
            st.plotly_chart(fig, use_container_width=True)

    # ─── 5 อันดับข่าวสาร (ตาราง) ──────────────────────────────────────────
    st.markdown("#### 🏆 5 อันดับข่าวสารยอดนิยม (สะสม Jul–Oct)")
    cols_rank = st.columns(2 if selected_project == "ทั้งหมด" else 1)

    if selected_project in ["ทั้งหมด", "ICRHH"]:
        with cols_rank[0]:
            st.markdown("**ICRHH**")
            st.dataframe(
                df_top_news_ic.set_index("อันดับ"),
                use_container_width=True
            )

    if selected_project in ["ทั้งหมด", "VEHHA"]:
        target = cols_rank[1] if selected_project == "ทั้งหมด" else cols_rank[0]
        with target:
            st.markdown("**VEHHA**")
            st.dataframe(
                df_top_news_vh.set_index("อันดับ"),
                use_container_width=True
            )

    st.markdown("---")

# ─── Home Care ──────────────────────────────────────────────────────────────
repair_status_cols = ["รอดำเนินการ", "กำลังดำเนินการ", "นัดหมาย", "เสร็จสิ้น", "ปิดงาน"]

if has_data(df_repair_ic, "Repair Request") or has_data(df_repair_vh, "Repair Request"):
    st.subheader("🔧 การแจ้งซ่อม / Home Care")

    repair_color_map = {
        "Repair Request":    "#a0c4ff",  # ฟ้าอ่อน
        "รอดำเนินการ":       "#74b9ff",  # ฟ้า
        "กำลังดำเนินการ":   "#0984e3",  # น้ำเงิน
        "นัดหมาย":           "#fd79a8",  # ชมพู
        "เสร็จสิ้น":         "#e17055",  # ส้ม-แดง
        "ปิดงาน":            "#00b894",  # เขียว
    }
    all_repair_cols = ["Repair Request"] + repair_status_cols

    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_repair_ic, "Repair Request"):
        with cols[0]:
            df_melt_ic = df_repair_ic[["เดือน"] + all_repair_cols].melt(
                id_vars="เดือน", var_name="สถานะ", value_name="จำนวน"
            )
            # กำหนดลำดับ category
            df_melt_ic["สถานะ"] = pd.Categorical(df_melt_ic["สถานะ"], categories=all_repair_cols, ordered=True)
            df_melt_ic = df_melt_ic.sort_values("สถานะ")
            fig = px.bar(
                df_melt_ic, x="เดือน", y="จำนวน", color="สถานะ",
                barmode="group",
                title="ICRHH - สถานะการแจ้งซ่อมรายเดือน",
                color_discrete_map=repair_color_map,
                category_orders={"สถานะ": all_repair_cols}
            )
            fig.update_layout(
                legend_title_text="สถานะ",
                xaxis_title="เดือน",
                yaxis_title="จำนวน",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("**ตารางสรุปรายเดือน ICRHH**")
            st.dataframe(df_repair_ic.set_index("เดือน"), use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_repair_vh, "Repair Request"):
        target = cols[1] if selected_project == "ทั้งหมด" else cols[0]
        with target:
            df_melt_vh = df_repair_vh[["เดือน"] + all_repair_cols].melt(
                id_vars="เดือน", var_name="สถานะ", value_name="จำนวน"
            )
            df_melt_vh["สถานะ"] = pd.Categorical(df_melt_vh["สถานะ"], categories=all_repair_cols, ordered=True)
            df_melt_vh = df_melt_vh.sort_values("สถานะ")
            fig = px.bar(
                df_melt_vh, x="เดือน", y="จำนวน", color="สถานะ",
                barmode="group",
                title="VEHHA - สถานะการแจ้งซ่อมรายเดือน",
                color_discrete_map=repair_color_map,
                category_orders={"สถานะ": all_repair_cols}
            )
            fig.update_layout(
                legend_title_text="สถานะ",
                xaxis_title="เดือน",
                yaxis_title="จำนวน",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("**ตารางสรุปรายเดือน VEHHA**")
            st.dataframe(df_repair_vh.set_index("เดือน"), use_container_width=True)

    # ─── 5 อันดับประเภทงานแจ้งซ่อม (ตาราง) ───────────────────────────────
    st.markdown("#### 🏆 5 อันดับประเภทงานแจ้งซ่อมสูงสุด (สะสม Jul–Oct)")
    cols_rank = st.columns(2 if selected_project == "ทั้งหมด" else 1)

    if selected_project in ["ทั้งหมด", "ICRHH"]:
        with cols_rank[0]:
            st.markdown("**ICRHH**")
            st.dataframe(
                df_top_repair_ic.set_index("อันดับ"),
                use_container_width=True
            )

    if selected_project in ["ทั้งหมด", "VEHHA"]:
        target = cols_rank[1] if selected_project == "ทั้งหมด" else cols_rank[0]
        with target:
            st.markdown("**VEHHA**")
            st.dataframe(
                df_top_repair_vh.set_index("อันดับ"),
                use_container_width=True
            )

    st.markdown("---")

# ─── ความพึงพอใจ ────────────────────────────────────────────────────────────
if has_data(df_sat_ic) or has_data(df_sat_vh):
    st.subheader("😊 การประเมินความพึงพอใจ (5 เต็ม)")
    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)
    col1 = cols[0]
    col2 = cols[1] if selected_project == "ทั้งหมด" else None

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_sat_ic):
        with col1:
            fig = px.bar(df_sat_ic.melt(id_vars="ด้าน", var_name="คะแนน", value_name="จำนวน"),
                         x="ด้าน", y="จำนวน", color="คะแนน", barmode="group", title="ICRHH")
            st.plotly_chart(fig, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_sat_vh):
        with (col2 if selected_project == "ทั้งหมด" else col1):
            fig = px.bar(df_sat_vh.melt(id_vars="ด้าน", var_name="คะแนน", value_name="จำนวน"),
                         x="ด้าน", y="จำนวน", color="คะแนน", barmode="group", title="VEHHA")
            st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

# ─── Payment ────────────────────────────────────────────────────────────────
if pay_ic_total[payment_categories].sum() > 0 or pay_vh_total[payment_categories].sum() > 0:
    st.subheader("💰 สรุปการชำระเงิน (รวม Jul–Oct)")
    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)

    if selected_project in ["ทั้งหมด", "ICRHH"] and pay_ic_total[payment_categories].sum() > 0:
        with cols[0]:
            df_count = pd.DataFrame({"channel": payment_categories, "count": [pay_ic_total.get(cat, 0) for cat in payment_categories]})
            df_count = df_count[df_count["count"] > 0]
            fig = px.pie(df_count, values="count", names="channel", title="ICRHH - สัดส่วนจำนวนครั้ง", hole=0.4)
            fig.update_traces(textposition='inside', textinfo='percent+label+value')
            st.plotly_chart(fig, use_container_width=True)

            df_amount = pd.DataFrame({"channel": payment_categories, "amount": [pay_ic_total.get(cat, 0) for cat in payment_categories]})
            df_amount = df_amount[df_amount["amount"] > 0]
            fig = px.pie(df_amount, values="amount", names="channel", title="ICRHH - สัดส่วนยอดเงิน", hole=0.4)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and pay_vh_total[payment_categories].sum() > 0:
        target = cols[1] if selected_project == "ทั้งหมด" else cols[0]
        with target:
            df_count = pd.DataFrame({"channel": payment_categories, "count": [pay_vh_total.get(cat, 0) for cat in payment_categories]})
            df_count = df_count[df_count["count"] > 0]
            fig = px.pie(df_count, values="count", names="channel", title="VEHHA - สัดส่วนจำนวนครั้ง", hole=0.4)
            fig.update_traces(textposition='inside', textinfo='percent+label+value')
            st.plotly_chart(fig, use_container_width=True)

            df_amount = pd.DataFrame({"channel": payment_categories, "amount": [pay_vh_total.get(cat, 0) for cat in payment_categories]})
            df_amount = df_amount[df_amount["amount"] > 0]
            fig = px.pie(df_amount, values="amount", names="channel", title="VEHHA - สัดส่วนยอดเงิน", hole=0.4)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

# ─── Parcel ─────────────────────────────────────────────────────────────────
if has_data(df_parcel_ic, "ทั้งหมด") or has_data(df_parcel_vh, "ทั้งหมด"):
    st.subheader("📦 Parcel Summary")
    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)
    col1 = cols[0]
    col2 = cols[1] if selected_project == "ทั้งหมด" else None

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_parcel_ic, "ทั้งหมด"):
        with col1:
            fig = px.bar(df_parcel_ic.melt(id_vars="เดือน", var_name="สถานะ", value_name="จำนวน"),
                         x="เดือน", y="จำนวน", color="สถานะ", barmode="group",
                         title="ICRHH", text_auto=True)
            st.plotly_chart(fig, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_parcel_vh, "ทั้งหมด"):
        target = col2 if selected_project == "ทั้งหมด" else col1
        with target:
            fig = px.bar(df_parcel_vh.melt(id_vars="เดือน", var_name="สถานะ", value_name="จำนวน"),
                         x="เดือน", y="จำนวน", color="สถานะ", barmode="group",
                         title="VEHHA", text_auto=True)
            st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

# ─── Home Service ────────────────────────────────────────────────────────────
if has_data(df_service_ic) or has_data(df_service_vh):
    st.subheader("🧹 บริการ Home Service")

    cols = st.columns(2 if selected_project == "ทั้งหมด" else 1)
    col1 = cols[0]
    col2 = cols[1] if selected_project == "ทั้งหมด" else None

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_service_ic):
        with col1:
            melted_ic = df_service_ic.melt(id_vars="เดือน", var_name="บริการ", value_name="จำนวน")
            fig_ic = px.bar(melted_ic, x="เดือน", y="จำนวน", color="บริการ", barmode="group",
                            title="ICRHH - บริการ Home Service รายเดือน")
            fig_ic.update_layout(xaxis_title="เดือน", yaxis_title="จำนวนครั้ง")
            st.plotly_chart(fig_ic, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_service_vh):
        with (col2 if selected_project == "ทั้งหมด" else col1):
            melted_vh = df_service_vh.melt(id_vars="เดือน", var_name="บริการ", value_name="จำนวน")
            fig_vh = px.bar(melted_vh, x="เดือน", y="จำนวน", color="บริการ", barmode="group",
                            title="VEHHA - บริการ Home Service รายเดือน")
            fig_vh.update_layout(xaxis_title="เดือน", yaxis_title="จำนวนครั้ง")
            st.plotly_chart(fig_vh, use_container_width=True)

    # ─── 5 อันดับ Home Service (ตาราง) ──────────────────────────────────
    st.markdown("#### 🏆 5 อันดับบริการ Home Service ยอดนิยม (สะสม Jul–Oct)")
    cols_rank = st.columns(2 if selected_project == "ทั้งหมด" else 1)

    if selected_project in ["ทั้งหมด", "ICRHH"] and not service_ic_total.empty:
        with cols_rank[0]:
            st.markdown("**ICRHH**")
            st.dataframe(service_ic_total.reset_index(), use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and not service_vh_total.empty:
        target = cols_rank[1] if selected_project == "ทั้งหมด" else cols_rank[0]
        with target:
            st.markdown("**VEHHA**")
            st.dataframe(service_vh_total.reset_index(), use_container_width=True)

    st.markdown("---")

# ─── Facility Booking ───────────────────────────────────────────────────────
if has_data(df_fac_ic) or has_data(df_fac_vh):
    st.subheader("🏊 การจองสิ่งอำนวยความสะดวก")

    if selected_project in ["ทั้งหมด", "ICRHH"] and has_data(df_fac_ic):
        fig = px.pie(df_fac_ic, values="จำนวนการจอง", names="เดือน",
                     title="ICRHH - สัดส่วนการจองแต่ละเดือน", hole=0.3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    if selected_project in ["ทั้งหมด", "VEHHA"] and has_data(df_fac_vh):
        fig = px.pie(df_fac_vh, values="จำนวนการจอง", names="เดือน",
                     title="VEHHA - สัดส่วนการจองแต่ละเดือน", hole=0.3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

# ─── FOOTER ─────────────────────────────────────────────────────────────────
st.caption("Dashboard • Proud Living Summary 31_10_2025 V2 • ")
