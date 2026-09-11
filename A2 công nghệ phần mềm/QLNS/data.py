import sqlite3
import os


# ================= ĐƯỜNG DẪN DATABASE =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "Nhansu.db")


# ================= KẾT NỐI DATABASE =================

def ket_noi():

    conn = sqlite3.connect(DB_PATH)

    return conn


# ================= TẠO BẢNG NHÂN VIÊN =================

def tao_bang():

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhanvien (

        ma TEXT PRIMARY KEY,

        ten TEXT NOT NULL,

        tuoi INTEGER,

        phongban TEXT,

        chucvu TEXT,

        luong REAL
    )
    """)

    conn.commit()

    conn.close()


# ================= TẠO BẢNG TÀI KHOẢN =================

def tao_bang_tai_khoan():

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS taikhoan (

        username TEXT PRIMARY KEY,

        password TEXT NOT NULL
    )
    """)


    # Kiểm tra tài khoản admin

    cursor.execute("""
    SELECT username FROM taikhoan
    WHERE username = ?
    """, ("admin",))


    tai_khoan = cursor.fetchone()


    # Nếu chưa có admin thì tạo

    if tai_khoan is None:

        cursor.execute("""
        INSERT INTO taikhoan
        VALUES (?, ?)
        """, (
            "admin",
            "123456"
        ))


    conn.commit()

    conn.close()


# ================= KIỂM TRA ĐĂNG NHẬP =================

def kiem_tra_dang_nhap(username, password):

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *

    FROM taikhoan

    WHERE username = ?
    AND password = ?
    """, (
        username,
        password
    ))


    ket_qua = cursor.fetchone()

    conn.close()


    if ket_qua:

        return True

    return False


# ================= THÊM NHÂN VIÊN =================

def them_nhan_vien(ma, ten, tuoi, phongban, chucvu, luong):

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO nhanvien
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        ma,
        ten,
        tuoi,
        phongban,
        chucvu,
        luong
    ))

    conn.commit()

    conn.close()


# ================= LẤY NHÂN VIÊN =================

def lay_nhan_vien():

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM nhanvien
    ORDER BY ma
    """)

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ================= XÓA NHÂN VIÊN =================

def xoa_nhan_vien(ma):

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM nhanvien
    WHERE ma = ?
    """, (ma,))

    conn.commit()

    conn.close()


# ================= SỬA NHÂN VIÊN =================

def sua_nhan_vien(ma, ten, tuoi, phongban, chucvu, luong):

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nhanvien

    SET
        ten = ?,
        tuoi = ?,
        phongban = ?,
        chucvu = ?,
        luong = ?

    WHERE ma = ?
    """, (
        ten,
        tuoi,
        phongban,
        chucvu,
        luong,
        ma
    ))

    conn.commit()

    conn.close()


# ================= TÌM KIẾM NHÂN VIÊN =================

def tim_kiem_nhan_vien(keyword):

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM nhanvien

    WHERE ma LIKE ?
    OR ten LIKE ?
    OR phongban LIKE ?
    OR chucvu LIKE ?

    ORDER BY ma
    """, (
        "%" + keyword + "%",
        "%" + keyword + "%",
        "%" + keyword + "%",
        "%" + keyword + "%"
    ))

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ================= THỐNG KÊ =================

def thong_ke():

    conn = ket_noi()

    cursor = conn.cursor()


    cursor.execute("""
    SELECT COUNT(*)
    FROM nhanvien
    """)

    tong_nv = cursor.fetchone()[0]


    cursor.execute("""
    SELECT COUNT(DISTINCT phongban)
    FROM nhanvien
    WHERE phongban != ''
    """)

    tong_phongban = cursor.fetchone()[0]


    cursor.execute("""
    SELECT COUNT(DISTINCT chucvu)
    FROM nhanvien
    WHERE chucvu != ''
    """)

    tong_chucvu = cursor.fetchone()[0]


    cursor.execute("""
    SELECT SUM(luong)
    FROM nhanvien
    """)

    tong_luong = cursor.fetchone()[0]


    if tong_luong is None:

        tong_luong = 0


    conn.close()


    return (
        tong_nv,
        tong_phongban,
        tong_chucvu,
        tong_luong
    )


# ================= LẤY PHÒNG BAN =================

def lay_phong_ban():

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT phongban

    FROM nhanvien

    WHERE phongban != ''

    ORDER BY phongban
    """)

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ================= LẤY LƯƠNG =================

def lay_luong():

    conn = ket_noi()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT ma, ten, phongban, chucvu, luong

    FROM nhanvien

    ORDER BY luong DESC
    """)

    danh_sach = cursor.fetchall()

    conn.close()

    return danh_sach


# ================= KHỞI TẠO DATABASE =================

tao_bang()

tao_bang_tai_khoan()