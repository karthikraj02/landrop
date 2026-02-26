@echo off
call lan_env\Scripts\activate
start "Receiver" python receiver.py
start "Discovery" python discovery_server.py
start "GUI" python main.py
echo LANdrop Premium Fully Started!
pause
