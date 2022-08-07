from tkinter import *
import psycopg2 as ps


def show_members_students(user, password, clubid=0):
    cmd = f"select s.studentname, s.studentsrn from student s, part_of p where s.studentsrn=p.studentsrn and p.clubid={clubid};"
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def show_members_teachers(user, password, clubid=0):
    cmd = f"select f.facultyname, f.facultyid from faculty f, member_of m where f.facultyid=m.facultyid and m.clubid={clubid};"
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def show_student_head(user, password, clubid=0):
    cmd = f"select s.studentname, s.studentsrn from club c, student s where c.clubheadsrn=s.studentsrn and c.clubid={clubid};"
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def show_faculty_head(user, password, clubid=0):
    cmd = f"select f.facultyname, f.facultyid from club c, faculty f where c.clubheadfid=f.facultyid and c.clubid={clubid};"
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def show_events(user, password, clubid=0):
    cmd = f"select e.eventname from event e, conducts c where e.eventid = c.eventid and c.clubid={clubid};"
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def insert_new_event(user, password, clubid=0):
    def combine():
        conn = ps.connect(database="clubdbms", user=user,
                          password=password, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        cmd = f"INSERT into EVENT values ({budget.get()}, '{desc.get()}', '{loc.get()}', '{date.get()}', \
        {eid.get()}, {pno.get()}, '{ename.get()}');"
        cur.execute(cmd)
        cmd = f"INSERT into CONDUCTS values ({eid.get()}, {clubid});"
        cur.execute(cmd)
        conn.commit()
        conn.close()

    ine_window = Toplevel(login)
    ine_window.title("New Event")
    ine_window.geometry("720x480")

    text = StringVar()
    text.set("Budget")
    budget = Entry(ine_window, textvariable=text)
    budget.place(x=30, y=30)

    text = StringVar()
    text.set("Description")
    desc = Entry(ine_window, textvariable=text)
    desc.place(x=30, y=225)

    text = StringVar()
    text.set("Location")
    loc = Entry(ine_window, textvariable=text)
    loc.place(x=30, y=420)

    text = StringVar()
    text.set("Date")
    date = Entry(ine_window, textvariable=text)
    date.place(x=315, y=30)

    text = StringVar()
    text.set("Event ID")
    eid = Entry(ine_window, textvariable=text)
    eid.place(x=315, y=225)

    text = StringVar()
    text.set("Participant Number")
    pno = Entry(ine_window, textvariable=text)
    pno.place(x=315, y=420)

    text = StringVar()
    text.set("Event Name")
    ename = Entry(ine_window, textvariable=text)
    ename.place(x=600, y=30)

    execute_button = Button(ine_window, text="Execute", font=(
        'bold', 10), command=lambda: combine())
    execute_button.place(x=600, y=225)


def insert_new_students(user, password, clubid=0):
    def combine():
        conn = ps.connect(database="clubdbms", user=user,
                          password=password, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        cmd = f"INSERT into EVENT values ('{Name.get()}', {GPA.get()}, {Semester.get()}, '{SRN.get()}', \
        '{Dept.get()}', '{email.get()}', '{phone.get()}');"
        cur.execute(cmd)
        cmd = f"INSERT into PART_OF values ('{SRN.get()}', {clubid}, {GPA.get()});"
        cur.execute(cmd)
        conn.commit()
        conn.close()

    ins_window = Toplevel(login)
    ins_window.title("New Student")
    ins_window.geometry("720x480")

    text = StringVar()
    text.set("Name")
    Name = Entry(ins_window, textvariable=text)
    Name.place(x=30, y=30)

    text = StringVar()
    text.set("GPA")
    GPA = Entry(ins_window, textvariable=text)
    GPA.place(x=30, y=225)

    text = StringVar()
    text.set("Semester")
    Semester = Entry(ins_window, textvariable=text)
    Semester.place(x=30, y=420)

    text = StringVar()
    text.set("SRN")
    SRN = Entry(ins_window, textvariable=text)
    SRN.place(x=315, y=30)

    text = StringVar()
    text.set("Department")
    Dept = Entry(ins_window, textvariable=text)
    Dept.place(x=315, y=225)

    text = StringVar()
    text.set("Email ID")
    email = Entry(ins_window, textvariable=text)
    email.place(x=315, y=420)

    text = StringVar()
    text.set("Phone Number")
    phone = Entry(ins_window, textvariable=text)
    phone.place(x=600, y=30)

    execute_button = Button(ins_window, text="Execute", font=(
        'bold', 10), command=lambda: combine())
    execute_button.place(x=600, y=225)


def insert_new_teachers(user, password, clubid=0):
    def combine():
        conn = ps.connect(database="clubdbms", user=user,
                          password=password, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        cmd = f"INSERT into FACULTY values (({First_Name.get()}, {Middle_Name.get()}, {Last_Name.get()}), {Faculty_ID.get()}, {email.get()}, {designation.get()})"
        cur.execute(cmd)
        cmd = f"INSERT into FACULTY_DEPARTMENT values ('{Dept.get()}', {Faculty_ID.get()});"
        cur.execute(cmd)
        cmd = f"INSERT into MEMBER_OF values ({clubid}, {Faculty_ID.get()});"
        cur.execute(cmd)
        conn.commit()
        conn.close()

    int_window = Toplevel(login)
    int_window.title("New Faculty")
    int_window.geometry("720x480")

    text = StringVar()
    text.set("First Name")
    First_Name = Entry(int_window, textvariable=text)
    First_Name.place(x=30, y=30)

    text = StringVar()
    text.set("Middle Name")
    Middle_Name = Entry(int_window, textvariable=text)
    Middle_Name.place(x=30, y=225)

    text = StringVar()
    text.set("Last Name")
    Last_Name = Entry(int_window, textvariable=text)
    Last_Name.place(x=30, y=420)

    text = StringVar()
    text.set("Faculty ID")
    Faculty_ID = Entry(int_window, textvariable=text)
    Faculty_ID.place(x=315, y=30)

    text = StringVar()
    text.set("Department")
    Dept = Entry(int_window, textvariable=text)
    Dept.place(x=315, y=225)

    text = StringVar()
    text.set("Email ID")
    email = Entry(int_window, textvariable=text)
    email.place(x=315, y=420)

    text = StringVar()
    text.set("Designation")
    designation = Entry(int_window, textvariable=text)
    designation.place(x=600, y=30)

    execute_button = Button(int_window, text="Execute", font=(
        'bold', 10), command=lambda: combine())
    execute_button.place(x=600, y=225)


def show_csr(user, password):
    csr_window = Toplevel(login)
    csr_window.title("CSR Club")
    csr_window.geometry("720x480")

    members_students = Button(csr_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=1))
    members_students.place(x=30, y=30)

    members_teachers = Button(csr_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=1))
    members_teachers.place(x=30, y=225)

    student_head = Button(csr_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=1))
    student_head.place(x=30, y=420)

    faculty_head = Button(csr_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=1))
    faculty_head.place(x=315, y=30)

    new_event = Button(csr_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=1))
    new_event.place(x=315, y=225)

    new_students = Button(csr_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=1))
    new_students.place(x=315, y=420)

    new_teachers = Button(csr_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=1))
    new_teachers.place(x=600, y=30)

    events = Button(csr_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=1))
    events.place(x=600, y=225)


