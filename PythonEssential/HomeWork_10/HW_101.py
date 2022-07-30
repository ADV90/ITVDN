import PythonEssential.HomeWork_10.app.user_interface_1 as ui1
import PythonEssential.HomeWork_10.app.user_interface_2 as ui2

if __name__ == '__main__':
    iface = input('Choose user interface:\n1 - numbers\n2 - letters\n>>> ')
    if iface == '1':
        ui1.main()
    elif iface == '2':
        ui2.run()
    else:
        print('Incorrect choice')
