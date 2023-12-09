#coding:utf-8

def modify_string(chenn_karakte):
    n = len(chenn_karakte)
    nouvo_chenn = ""

    i = 0
    while i < n:
        k = 1
        while i + k < n and chenn_karakte[i] == chenn_karakte[i + k]:
            k += 1

        if k >= 3:
            nouvo_chenn += chenn_karakte[i]  
            i += k  
        else:
            nouvo_chenn += chenn_karakte[i] 
            i += 1  

    return nouvo_chenn

antreUser = input("Tanpri antre yon chen karakte: ")

rezilta = modify_string(antre_chenn)


print("Chen karakte modifye se:", rezilta)