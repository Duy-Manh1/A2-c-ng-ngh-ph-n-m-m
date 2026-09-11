import customtkinter as ctk

from tkinter import messagebox

from data import kiem_tra_dang_nhap


def mo_dang_nhap(app, khi_dang_nhap_thanh_cong):

    # Xóa giao diện cũ

    for widget in app.winfo_children():

        widget.destroy()


    # ================= KHUNG CHÍNH =================

    main_frame = ctk.CTkFrame(
        app,
        corner_radius=0
    )

    main_frame.pack(
        fill="both",
        expand=True
    )


    # ================= KHUNG ĐĂNG NHẬP =================

    login_frame = ctk.CTkFrame(
        main_frame,
        width=420,
        height=500,
        corner_radius=20
    )

    login_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )


    # ================= LOGO =================

    logo = ctk.CTkLabel(
        login_frame,
        text="👥",
        font=("Arial", 60)
    )

    logo.pack(
        pady=(45, 10)
    )


    # ================= TIÊU ĐỀ =================

    title = ctk.CTkLabel(
        login_frame,
        text="HR SYSTEM",
        font=("Arial", 28, "bold")
    )

    title.pack(
        pady=(5, 0)
    )


    subtitle = ctk.CTkLabel(
        login_frame,
        text="Hệ thống quản lý nhân sự",
        font=("Arial", 15)
    )

    subtitle.pack(
        pady=(0, 30)
    )


    # ================= USERNAME =================

    entry_username = ctk.CTkEntry(
        login_frame,
        width=300,
        height=45,
        placeholder_text="Tên đăng nhập"
    )

    entry_username.pack(
        pady=10
    )


    # ================= PASSWORD =================

    entry_password = ctk.CTkEntry(
        login_frame,
        width=300,
        height=45,
        placeholder_text="Mật khẩu",
        show="*"
    )

    entry_password.pack(
        pady=10
    )


    # ================= ĐĂNG NHẬP =================

    def dang_nhap():

        username = entry_username.get().strip()

        password = entry_password.get().strip()


        if username == "" or password == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ thông tin!"
            )

            return


        if kiem_tra_dang_nhap(username, password):

            messagebox.showinfo(
                "Thành công",
                "Đăng nhập thành công!"
            )

            khi_dang_nhap_thanh_cong()

        else:

            messagebox.showerror(
                "Lỗi",
                "Tên đăng nhập hoặc mật khẩu không đúng!"
            )


    # ================= NÚT =================

    btn_login = ctk.CTkButton(
        login_frame,
        text="ĐĂNG NHẬP",
        width=300,
        height=45,
        font=("Arial", 15, "bold"),
        command=dang_nhap
    )

    btn_login.pack(
        pady=25
    )


    # ================= THÔNG TIN =================

    info = ctk.CTkLabel(
        login_frame,
        text="Tài khoản mặc định: admin\nMật khẩu: 123456",
        font=("Arial", 12)
    )

    info.pack(
        pady=10
    )


    # Enter để đăng nhập

    app.bind(
        "<Return>",
        lambda event: dang_nhap()
    )