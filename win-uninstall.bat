@echo off
@title=LinuxUsersLinuxMint-Calculator Uninstall
:m
cls
echo LinuxUsersLinuxMint-Calculatorr Uninstall
echo Are you sure you want to uninstall LinuxUsersLinuxMint-Calculator?
echo Yes (1)
echo No (2)
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==1 goto one
if %input%==2 goto two
goto m
:one
echo LinuxUsersLinuxMint-Calculator Uninstall.
pause
del C:\Users\%users%\calc
pause
exit
goto m
:two
echo LinuxUsersLinuxMint-Calculator removal has been cancelled.
pause
exit