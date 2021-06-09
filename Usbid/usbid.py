import usb.core

#Creating new log
def new_log():
    dev = usb.core.find(find_all=1)
    fname = input ('Enter new log name: ')
    log = open(fname, "w")
    for cfg in dev:
        if str(cfg.idProduct) != '1' and str(cfg.idProduct) != '2':
            log.write(str(hex(cfg.idVendor)) + ' : ' + str(hex(cfg.idProduct)) + '\n')
    log.close()
    print ('Saved in', fname)

#Logging of conected devices
def accept():
    dev = usb.core.find(find_all=1)
    acc = open("usblog.txt", "a")
    for cfg in dev:
        entry = str(hex(cfg.idVendor)) + ' : ' + str(hex(cfg.idProduct))
        with open("usblog.txt") as file:
            if str(cfg.idProduct) != '1' and str(cfg.idProduct) != '2' and entry not in map(str.strip, file):
                acc.write(str(hex(cfg.idVendor)) + ' : ' + str(hex(cfg.idProduct)) + '\n')
    acc.close()

#Demonstration of found devices in the terminal
def show():
    dev = usb.core.find(find_all=1)
    for cfg in dev:
        if str(cfg.idProduct) != '1' and str(cfg.idProduct) != '2':
            print ('Vendor ID:' + str(hex(cfg.idVendor)) + ' Device ID:' + str(hex(cfg.idProduct)) + '\n')

#Checking if the device is logged
def check():
    dev = usb.core.find(find_all=1)
    for cfg in dev:
        if str(cfg.idProduct) != '1' and str(cfg.idProduct) != '2':
            line = str(hex(cfg.idVendor)) + ' : ' + str(hex(cfg.idProduct))
            with open("usblog.txt") as file:
                if line not in map(str.strip, file):
                    print("No entry in the log:")
                    print ('Vendor ID:' + str(hex(cfg.idVendor)) + ' Device ID:' + str(hex(cfg.idProduct)) + '\n')
                else: print('Device ID:' + str(hex(cfg.idVendor)) + ' Device ID:' + str(hex(cfg.idProduct)) + " - OK" + '\n')

#Menu
working = True
while working:
    cmd = input(">>> ")
    if cmd == "new":
        new_log()
    elif cmd == "accept":
        accept()
    elif cmd == "show":
        show()
    elif cmd == "check":
        check()
    elif cmd == "quit":
        working = False