def show_qqc(user, password):
    qqc_window = Toplevel(login)
    qqc_window.title("QQC Club")
    qqc_window.geometry("720x480")

    members_students = Button(qqc_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=2))
    members_students.place(x=30, y=30)

    members_teachers = Button(qqc_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=2))
    members_teachers.place(x=30, y=225)

    student_head = Button(qqc_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=2))
    student_head.place(x=30, y=420)

    faculty_head = Button(qqc_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=2))
    faculty_head.place(x=315, y=30)

    new_event = Button(qqc_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=2))
    new_event.place(x=315, y=225)

    new_students = Button(qqc_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=2))
    new_students.place(x=315, y=420)

    new_teachers = Button(qqc_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=2))
    new_teachers.place(x=600, y=30)

    events = Button(qqc_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=2))
    events.place(x=600, y=225)


def show_eqx(user, password):
    eqx_window = Toplevel(login)
    eqx_window.title("Equinox Club")
    eqx_window.geometry("720x480")

    members_students = Button(eqx_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=3))
    members_students.place(x=30, y=30)

    members_teachers = Button(eqx_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=3))
    members_teachers.place(x=30, y=225)

    student_head = Button(eqx_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=3))
    student_head.place(x=30, y=420)

    faculty_head = Button(eqx_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=3))
    faculty_head.place(x=315, y=30)

    new_event = Button(eqx_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=3))
    new_event.place(x=315, y=225)

    new_students = Button(eqx_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=3))
    new_students.place(x=315, y=420)

    new_teachers = Button(eqx_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=3))
    new_teachers.place(x=600, y=30)

    events = Button(eqx_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=3))
    events.place(x=600, y=225)


