import customtkinter as ctk

import os
import sys


# ================= ĐƯỜNG DẪN =================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


GIAODIEN_PATH = os.path.join(
    BASE_DIR,
    "Giaodien"
)


sys.path.append(
    GIAODIEN_PATH
)


# ================= IMPORT =================

from dangnhap import mo_dang_nhap

from giaodien import hien_dashboard

from nhanvien import hien_nhan_vien

from phongban import hien_phong_ban

from luong import hien_luong


# ================= CẤU HÌNH =================

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")


# ================= CỬA SỔ =================

app = ctk.CTk()

app.title(
    "HR SYSTEM - Quản lý nhân sự"
)

app.geometry(
    "1250x750"
)

app.minsize(
    1000,
    650
)


# =================================================
# MỞ GIAO DIỆN CHÍNH
# =================================================

def mo_he_thong():

    # Xóa màn hình đăng nhập

    for widget in app.winfo_children():

        widget.destroy()


    # ================= SIDEBAR =================

    sidebar = ctk.CTkFrame(
        app,
        width=230,
        corner_radius=0
    )

    sidebar.pack(
        side="left",
        fill="y"
    )


    # ================= LOGO =================

    logo = ctk.CTkLabel(
        sidebar,
        text="HR SYSTEM",
        font=("Arial", 26, "bold")
    )

    logo.pack(
        pady=(35, 0)
    )


    logo_sub = ctk.CTkLabel(
        sidebar,
        text="QUẢN LÝ NHÂN SỰ",
        font=("Arial", 12)
    )

    logo_sub.pack(
        pady=(0, 35)
    )


    # ================= MAIN =================

    main_frame = ctk.CTkFrame(
        app,
        corner_radius=0,
        fg_color="transparent"
    )

    main_frame.pack(
        side="right",
        fill="both",
        expand=True
    )


    # ================= TOPBAR =================

    topbar = ctk.CTkFrame(
        main_frame,
        height=70,
        corner_radius=0
    )

    topbar.pack(
        fill="x"
    )


    top_title = ctk.CTkLabel(
        topbar,
        text="Hệ thống quản lý nhân sự",
        font=("Arial", 20, "bold")
    )

    top_title.pack(
        side="left",
        padx=30,
        pady=15
    )


    admin = ctk.CTkLabel(
        topbar,
        text="👤 Admin",
        font=("Arial", 15)
    )

    admin.pack(
        side="right",
        padx=30
    )


    # ================= CONTENT =================

    content = ctk.CTkFrame(
        main_frame,
        corner_radius=0,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True
    )


    # =================================================
    # MỞ CÁC TRANG
    # =================================================

    def mo_dashboard():

        hien_dashboard(content)


    def mo_nhan_vien():

        hien_nhan_vien(content)


    def mo_phong_ban():

        hien_phong_ban(content)


    def mo_luong():

        hien_luong(content)


    # ================= ĐĂNG XUẤT =================

    def dang_xuat():

        result = ctk.CTkInputDialog(
            text="Nhập YES để xác nhận đăng xuất",
            title="Đăng xuất"
        )

        answer = result.get_input()


        if answer == "YES":

            mo_dang_nhap(
                app,
                mo_he_thong
            )


    # ================= MENU =================

    btn_dashboard = ctk.CTkButton(
        sidebar,
        text="🏠   Dashboard",
        anchor="w",
        height=45,
        command=mo_dashboard
    )

    btn_dashboard.pack(
        fill="x",
        padx=15,
        pady=5
    )


    btn_nhanvien = ctk.CTkButton(
        sidebar,
        text="👥   Nhân viên",
        anchor="w",
        height=45,
        command=mo_nhan_vien
    )

    btn_nhanvien.pack(
        fill="x",
        padx=15,
        pady=5
    )


    btn_phongban = ctk.CTkButton(
        sidebar,
        text="🏢   Phòng ban",
        anchor="w",
        height=45,
        command=mo_phong_ban
    )

    btn_phongban.pack(
        fill="x",
        padx=15,
        pady=5
    )


    btn_luong = ctk.CTkButton(
        sidebar,
        text="💰   Quản lý lương",
        anchor="w",
        height=45,
        command=mo_luong
    )

    btn_luong.pack(
        fill="x",
        padx=15,
        pady=5
    )


    # ================= ĐĂNG XUẤT =================

    btn_logout = ctk.CTkButton(
        sidebar,
        text="🚪   Đăng xuất",
        anchor="w",
        height=45,
        command=dang_xuat
    )

    btn_logout.pack(
        side="bottom",
        fill="x",
        padx=15,
        pady=20
    )


    # ================= VERSION =================

    version = ctk.CTkLabel(
        sidebar,
        text="HR SYSTEM v1.0",
        font=("Arial", 12)
    )

    version.pack(
        side="bottom",
        pady=5
    )


    # ================= MỞ DASHBOARD =================

    mo_dashboard()


# =================================================
# MỞ ĐĂNG NHẬP
# =================================================

mo_dang_nhap(
    app,
    mo_he_thong
)


# =================================================
# CHẠY
# =================================================

app.mainloop()