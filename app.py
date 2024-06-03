# import modules
import cv2
import numpy as np
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
from lsb import LSB
from aes import AESCipher
import os


class IMG_Stegno:

    output_image_size = 0

    # main frame or start page
    def main(self, root):
        root.title('Image Steganography')
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        root.config(bg='#e3f4f1')
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text='Image Steganography')
        title.config(font=('Times new roman', 25, 'bold'))
        title.grid(pady=10)
        title.config(bg='#e3f4f1')
        title.grid(row=1)

        encode = Button(frame, text='Encode', command=lambda : self.encode_frame0(frame), padx=14, bg='#e3f4f1')
        encode.config(font=('Helvetica', 14), bg='#e8c1c7')
        encode.grid(row=2)
        decode = Button(frame, text='Decode', command=lambda : self.decode_frame0(frame), padx=14, bg='#e3f4f1')
        decode.config(font=('Helvetica', 14), bg='#e8c1c7')
        decode.grid(pady=12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        

    # back function to loop back to main screen
    def back(self, frame):
        frame.destroy()
        self.main(root)


    # choose LSB or AES+LSB for encoding
    def encode_frame0(self, F):
        F.destroy()
        F1 = Frame(root)
        label1 = Label(F1, text='Choose the desired\nencryption method:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()

        button_lsb = Button(F1, text='LSB', command=lambda : self.encode_frame1(F1))
        button_lsb.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_lsb.grid()
        button_aes = Button(F1, text='AES + LSB', command=lambda : self.encode_frame3(F1))
        button_aes.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_aes.grid(pady=15)
        button_aes.grid()
        F1.grid()


    # choose LSB or AES+LSB for decoding
    def decode_frame0(self, F):
        F.destroy()
        d_F1 = Frame(root)
        label1 = Label(d_F1, text='Choose the desired\ndecryption method:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()

        button_lsb = Button(d_F1, text='LSB', command=lambda : self.decode_frame1(d_F1))
        button_lsb.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_lsb.grid()
        button_aes = Button(d_F1, text='AES + LSB', command=lambda : self.decode_frame3(d_F1))
        button_aes.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_aes.grid(pady=15)
        button_aes.grid()
        d_F1.grid()


    # frame for encode page for LSB
    def encode_frame1(self, F):
        F.destroy()
        F2 = Frame(root)
        label1 = Label(F2, text='Select the image in which\nyou want to hide text:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()

        button_bws = Button(F2, text='Select', command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self, F2))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()


    # frame for encode page for AES + LSB
    def encode_frame3(self, F):
        F.destroy()
        F3 = Frame(root)
        label1 = Label(F3, text='Select the image in which\nyou want to hide text:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()

        button_bws = Button(F3, text='Select', command=lambda : self.encode_frame4(F3))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(F3, text='Cancel', command=lambda : IMG_Stegno.back(self, F3))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F3.grid()


    # function to encode image for AES + LSB
    def encode_frame4(self, e_F3):
        e_pg = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])

        if not myfile:
            messagebox.showerror('Error', 'You have selected nothing!')
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(new_image)
            label3 = Label(e_pg, text='Selected image')
            label3.config(font=('Helvetica', 14, 'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            (self.o_image_w, self.o_image_h) = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Secret message')
            label2.config(font=('Helvetica', 14, 'bold'))
            label2.grid(pady=15)
            message_input = Text(e_pg, width=50, height=6)
            message_input.grid()
            label3 = Label(e_pg, text='Key')
            label3.config(font=('Helvetica', 14, 'bold'))
            label3.grid(pady=15)
            key_input = Text(e_pg, width=50, height=2)
            key_input.grid()
            cancel_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self, e_pg))
            cancel_button.config(font=('Helvetica', 14), bg='#e8c1c7')
            message = message_input.get('1.0', 'end-1c')
            key = key_input.get('1.0', 'end-1c')
            encode_button = Button(e_pg, text='Encode', command=lambda : [self.encode_aeslsb(message_input, key_input, my_img, myfile), IMG_Stegno.back(self, e_pg)])

            encode_button.config(font=('Helvetica', 14), bg='#e8c1c7')
            encode_button.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F3.destroy()


    # create AESCipher object to encode message with inputed key as secret key
    def cipher(self, key_input):
        key = key_input.get('1.0', 'end-1c')
        if len(key) == 0:
            messagebox.showinfo('Alert', 'Kindly enter a 16 character key.')
        else:
            # key length must be 16 characters
            if len(key) != 16:
                messagebox.showwarning('Warning', 'Key must be 16 characters!')
                return
            return AESCipher(key)


    # encode message using AESCipher and embed cipher text to image
    def encode_aeslsb(self, message_input, key_input, myImg, path):
        message = message_input.get('1.0', 'end-1c')
        if len(message) == 0:
            messagebox.showinfo('Alert', 'Kindly enter text in textbox.')
        else:
            newImg = myImg.copy()
            # message length will be forced to be a multiple of 16 by adding extra whitespaces at the end
            if len(message) % 16 != 0:
                message += ' ' * (16 - len(message) % 16)
            cipher = self.cipher(key_input)
            if cipher == None:
                return
            cipherText = cipher.encrypt(message)
            obj = LSB(cv2.imread(path))
            obj.embed(cipherText)
            message_input.delete(1.0, tkinter.END)
            key_input.delete(1.0, tkinter.END)
            temp = os.path.splitext(os.path.basename(myImg.filename))[0]
            obj.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')], defaultextension='.png'))
            self.image = obj.image
            messagebox.showinfo('Success', 'Encoded successfully')


    # function to encode image
    def encode_frame2(self, e_F2):
        e_pg = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])

        if not myfile:
            messagebox.showerror('Error', 'You have selected nothing!')
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(new_image)
            label3 = Label(e_pg, text='Selected image')
            label3.config(font=('Helvetica', 14, 'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            (self.o_image_w, self.o_image_h) = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Secret message')
            label2.config(font=('Helvetica', 14, 'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self, e_pg))
            encode_button.config(font=('Helvetica', 14), bg='#e8c1c7')
            data = text_a.get('1.0', 'end-1c')
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a, my_img), IMG_Stegno.back(self, e_pg)])

            button_back.config(font=('Helvetica', 14), bg='#e8c1c7')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()


    # frame for decode page
    def decode_frame1(self, F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select image with hidden text:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()
        label1.config(bg='#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda : self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self, d_f2))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()


    # function to decode image
    def decode_frame2(self, d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])

        if not myfiles:
            messagebox.showerror('Error', 'You have selected nothing!')
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4 = Label(d_F3, text='Selected image:')
            label4.config(font=('Helvetica', 14, 'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Secret message')
            label2.config(font=('Helvetica', 14, 'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command=lambda : self.frame_3(d_F3))
            button_back.config(font=('Helvetica', 14), bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()


    # frame for decode page for AES + LSB
    def decode_frame3(self, F):
        F.destroy()
        d_F3 = Frame(root)
        label1 = Label(d_F3, text='Select image with hidden text:')
        label1.config(font=('Times new roman', 25, 'bold'), bg='#e3f4f1')
        label1.grid()

        button_bws = Button(d_F3, text='Select', command=lambda : self.decode_frame4(d_F3))
        button_bws.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_F3, text='Cancel', command=lambda : IMG_Stegno.back(self, d_F3))
        button_back.config(font=('Helvetica', 18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_F3.grid()


    # function to decode image for AES + LSB
    def decode_frame4(self, dec_F3):
        e_pg = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])

        if not myfile:
            messagebox.showerror('Error', 'You have selected nothing!')
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(new_image)
            label3 = Label(e_pg, text='Selected image')
            label3.config(font=('Helvetica', 14, 'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            (self.o_image_w, self.o_image_h) = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Secret message')
            label2.config(font=('Helvetica', 14, 'bold'))
            label2.grid(pady=15)
            message_input = Text(e_pg, width=50, height=6)
            message_input.grid()
            label3 = Label(e_pg, text='Key')
            label3.config(font=('Helvetica', 14, 'bold'))
            label3.grid(pady=15)
            key_input = Text(e_pg, width=50, height=2)
            key_input.grid()
            cancel_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self, e_pg))
            cancel_button.config(font=('Helvetica', 14), bg='#e8c1c7')
            message = message_input.get('1.0', 'end-1c')
            key = key_input.get('1.0', 'end-1c')
            decode_button = Button(e_pg, text='Decode', command=lambda : self.decode_aeslsb(key_input, message_input, myfile))
            decode_button.config(font=('Helvetica', 14), bg='#e8c1c7')
            decode_button.grid(pady=15)
            decode_button.grid()
            button_back = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self, e_pg))
            button_back.config(font=('Helvetica', 14), bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            e_pg.grid(row=1)
            dec_F3.destroy()


    # decode cipher text from image and try to decrypt it using provided secret key
    def decode_aeslsb(self, key_input, message_input, path):
        cipher = self.cipher(key_input)
        if cipher == None:
            return
        obj = LSB(cv2.imread(path))
        cipherText = obj.extract()
        msg = cipher.decrypt(cipherText)
    # show decoded secret message in message input box
        message_input.delete(1.0, tkinter.END)
        message_input.insert(tkinter.INSERT, msg)


    # function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while True:
            pixels = [value for value in image_data.__next__()[:3] + image_data.__next__()[:3] + image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data


    # function to generate data
    def generate_Data(self, data):
        new_data = []
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    # function to modify the pixels of image
    def modify_Pix(self, pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] + imgData.__next__()[:3] + imgData.__next__()[:3]]

            for j in range(0, 8):
                if dataList[i][j] == '0' and pix[j] % 2 != 0:
                    if pix[j] % 2 != 0:
                        pix[j] -= 1
                elif dataList[i][j] == '1' and pix[j] % 2 == 0:
                    pix[j] -= 1

            if i == dataLen - 1:
                if pix[-1] % 2 == 0:
                    pix[-1] -= 1
            else:
                if pix[-1] % 2 != 0:
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]


    # function to enter the data pixels in image
    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):
            # putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if x == w - 1:
                x = 0
                y += 1
            else:
                x += 1


    # function to enter hidden text
    def enc_fun(self, text_a, myImg):
        data = text_a.get('1.0', 'end-1c')
        if len(data) == 0:
            messagebox.showinfo('Alert', 'Kindly enter text in textbox.')
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')], defaultextension='.png'))
            self.d_image_size = my_file.tell()
            (self.d_image_w, self.d_image_h) = newImg.size
            messagebox.showinfo('Success', 'Encoded successfully')


    def frame_3(self, frame):
        frame.destroy()
        self.main(root)

# GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()

