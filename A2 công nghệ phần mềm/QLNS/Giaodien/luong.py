import customtkinter as ctk

from tkinter import ttk

from data import lay_luong


# ================= XÓA NỘI DUNG =================

def xoa_noi_dung(content):

    for widget in content.winfo_children():

        widget.destroy()


# ================= QUẢN LÝ LƯƠNG =================

def hien_luong(content):

    xoa_noi_dung(content)


    # Tiêu đề

    title = ctk.CTkLabel(
        content,
        text="Quản lý lương",
        font=("Arial", 28, "bold")
    )

    title.pack(
        anchor="w",
        padx=30,
        pady=(30, 5)
    )


    subtitle = ctk.CTkLabel(
        content,
        text="Danh sách lương nhân viên",
        font=("Arial", 15)
    )

    subtitle.pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )


    # Khung tổng

    tong_frame = ctk.CTkFrame(
        content,
        corner_radius=15
    )

    tong_frame.pack(
        fill="x",
        padx=30,
        pady=10
    )


    danh_sach = lay_luong()


    tong_luong = 0


    for nv in danh_sach:

        tong_luong += nv[4]


    label_tong = ctk.CTkLabel(
        tong_frame,
        text=f"💰 Tổng quỹ lương: {tong_luong:,.0f} VNĐ",
        font=("Arial", 22, "bold")
    )

    label_tong.pack(
        padx=20,
        pady=20
    )


    # ================= BẢNG =================

    table_frame = ctk.CTkFrame(
        content,
        corner_radius=15
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(10, 30)
    )


    columns = (
        "ma",
        "ten",
        "phongban",
        "chucvu",
        "luong"
    )


    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    table.heading(
        "ma",
        text="Mã NV"
    )

    table.heading(
        "ten",
        text="Họ tên"
    )

    table.heading(
        "phongban",
        text="Phòng ban"
    )

    table.heading(
        "chucvu",
        text="Chức vụ"
    )

    table.heading(
        "luong",
        text="Lương"
    )


    table.column(
        "ma",
        width=100
    )

    table.column(
        "ten",
        width=200
    )

    table.column(
        "phongban",
        width=180
    )

    table.column(
        "chucvu",
        width=180
    )

    table.column(
        "luong",
        width=180
    )


    table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )


    # Thêm dữ liệu

    for nv in danh_sach:

        table.insert(
            "",
            "end",
            values=(
                nv[0],
                nv[1],
                nv[2],
                nv[3],
                f"{nv[4]:,.0f} VNĐ"
            )
        )