import pyautogui
import time

def find_alterac():
    time.sleep(5)
    pyautogui.press('h')
    time.sleep(3)
    pyautogui.moveTo(207, 521)
    pyautogui.click()

#=====================================================================================

def accept_alterac():
    while True:
        acceptAlterac = pyautogui.locateOnScreen('acceptAlterac.png', confidence=0.4)
        if acceptAlterac:
            print('Alterac encontrada!!')
            pyautogui.moveTo(605, 193)
            pyautogui.click()
            break
        else:
            print('Buscando Alterac...')
            time.sleep(3)
            pass

#=====================================================================================
def leave_alterac():
    while True:
        leaveAlterac = pyautogui.locateOnScreen('leaveBG.png', confidence=0.4)
        if leaveAlterac:
            print('Alterac Finalizada!!')
            pyautogui.moveTo(684, 553)
            pyautogui.click()
            break
        else:
            print('Alterac em andamento...')
            time.sleep(3)
            pass



print(" ================ Iniciando Macro ================ ")
time.sleep(10)
i = 1
while i < 100:
    print('Buscando Alterac '+str(i)+' de 100')
    find_alterac()
    accept_alterac()
    leave_alterac()
    time.sleep(20)
    i = i + 1
