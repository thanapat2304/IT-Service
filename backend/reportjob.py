from flask import request, redirect, url_for, render_template
from flask import redirect, url_for
from backend.db_connection import connect_it_work
from mysql.connector import Error

def add_record_it(): 
    if request.method == 'POST':
        return redirect(url_for('dashboard'))

    return render_template('reportjob.html')

def dropdown_one():
    section = [
        "ผู้บริหาร",
        "การเงิน-บัญชี",
        "การตลาด",
        "ประสานงานขาย Sale-Co",
        "ธุรการขาย Admins",
        "ฝ่ายขาย Food-Service",
        "ควบคุมคุณภาพ",
        "ทรัพยากรมนุษย์",
        "นำเข้าสินค้า",
        "พัฒนาธุรกิจ",
        "ปฎิบัติการ-ศุลกากร",
        "คลังสินค้า-สำนักงานใหญ่",
        "คลังสินค้า-สาขา",
        "คลังสินค้า-ลำลูกกา",
        "ขนส่งสินค้า",
        "เทคโนโลยีสารสนเทศ"
    ]
    return section

def dropdown_two():
    topic = [
        "Operating System",
        "Data Report",
        "Application",
        "Computer",
        "Telephone",
        "Netwrok",
        "Monitor",
        "Printer",
        "cctv camera",
        "Other"
    ]
    return topic

def dropdown_three():
    name = [
        "คิม",
        "จอจ",
        "ตัง"
    ]
    return name