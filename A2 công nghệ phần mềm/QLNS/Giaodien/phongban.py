import customtkinter as ctk

from data import lay_phong_ban


# ================= XÓA NỘI DUNG =================

def xoa_noi_dung(content):

    for widget in content.winfo_children():

        widget.destroy()


# ================= PHÒNG BAN =================

def hien_phong_ban(content):

    xoa_noi_dung(content)


    # Tiêu đề

    title = ctk.CTkLabel(
        content,
        text="Quản lý phòng ban",
        font=("Arial", 28, "bold")
    )

    title.pack(
        anchor="w",
        padx=30,
        pady=(30, 5)
    )


    subtitle = ctk.CTkLabel(
        content,
        text="Danh sách các phòng ban trong công ty",
        font=("Arial", 15)
    )

    subtitle.pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )


    # Khung chính

    main_frame = ctk.CTkFrame(
        content,
        corner_radius=15
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )


    danh_sach = lay_phong_ban()


    if len(danh_sach) == 0:

        label = ctk.CTkLabel(
            main_frame,
            text="Chưa có phòng ban nào",
            font=("Arial", 18)
        )

        label.pack(
            pady=80
        )


    else:

        for index, pb in enumerate(danh_sach):

            frame = ctk.CTkFrame(
                main_frame,
                height=55
            )

            frame.pack(
                fill="x",
                padx=20,
                pady=6
            )


            text = (
                f"🏢  {index + 1}. {pb[0]}"
            )


            label = ctk.CTkLabel(
                frame,
                text=text,
                font=("Arial", 17)
            )

            label.pack(
                side="left",
                padx=20,
                pady=12
            )