def show_qft(user, password):
    qft_window = Toplevel(login)
    qft_window.title("QForest Club")
    qft_window.geometry("720x480")

    members_students = Button(qft_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=4))
    members_students.place(x=30, y=30)

    members_teachers = Button(qft_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=4))
    members_teachers.place(x=30, y=225)

    student_head = Button(qft_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=4))
    student_head.place(x=30, y=420)

    faculty_head = Button(qft_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=4))
    faculty_head.place(x=315, y=30)

    new_event = Button(qft_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=4))
    new_event.place(x=315, y=225)

    new_students = Button(qft_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=4))
    new_students.place(x=315, y=420)

    new_teachers = Button(qft_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=4))
    new_teachers.place(x=600, y=30)

    events = Button(qft_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=4))
    events.place(x=600, y=225)


def show_aol(user, password):
    aol_window = Toplevel(login)
    aol_window.title("Aeolus Club")
    aol_window.geometry("720x480")

    members_students = Button(aol_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=5))
    members_students.place(x=30, y=30)

    members_teachers = Button(aol_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=5))
    members_teachers.place(x=30, y=225)

    student_head = Button(aol_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=5))
    student_head.place(x=30, y=420)

    faculty_head = Button(aol_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=5))
    faculty_head.place(x=315, y=30)

    new_event = Button(aol_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=5))
    new_event.place(x=315, y=225)

    new_students = Button(aol_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=5))
    new_students.place(x=315, y=420)

    new_teachers = Button(aol_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=5))
    new_teachers.place(x=600, y=30)

    events = Button(aol_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=5))
    events.place(x=600, y=225)


def show_th(user, password):
    th_window = Toplevel(login)
    th_window.title("Team Haya")
    th_window.geometry("720x480")

    members_students = Button(th_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=6))
    members_students.place(x=30, y=30)

    members_teachers = Button(th_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=6))
    members_teachers.place(x=30, y=225)

    student_head = Button(th_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=6))
    student_head.place(x=30, y=420)

    faculty_head = Button(th_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=6))
    faculty_head.place(x=315, y=30)

    new_event = Button(th_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=6))
    new_event.place(x=315, y=225)

    new_students = Button(th_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=6))
    new_students.place(x=315, y=420)

    new_teachers = Button(th_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=6))
    new_teachers.place(x=600, y=30)

    events = Button(th_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=6))
    events.place(x=600, y=225)


def show_tv(user, password):
    tv_window = Toplevel(login)
    tv_window.title("Team Vega")
    tv_window.geometry("720x480")

    members_students = Button(tv_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=7))
    members_students.place(x=30, y=30)

    members_teachers = Button(tv_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=7))
    members_teachers.place(x=30, y=225)

    student_head = Button(tv_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=7))
    student_head.place(x=30, y=420)

    faculty_head = Button(tv_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=7))
    faculty_head.place(x=315, y=30)

    new_event = Button(tv_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=7))
    new_event.place(x=315, y=225)

    new_students = Button(tv_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=7))
    new_students.place(x=315, y=420)

    new_teachers = Button(tv_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=7))
    new_teachers.place(x=600, y=30)

    events = Button(tv_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=7))
    events.place(x=600, y=225)


def show_tn(user, password):
    tn_window = Toplevel(login)
    tn_window.title("Team Nautanki")
    tn_window.geometry("720x480")

    members_students = Button(tn_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=8))
    members_students.place(x=30, y=30)

    members_teachers = Button(tn_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=8))
    members_teachers.place(x=30, y=225)

    student_head = Button(tn_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=8))
    student_head.place(x=30, y=420)

    faculty_head = Button(tn_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=8))
    faculty_head.place(x=315, y=30)

    new_event = Button(tn_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=8))
    new_event.place(x=315, y=225)

    new_students = Button(tn_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=8))
    new_students.place(x=315, y=420)

    new_teachers = Button(tn_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=8))
    new_teachers.place(x=600, y=30)

    events = Button(tn_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=8))
    events.place(x=600, y=225)


