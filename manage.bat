@echo off
if NOT "%1"=="" goto %1
:beggining
cls
echo.
echo 	Accepted commands:
echo. 
echo 	c	cycle (run many iterations)
echo 	d	debug (run one iteration)
echo 	g	generate Facebook SDK layer
echo 	r	remove all posts
echo 	tc	show current token
echo 	td	delete token from list
echo 	tr	register (new) token in list
echo 	ts	select token from list
echo 	z	zip files to aws lambda
echo.

set /p i=" >>> "
goto %i%

:c
echo.
set /p iterations=" #iterations = "
if %iterations% EQU 1 goto d
if %iterations% EQU 0 goto beggining
if %iterations% LSS 0 (
echo.
echo Invalid!
echo.
goto hold
)
echo.
echo from fibonacci import FibonacciBot>cycle.py
echo for i in range(%iterations%):>>cycle.py
echo 	print("Iteration #{} ---------------------".format(i+1))>>cycle.py
echo 	FibonacciBot(0,0)>>cycle.py
echo print("\nDone iterating %iterations% posts!\n")>>cycle.py
python cycle.py
del cycle.py
goto hold

:d
python -c "from fibonacci import FibonacciBot; FibonacciBot(0,0)"
goto hold

:g
if exist .\python rd /s /q .\python
if exist facebook-sdk-layer.zip del facebook-sdk-layer.zip
pip install facebook-sdk --target .\python
7z a -r -sdel facebook-sdk-layer.zip .\python
goto hold

:tc
:td
:tr
:ts
echo from tokenManager import launch>tkmng.py
echo launch("%i%")>>tkmng.py
python tkmng.py
del tkmng.py
goto hold

:r
python remove.py
goto hold

:z
if exist lambda.zip del lambda.zip
7z a -y lambda.zip fibonacci.py tokens.tk
goto hold

:hold
if exist .\__pycache__ rd /s /q .\__pycache__
pause
cls
goto beggining