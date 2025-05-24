from flask import session, redirect, url_for, request, render_template
from backend.db_connection import connect_it_work
import random
from datetime import datetime, timedelta

def get_fda_tb_sticker():
    try:
        mock_data = []
        names = ["สมชาย", "สมหญิง", "อนันต์", "จันทนา", "ปิยะ", "ศิริพร"]
        Informer = ["ตัง", "คิม", "จอจ"]
        departments = ["แผนกบัญชี", "แผนกไอที", "แผนกบุคคล", "แผนกจัดซื้อ", "แผนกคลังสินค้า"]
        statuses = ["Complete", "In Progress", "Cancel"]
        subjects = ["Operating System", "Data Report", "Application", "Computer", "Telephone", "Netwrok"]

        for i in range(20):
            mock_record = {
                "No": i + 1,
                "Date": (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S'),
                "Name": random.choice(names),
                "Section": random.choice(departments),
                "Informer": random.choice(Informer),
                "Topic": random.choice(subjects),
                "Detail": f"รายละเอียดการขอรายการที่ {i + 1}",
                "Status": random.choice(statuses),
                "Note": f"หมายเหตุ {i + 1}" if random.random() > 0.3 else ""
            }
            mock_data.append(mock_record)

        return mock_data
    except Exception as e:
        print(f"Error generating mock sticker data: {e}")
        return []

def update_status():
    if request.method == 'POST':
        return redirect(url_for('fda_check_view'))
    return render_template('complete_reason_form.html')