def show_tnid(user, password):
    tnid_window = Toplevel(login)
    tnid_window.title("Team Vega")
    tnid_window.geometry("720x480")

    members_students = Button(tnid_window, text="Students", font=(
        'bold', 10), command=lambda: show_members_students(user, password, clubid=9))
    members_students.place(x=30, y=30)

    members_teachers = Button(tnid_window, text="Teachers", font=(
        'bold', 10), command=lambda: show_members_teachers(user, password, clubid=9))
    members_teachers.place(x=30, y=225)

    student_head = Button(tnid_window, text="Student Head", font=(
        'bold', 10), command=lambda: show_student_head(user, password, clubid=9))
    student_head.place(x=30, y=420)

    faculty_head = Button(tnid_window, text="Faculty Head", font=(
        'bold', 10), command=lambda: show_faculty_head(user, password, clubid=9))
    faculty_head.place(x=315, y=30)

    new_event = Button(tnid_window, text="New Event", font=(
        'bold', 10), command=lambda: insert_new_event(user, password, clubid=9))
    new_event.place(x=315, y=225)

    new_students = Button(tnid_window, text="New Students", font=(
        'bold', 10), command=lambda: insert_new_students(user, password, clubid=9))
    new_students.place(x=315, y=420)

    new_teachers = Button(tnid_window, text="New Teachers", font=(
        'bold', 10), command=lambda: insert_new_teachers(user, password, clubid=9))
    new_teachers.place(x=600, y=30)

    events = Button(tnid_window, text="Events", font=(
        'bold', 10), command=lambda: show_events(user, password, clubid=9))
    events.place(x=600, y=225)


def exec_custom(cmd, user, password):
    cmd.lower()

    try:
        conn = ps.connect(database="clubdbms", user=user,
                          password=password, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        cur.execute(cmd)

        if cmd.startswith("select"):
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()
        print("Command Successful")
    except Exception as e:
        print(e)


def roots(user='postgres', password='postgres'):
    conn = ps.connect(database="clubdbms", user=user,
                      password=password, host="127.0.0.1", port="5432")

    root = Toplevel(login)
    root.geometry("720x600")
    root.title("CLUB-DBMS")

    csr = Button(root, text="CSR Club", font=(
        'bold', 10), command=lambda: show_csr(user, password))
    csr.place(x=30, y=30)

    qqc = Button(root, text="QQC Club", font=(
        'bold', 10), command=lambda: show_qqc(user, password))
    qqc.place(x=30, y=225)

    eqx = Button(root, text="Equinox Club", font=(
        'bold', 10), command=lambda: show_eqx(user, password))
    eqx.place(x=30, y=420)

    qft = Button(root, text="QForest Club", font=(
        'bold', 10), command=lambda: show_qft(user, password))
    qft.place(x=315, y=30)

    aol = Button(root, text="Aeolus Club", font=(
        'bold', 10), command=lambda: show_aol(user, password))
    aol.place(x=315, y=225)

    th = Button(root, text="Team Haya", font=(
        'bold', 10), command=lambda: show_th(user, password))
    th.place(x=315, y=420)

    tv = Button(root, text="Team Vega", font=(
        'bold', 10), command=lambda: show_tv(user, password))
    tv.place(x=600, y=30)

    tn = Button(root, text="Team Nautanki", font=(
        'bold', 10), command=lambda: show_tn(user, password))
    tn.place(x=600, y=225)

    tnid = Button(root, text="Team Ninaada", font=(
        'bold', 10), command=lambda: show_tnid(user, password))
    tnid.place(x=600, y=420)

    custom = Text(root, height=2, width=50)
    execute = Button(root, text="EXECUTE", font=('bold', 10),
                     command=lambda: exec_custom(custom.get(1.0, "end-1c"), user, password))
    custom.place(x=180, y=475)
    execute.place(x=315, y=540)

    conn.commit()
    conn.close()


login = Tk()
login.geometry("720x600")
login.title("CLUB-DBMS")

text = StringVar()
text.set("User")
User = Entry(login, textvariable=text)
User.place(x=30, y=30)

text = StringVar()
text.set("Password")
Password = Entry(login, textvariable=text)
Password.place(x=600, y=30)

Execute = Button(login, text="Login", font=(
    'bold', 10), command=lambda: roots(User.get(), Password.get()))
Execute.place(x=340, y=225)

if __name__ == "__main__":
    login.mainloop()
