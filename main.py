import serial
import time
import asyncio

import tracemalloc

tracemalloc.start()

import PySimpleGUI as sg

def pisca(ledID, sleep):
   ser.write(str(ledID).encode())
   time.sleep(sleep)
   ser.write(str(ledID).encode())
   
async def puxaPisca(ledID):
    await pisca(ledID)

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

sg.theme('DarkBrown4')  
layout = [  [sg.Text('Light Controller')],
            [sg.Button('RESET', key='reset',  size=(10, 5)),],
            [sg.Text('SWITCHS')],
            [
                sg.Button('Switch 1', key='s1', size=(10, 5)),
                sg.Button('Switch 2', key='s2',  size=(10, 5)),
                sg.Button('Switch 3', key='s3',  size=(10, 5)),
                sg.Button('Switch 4', key='s4',  size=(10, 5)),
            ],
            [sg.Text('Button')],
            [
                sg.Button('Button 1', key='b1', size=(10, 5)),
                sg.Button('Button 2', key='b2',  size=(10, 5)),
                sg.Button('Button 3', key='b3',  size=(10, 5)),
                sg.Button('Button 4', key='b4',  size=(10, 5)),
            ],
            [
                sg.Button('Button 1', key='b5', size=(10, 5)),
                sg.Button('Button 2', key='b6',  size=(10, 5)),
                sg.Button('Button 3', key='b7',  size=(10, 5)),
                sg.Button('Button 4', key='b8',  size=(10, 5)),
            ],
            
]


window = sg.Window('Light Controller', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'reset':
        ser.write('5'.encode())


    
    if event == sg.WIN_CLOSED or event == 's1':
        ser.write('1'.encode())
        
    if event == sg.WIN_CLOSED or event == 's2':
        ser.write('2'.encode())

    if event == sg.WIN_CLOSED or event == 's3':
        ser.write('3'.encode())
    
    if event == sg.WIN_CLOSED or event == 's4':
        ser.write('4'.encode())



    if event == sg.WIN_CLOSED or event == 'b1':
        pisca(1, 0.08)
        
    if event == sg.WIN_CLOSED or event == 'b2':
        pisca(2, 0.08)

    if event == sg.WIN_CLOSED or event == 'b3':
        pisca(3, 0.08)
    
    if event == sg.WIN_CLOSED or event == 'b4':
        pisca(4, 0.08)


    if event == sg.WIN_CLOSED or event == 'b5':
        pisca(1, 0.04)
        
    if event == sg.WIN_CLOSED or event == 'b6':
        pisca(2, 0.04)

    if event == sg.WIN_CLOSED or event == 'b7':
        pisca(3, 0.04)
    
    if event == sg.WIN_CLOSED or event == 'b8':
        pisca(4, 0.04)

window.close()

