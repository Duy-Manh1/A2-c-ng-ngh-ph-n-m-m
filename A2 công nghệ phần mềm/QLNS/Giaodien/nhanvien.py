import customtkinter as ctk

from tkinter import ttk
from tkinter import messagebox

import sqlite3

from data import them_nhan_vien
from data import lay_nhan_vien
from data import xoa_nhan_vien
from data import sua_nhan_vien
from data import tim_kiem_nhan_vien


# ================= XÓA NỘI DUNG =================

def xoa_noi_dung(content):

    for widget in content.winfo_children():

        widget.destroy()


# ================= HIỂN THỊ TRANG =================

def hien_nhan_vien(content):

    xoa_noi_dung(content)


    # ================= TIÊU ĐỀ =================

    title = ctk.CTkLabel(
        content,
        text="Quản lý nhân viên",
        font=("Arial", 28, "bold")
    )

    title.pack(
        anchor="w",
        padx=30,
        pady=(25, 5)
    )


    subtitle = ctk.CTkLabel(
        content,
        text="Thêm, sửa, xóa và tìm kiếm nhân viên",
        font=("Arial", 14)
    )

    subtitle.pack(
        anchor="w",
        padx=30,
        pady=(0, 15)
    )


    # ================= TÌM KIẾM =================

    search_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    search_frame.pack(
        fill="x",
        padx=30,
        pady=5
    )


    search_entry = ctk.CTkEntry(
        search_frame,
        width=300,
        height=40,
        placeholder_text="🔍 Nhập tên, mã hoặc phòng ban..."
    )

    search_entry.pack(
        side="left"
    )


    # ================= FORM =================

    form_frame = ctk.CTkFrame(
        content,
        corner_radius=15
    )

    form_frame.pack(
        fill="x",
        padx=30,
        pady=15
    )


    # Mã

    entry_ma = ctk.CTkEntry(
        form_frame,
        placeholder_text="Mã nhân viên",
        width=180
    )

    entry_ma.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )


    # Tên

    entry_ten = ctk.CTkEntry(
        form_frame,
        placeholder_text="Họ và tên",
        width=220
    )

    entry_ten.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )


    # Tuổi

    entry_tuoi = ctk.CTkEntry(
        form_frame,
        placeholder_text="Tuổi",
        width=120
    )

    entry_tuoi.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )


    # Phòng ban

    entry_phongban = ctk.CTkEntry(
        form_frame,
        placeholder_text="Phòng ban",
        width=180
    )

    entry_phongban.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )


    # Chức vụ

    entry_chucvu = ctk.CTkEntry(
        form_frame,
        placeholder_text="Chức vụ",
        width=220
    )

    entry_chucvu.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )


    # Lương

    entry_luong = ctk.CTkEntry(
        form_frame,
        placeholder_text="Lương",
        width=120
    )

    entry_luong.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )


    # ================= KHUNG NÚT =================

    button_frame = ctk.CTkFrame(
        form_frame,
        fg_color="transparent"
    )

    button_frame.grid(
        row=0,
        column=3,
        rowspan=2,
        padx=15
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
        pady=(5, 25)
    )


    columns = (
        "ma",
        "ten",
        "tuoi",
        "phongban",
        "chucvu",
        "luong"
    )


    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    # Tiêu đề bảng

    table.heading("ma", text="Mã NV")
    table.heading("ten", text="Họ tên")
    table.heading("tuoi", text="Tuổi")
    table.heading("phongban", text="Phòng ban")
    table.heading("chucvu", text="Chức vụ")
    table.heading("luong", text="Lương")


    # Độ rộng

    table.column("ma", width=100)
    table.column("ten", width=180)
    table.column("tuoi", width=70)
    table.column("phongban", width=150)
    table.column("chucvu", width=150)
    table.column("luong", width=150)


    table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )


    # ================= HÀM =================

    def xoa_o_nhap():

        entry_ma.delete(0, "end")
        entry_ten.delete(0, "end")
        entry_tuoi.delete(0, "end")
        entry_phongban.delete(0, "end")
        entry_chucvu.delete(0, "end")
        entry_luong.delete(0, "end")


    def tai_du_lieu():

        for item in table.get_children():

            table.delete(item)


        danh_sach = lay_nhan_vien()


        for nv in danh_sach:

            table.insert(
                "",
                "end",
                values=nv
            )


    def them():

        ma = entry_ma.get().strip()
        ten = entry_ten.get().strip()
        tuoi = entry_tuoi.get().strip()
        phongban = entry_phongban.get().strip()
        chucvu = entry_chucvu.get().strip()
        luong = entry_luong.get().strip()


        if ma == "" or ten == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã và tên nhân viên!"
            )

            return


        # Kiểm tra tuổi

        try:

            if tuoi == "":
                tuoi = 0

            else:
                tuoi = int(tuoi)

        except:

            messagebox.showerror(
                "Lỗi",
                "Tuổi phải là số!"
            )

            return


        # Kiểm tra lương

        try:

            if luong == "":
                luong = 0

            else:
                luong = float(luong)

        except:

            messagebox.showerror(
                "Lỗi",
                "Lương phải là số!"
            )

            return


        try:

            them_nhan_vien(
                ma,
                ten,
                tuoi,
                phongban,
                chucvu,
                luong
            )


            messagebox.showinfo(
                "Thành công",
                "Đã thêm nhân viên!"
            )


            xoa_o_nhap()

            tai_du_lieu()


        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Lỗi",
                "Mã nhân viên đã tồn tại!"
            )


    def chon_nhan_vien(event):

        selected = table.focus()


        if selected == "":

            return


        values = table.item(
            selected,
            "values"
        )


        xoa_o_nhap()


        entry_ma.insert(0, values[0])
        entry_ten.insert(0, values[1])
        entry_tuoi.insert(0, values[2])
        entry_phongban.insert(0, values[3])
        entry_chucvu.insert(0, values[4])
        entry_luong.insert(0, values[5])


    def sua():

        ma = entry_ma.get().strip()


        if ma == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn nhân viên!"
            )

            return


        ten = entry_ten.get().strip()
        tuoi = entry_tuoi.get().strip()
        phongban = entry_phongban.get().strip()
        chucvu = entry_chucvu.get().strip()
        luong = entry_luong.get().strip()


        try:

            if tuoi == "":
                tuoi = 0

            else:
                tuoi = int(tuoi)


            if luong == "":
                luong = 0

            else:
                luong = float(luong)


        except:

            messagebox.showerror(
                "Lỗi",
                "Tuổi hoặc lương không hợp lệ!"
            )

            return


        sua_nhan_vien(
            ma,
            ten,
            tuoi,
            phongban,
            chucvu,
            luong
        )


        messagebox.showinfo(
            "Thành công",
            "Đã cập nhật nhân viên!"
        )


        tai_du_lieu()


    def xoa():

        selected = table.focus()


        if selected == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn nhân viên!"
            )

            return


        values = table.item(
            selected,
            "values"
        )


        ma = values[0]


        result = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa nhân viên này?"
        )


        if result:

            xoa_nhan_vien(ma)

            tai_du_lieu()

            xoa_o_nhap()

            messagebox.showinfo(
                "Thành công",
                "Đã xóa nhân viên!"
            )


    def tim_kiem():

        keyword = search_entry.get().strip()


        for item in table.get_children():

            table.delete(item)


        danh_sach = tim_kiem_nhan_vien(keyword)


        for nv in danh_sach:

            table.insert(
                "",
                "end",
                values=nv
            )


    # ================= NÚT =================

    btn_them = ctk.CTkButton(
        button_frame,
        text="➕ Thêm",
        width=130,
        command=them
    )

    btn_them.pack(
        pady=5
    )


    btn_sua = ctk.CTkButton(
        button_frame,
        text="✏ Sửa",
        width=130,
        command=sua
    )

    btn_sua.pack(
        pady=5
    )


    btn_xoa = ctk.CTkButton(
        button_frame,
        text="🗑 Xóa",
        width=130,
        command=xoa
    )

    btn_xoa.pack(
        pady=5
    )


    # ================= NÚT TÌM KIẾM =================

    btn_search = ctk.CTkButton(
        search_frame,
        text="Tìm kiếm",
        height=40,
        width=110,
        command=tim_kiem
    )

    btn_search.pack(
        side="left",
        padx=10
    )


    btn_all = ctk.CTkButton(
        search_frame,
        text="Tất cả",
        height=40,
        width=100,
        command=tai_du_lieu
    )

    btn_all.pack(
        side="left"
    )


    # Chọn nhân viên

    table.bind(
        "<<TreeviewSelect>>",
        chon_nhan_vien
    )


    # Tải dữ liệu

    tai_du_lieu()