def generate_qrcode():
    import qrcode
    img = qrcode.make(input("Admission Number: "))
    file_name = input("File Name: ")
    img.save(f"""C:\\Coding\\Attendance System\\qr\\{file_name}.jpg""")
    # img.show(f"""C:\\Coding\\Attendance System\\{file_name}.jpg""")
    print("QR Code Sucessfully Generated")

if __name__ == '__main__':
        generate_qrcode()