while True:
    print('------------------------------')
    print("ĐĂNG KÍ")
    print()
    HOTEN = SĐT = EMAIL = TENDN = MK = []
    hoten = str(input('Họ và tên: '))
    sđt = input('Số điện thoại: ')
    email = str(input('Email: '))
    tendangnhap = input('Tên đăng nhập: ')
    matkhau = input('Mật khẩu: ')
    xacnhanMK = input('Xác nhận mật khẩu: ')
    print()
    print('------------------------------')
    if matkhau == xacnhanMK and len(sđt)==10 and sđt.isnumeric() :
        HOTEN = HOTEN + [hoten]
        SĐT = SĐT + [sđt]
        EMAIL = EMAIL + [email]
        TENDN = TENDN + [tendangnhap]
        MK = MK + [matkhau]
        print('<Gửi mã xác thực/OTP]>')
        while True:
            maOTP = ''
            for i in range(0, 6):
                import random
                so = random.randint(0, 9)
                maOTP += str(so)
            print('[Mã OTP của bạn là:'+ maOTP +']')
            print('------------------------------')
            print()
            print("Nhập mã xác thực/OTP")
            xacthucOTP=str(input())
            print()
            print('------------------------------')
            if xacthucOTP != maOTP:
                print('Mã xác thực không đúng')
                print('<Gửi lại mã>')
                continue
            else:
                break
        print('[Đăng kí thành công!]')
        break
    else:
        print('[Không hợp lệ]')


while True:
    print('------------------------------')
    print('ĐĂNG NHẬP')
    print()
    tendangnhap = input('Tên đăng nhập' + '\n')
    matkhau = input('Nhập mật khẩu' + '\n')
    print()
    print('------------------------------')
    for i in (TENDN):
        if i == tendangnhap:
            for j in (MK):
                if j == matkhau:
                    print('[Đăng nhập thành công!]')
                    y=True
                    break
                else:
                    print('[Mật khẩu đăng nhập sai]')
                    y=False
                    break
        elif i!= tendangnhap:
            print('[Tên đăng nhập không hợp lệ]')
            y=False
            break
    if y == False:
        continue
    else:
        break


while True:
    print('------------------------------')
    print('Thiết lập mã PIN mở khoá?')
    traloi = input()
    print()
    if traloi == 'có' or traloi == 'Có':
        while True:
            maPIN1 = str(input('Vui lòng nhập mã PIN (6 chữ số)' + '\n'))
            if maPIN1.isnumeric() and len(maPIN1) == 6:
                while True:
                    maPIN2 = str(input('Nhập lại mã PIN' + '\n'))
                    print()
                    print('------------------------------')
                    if maPIN1 == maPIN2:
                        print('[Tạo mã PIN mở khoá thành công!]')
                        print('------------------------------')
                        print()
                        while True:
                            nhapPIN = str(input('Nhập mã PIN mở khoá'+'\n'))
                            print()
                            print('------------------------------')
                            if nhapPIN == maPIN1:
                                print('[Mở khoá thành công!]')
                                print('------------------------------')
                                break
                            else:
                                print('[Mã PIN không đúng]')
                                print('------------------------------')
                        break
                    else:
                        print('[Mã PIN không khớp]')
                        print('------------------------------')
                break

        break
    else:
        break






