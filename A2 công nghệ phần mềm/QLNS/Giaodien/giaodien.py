import customtkinter as ctk

from data import thong_ke, lay_nhan_vien


# ================= XÓA NỘI DUNG CŨ =================

def xoa_noi_dung(content):

    for widget in content.winfo_children():

        widget.destroy()


# ================= TẠO CARD =================

def tao_card(parent, icon, tieu_de, gia_tri):

    card = ctk.CTkFrame(
        parent,
        corner_radius=15
    )

    card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=8
    )


    icon_label = ctk.CTkLabel(
        card,
        text=icon,
        font=("Arial", 28)
    )

    icon_label.pack(
        anchor="w",
        padx=20,
        pady=(15, 0)
    )


    title = ctk.CTkLabel(
        card,
        text=tieu_de,
        font=("Arial", 14)
    )

    title.pack(
        anchor="w",
        padx=20
    )


    value = ctk.CTkLabel(
        card,
        text=str(gia_tri),
        font=("Arial", 26, "bold")
    )

    value.pack(
        anchor="w",
        padx=20,
        pady=(5, 15)
    )


# ================= DASHBOARD =================

def hien_dashboard(content):

    xoa_noi_dung(content)


    # Lấy thống kê

    tong_nv, tong_pb, tong_cv, tong_luong = thong_ke()


    # ================= TIÊU ĐỀ =================

    title = ctk.CTkLabel(
        content,
        text="Dashboard",
        font=("Arial", 30, "bold")
    )

    title.pack(
        anchor="w",
        padx=30,
        pady=(30, 5)
    )


    subtitle = ctk.CTkLabel(
        content,
        text="Tổng quan hệ thống quản lý nhân sự",
        font=("Arial", 15)
    )

    subtitle.pack(
        anchor="w",
        padx=30
    )


    # ================= CARD =================

    card_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    card_frame.pack(
        fill="x",
        padx=22,
        pady=25
    )


    tao_card(
        card_frame,
        "👥",
        "Tổng nhân viên",
        tong_nv
    )


    tao_card(
        card_frame,
        "🏢",
        "Phòng ban",
        tong_pb
    )


    tao_card(
        card_frame,
        "💼",
        "Chức vụ",
        tong_cv
    )


    tao_card(
        card_frame,
        "💰",
        "Tổng quỹ lương",
        f"{tong_luong:,.0f} VNĐ"
    )


    # ================= NHÂN VIÊN MỚI =================

    recent_frame = ctk.CTkFrame(
        content,
        corner_radius=15
    )

    recent_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 30)
    )


    recent_title = ctk.CTkLabel(
        recent_frame,
        text="👥 Danh sách nhân viên",
        font=("Arial", 20, "bold")
    )

    recent_title.pack(
        anchor="w",
        padx=25,
        pady=20
    )


    danh_sach = lay_nhan_vien()


    if len(danh_sach) == 0:

        empty = ctk.CTkLabel(
            recent_frame,
            text="Chưa có nhân viên nào",
            font=("Arial", 16)
        )

        empty.pack(
            pady=50
        )

    else:

        # Chỉ hiện 8 nhân viên

        danh_sach = danh_sach[:8]


        for nv in danh_sach:

            frame_nv = ctk.CTkFrame(
                recent_frame,
                height=45
            )

            frame_nv.pack(
                fill="x",
                padx=20,
                pady=4
            )


            text = (
                f"👤  {nv[1]}"
                f"     |     {nv[3]}"
                f"     |     {nv[4]}"
            )


            label = ctk.CTkLabel(
                frame_nv,
                text=text,
                font=("Arial", 14)
            )

            label.pack(
                side="left",
                padx=15,
                pady=10
            )