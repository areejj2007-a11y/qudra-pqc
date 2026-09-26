import random
import time
import streamlit as st

st.set_page_config(page_title="الدرع السعودي | Saudi Shield PQC", layout="wide")

# إدارة حالة تسجيل الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- شاشة تسجيل الدخول الوهمية ---
if not st.session_state.logged_in:
    st.title("🛡️ بوابة الدخول السيادية | الدرع السعودي")
    st.markdown("🔒 **يرجى إدخال بيانات الاعتماد المعتمدة للوصول إلى النظام الآمن**")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("اسم المستخدم (Username)", value="admin_security")
            password = st.text_input("كلمة المرور (Password)", type="password", value="secure_pass")
            submit_button = st.form_submit_button(label="تسجيل الدخول الآمن 🔐")
            
            if submit_button:
                with st.spinner("جاري التحقق من الهوية الرقمية عبر البصمة الكمية..."):
                    time.sleep(1)
                st.session_state.logged_in = True
                st.rerun()

# --- لوحة التحكم الرئيسية (تظهر بعد تسجيل الدخول) ---
else:
    st.title("🛡️ الدرع السعودي | Saudi Shield PQC & AI Guardian")
    st.markdown("🔒 **البنية التحتية الرقمية السيادية في عصر ما بعد الكوانتم (Post-Quantum Cryptography)**")
    st.markdown("---")

    # مؤشرات الأداء السيادي (Metrics)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="خوارزمية التشفير", value="CRYSTALS-Kyber", delta="مقاومة كمية متقدمة")
    with col2:
        st.metric(label="حالة الذكاء الاصطناعي", value="AI Guardian Active", delta="مراقبة لحظية ⚡")
    with col3:
        st.metric(label="البيانات التي تم حمايتها", value="1,489", delta="سجل البيانات الآمنة")

    st.markdown("---")

    # قناة الاتصال المشفرة
    st.markdown("### 🌐 قناة الاتصال المشفرة المحمية (Symmetric Data Tunnel)")
    new_hash = hex(random.randint(10000000, 99999999))
    st.code(f"New Secure Stream: 0x{new_hash.upper()}... [تم تدوير المفاتيح والتحقق منها بنجاح]", language="python")

    # قسم الأزرار التفاعلية للعرض
    st.markdown("### ⚡ محاكاة الحماية واختبار الذكاء الاصطناعي")
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("🔄 محاكاة تدوير المفاتيح (Key Rotation)"):
            with st.spinner("جاري توليد مفاتيح تشفير جديدة مقاومة للكوانتم..."):
                time.sleep(1)
            st.success("✅ تم تغيير وتحديث المفاتيح بنجاح طيرانياً وبدون أي تسريب للبيانات.")

    with col_btn2:
        if st.button("⚠️ إطلاق محاكاة هجوم الكوانتم (Quantum Attack)"):
            with st.spinner("جاري رصد محاولة الاختراق الكمي..."):
                time.sleep(1)
            st.error("🚨 [تنبيه الحارس الذكي]: تم رصد محاولة فك تشفير كمية وتم التصدي لها وفصل القناة فوراً!")
            st.info("🛡️ تم تحويل النظام تلقائياً إلى طبقة الحماية السيادية البديلة بنجاح تام.")

    st.markdown("---")
    
    # زر لتسجيل الخروج لو حبيتي تعيدين التجربة قدام الدكاترة
    if st.button("🚪 تسجيل الخروج (إعادة تعيين العرض)"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<p style='text-align: center; color: gray;'>مشروع الدرع السعودي - مصمم خصيصاً للمنصات السيادية والجهات الحيوية في المملكة 🇸🇦</p>", unsafe_allow_html=True)
