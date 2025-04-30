#!/usr/bin/python3
import os
from colorama import Fore, init
from Basic_Maths import *
init(autoreset=True)
islem=int(0)
error_dialog = "Geçersiz İşlem/Komut!"
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calculator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calculator All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calculator
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calculator """
print("*********************************************************************")
print("*** LinuxUsersLinuxMint-Calculator 2.2 Programına Hoşgeldiniz   ***")
print("""*** Seçenekler:                                                   ***
***                                                               ***
*** Seçmek istediğiniz Komutu Giriniz...                          ***
***                                                               ***
*** 1. calc                                                       ***
*** 2. about                                                      ***                     
*** 3. exit                                                       ***                      
*** 4. help                                                       ***
*** 5. git-address                                                ***                              
*** 6. ver                                                        ***          
*** 7. licence                                                    ***                                  
*** 8. Thank                                                      ***                                    
*********************************************************************""")
command=str(input(Fore.LIGHTBLUE_EX +'calc> '))
os.system("clear")
about="Python Hesap Makinesi CLI(Komut Satırı Arayüzü) LICENCE=GPL2"
secilen_islem=str(Fore.LIGHTBLUE_EX+"None")
if command=="calc":
   print("""*** Girebileceğiniz işlemler:     ***
         Seçilen İşlem={0}""". format(secilen_islem))
   print("""
1.   Toplama
2.   Çıkarma
3.   Çarpma
4.   Bölme
5.   Yüzde alma""")
   islem=str(input('calc> Seçmek İstediğiniz İşlemin Numarasını Giriniz: '))
   secilen_islem=islem
   os.system("clear")
   print(Fore.LIGHTBLUE_EX+"""calc> Seçilen İşlem: 
         Seçilen İşlem={0}""". format(secilen_islem))
   sayi1=float(input('calc> 1. sayiyi giriniz: '))
   sayi2=float(input('calc> 2. sayiyi giriniz: '))
   os.system("clear")
if islem=="1": 
     Addition(sayi1,sayi2,"Sonuç: ")  
elif islem=="2":
     Extraction(sayi1,sayi2,"Sonuç: ")
elif islem=="3":
     Multiplication(sayi1,sayi2,"Sonuç: ")
elif islem=="4":
     Division(sayi1,sayi2,"Sonuç: ","Bölme işleminde sayılar 0 olamaz!")
elif islem=="5":
     Percentage(sayi1,sayi2,"Sonuç: ")
else:
     error_msg(error_dialog)
if command=="about":
     print(about)
elif command=="exit":
     exit_select = int(input('Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): '))
     exit_select = int(exit_select)
     if exit_select == 0:
          userTime = input('After how many seconds should the program be closed?: ')
          userTime = int(userTime)
          exit_program_dialog_time("Exit program...", userTime)
     elif exit_select == 1:
          userTime = input('After how many seconds should the program be closed?: ')
          userTime = int(userTime)
          exit_program_time(userTime)
     elif exit_select == 2:
          exit_program_dialog("Exit program...")
     elif exit_select == 3:
          exit()
     else:
          error_msg(error_dialog)
elif command=="help":
     print("LinuxUsersLinuxMint-Calculator Help")
     print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence , Thank")
elif command=="git-address":
     print("Github Link: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calculator")
elif command=="web-site":
     print("linuxuserslinuxmint.github.io")
elif command=="ver":
     print("Sürüm: 2.2 (Son Güncellenme Tarihi 29 Ocak , 2025 , 15:12)")
elif command=="licence":
     print("Bu Yazılım GPL2 lisansı kapsamında korunmaktadır.")
elif command=="Thank":
     print("LinuxUsersLinuxMint-Calculator'u Kullandığınız için Teşekkür ederim. ")
else:
     error_msg(error_dialog)
