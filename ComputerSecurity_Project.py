import math
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import messagebox


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# modular inverse function
def modinv(a, m=26):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def Encryption(a, b, plaintext):
    cyphirtext = []
    i=0
    while(i < len(plaintext)):
        # if the index value is not space, do the calculation
        if plaintext[i]=='\n':
            i+=1
            continue
        elif plaintext[i] != ' ':
            x = letters.index(plaintext[i].upper()) # numerical valur of the letter
            y = ((a * x) + b) % 26
            cyphirtext.append(letters[y])  # after decrypt that letter, append it to the final string      
        else:
            cyphirtext.append(' ')
        i += 1

    # combain the letters in string variable
    final_cyphirtext = ''.join(cyphirtext)
    text4.insert('end', final_cyphirtext)
    #print(final_cyphirtext)

def Decryption(a, b, cyphertext):
    i=0
    plaintext = []
    while(i < len(cyphertext)):
        # if the index value is not space, do the calculation
        if cyphertext[i]=='\n':
            i+=1
            continue
        elif cyphertext[i] != ' ':
            inverse = modinv(a, 26)
            y = letters.index(cyphertext[i].upper())
            x =  inverse * (y - b) % 26
            plaintext.append(letters[x])        
        else:
            plaintext.append(' ')

        i += 1
    final_plaintext = ''.join(plaintext)
    #print(final_plaintext)
    text4.insert('1.0', final_plaintext)

def check():
    a = int(a_in.get())
    b = int(b_in.get())
    text = text1.get('1.0','end')
    text4.delete(1.0, tk.END)
    if math.gcd(a, 26) == 1:
        if(selected.get() == 'En'):
            #print(str(text))
            Encryption(a, b, str(text))
        else:
            Decryption(a, b, str(text))
        #break
    else:
        # Display a warning message dialog
        messagebox.showwarning("Warning", "Unvalid key values!")
    

# define a list of alphabet for reference, each index represent the letter number value
letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# create window
window = tk.Tk()
window.title("Affine Cipher")
# Set geometry(widthxheight)
window.geometry('850x630')

title = tk.Label(window, text = "Affine Cipher", background='#BFB6D9', foreground='white', font=("Helvetica", 20))#, width=500, height=)
title.config(width=200, height=3 )
title.pack()
#UI contains several sections
section1 = tk.LabelFrame(window, text='Keys')
section2 = tk.LabelFrame(window, text='Text')
section3 = tk.LabelFrame(window, text='Operation')

#Section1
field2 = tk.Label(section1, text='Enter key1 value: ', font=("Helvetica", 12),anchor=tk.W)
field2.pack()
a_in = tk.StringVar()
text2 = tk.Entry(section1, textvariable = a_in)
text2.pack()

field3 = tk.Label(section1, text='Enter key2 value: ', font=("Helvetica", 12),anchor=tk.W)
field3.pack()
b_in = tk.StringVar()
text3 = tk.Entry(section1, textvariable=b_in)
text3.pack(pady=10)

#Section2
field1 = tk.Label(section2, text='Enter the text ', font=("Helvetica", 14),anchor=tk.W)
field1.pack()
text1 = tk.Text(section2, height=3, width=80)
text1.pack(pady=10)

field4 = tk.Label(section2, text='The Result Text ', font=("Helvetica", 14),anchor=tk.W)
field4.pack()
text4 = tk.Text(section2, height=3, width=80)
text4.pack()

#Section3
selected = tk.StringVar()
r1 = tk.Radiobutton(section3, text='Encryption', value='En', variable=selected)
r2 = tk.Radiobutton(section3, text='Decryption', value='De', variable=selected)
selected.set('En')
r1.pack()
r2.pack(pady=10)

section2.pack(pady=10)
section1.pack(pady=10)
section3.pack(pady=10)

button = tk.Button(window, text='Do The Operation', width=20, command=check, background="#6488E5", foreground='white')
button.pack()

window.mainloop()

