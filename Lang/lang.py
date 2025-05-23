#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calcutator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calcutator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite"""

lang=input("Language: ")

if lang == "tr" or lang == "TR":
    error_dialog = "Geçersiz işlem!"
    welcome_msg = "LinuxUsersLinuxMint-Calculator 2.3 Programına hoşgeldiniz"
    process_list = "Seçenekler:"
    process_list_msg = "Seçmek istediğiniz komutu giriniz..."
    slctd_prcs = "Hiçbiri"
    command_calc_txt = "Girebileceğiniz işlemler:"
    slctd_prcs_msg = "Seçilen İşlem"
    usr_input = "calc> Seçmek istediğiniz işlemi veya işlemin numarasını giriniz: "
    usr_input_n1 = "calc> 1. sayiyi giriniz: "
    usr_input_n2 = "calc> 2. sayiyi giriniz: "
    process_input = "calc> Seçmek istediğiniz işlemi veya işlemin numarasını giriniz: "
    div_err = "Bölme işleminde sayı 0 olamaz!"
    thank = "LinuxUsersLinuxMint-Calcutator'u Kullandığınız için Teşekkür ederiz."
    licence_msg = "Bu Yazılım GPL2 lisansı kapsamında korunmaktadır."
    ver_msg = "Sürüm: 2.3 (Son Güncellenme Tarihi 29 Ocak , 2025 , 15:12)"
    add = "Toplama"
    ext = "Cıkarma"
    mul = "Carpma"
    div = "Bolme"
    per = "Yüzde hesaplama"
    mod = "Mod Alma"
elif lang == "en" or lang == "EN":
    error_dialog = "Invalid process!"
    welcome_msg = "Welcome to LinuxUsersLinuxMint-Calcutator 2.3 Program"
    process_list = "Options:"
    process_list_msg = "Enter the command you want to select..."
    slctd_prcs = "None"
    command_calc_txt = "Commands you can enter:"
    slctd_prcs_msg = "Selected Process"
    usr_input = "calc> Enter the process you want to select or its number: "
    usr_input_n1 = "calc> Enter the first number: "
    usr_input_n2 = "calc> Enter the second number: "
    process_input = "calc> Enter the process you want to select or its number: "
    div_err = "The division process cannot have a number of 0!"
    thank = "Thanks for using LinuxUsersLinuxMint-Calcutator!"
    licence_msg = "This Software is under the GPL2 license."
    ver_msg = "Version: 2.3 (Last Update Date 29 January , 2025 , 15:12)"
    add = "Addition"
    ext = "Extraction"
    mul = "Multiplication"
    div = "Division"
    per = "Percentage"
    mod = "Mod"
else:
    print("Invalid Language!")