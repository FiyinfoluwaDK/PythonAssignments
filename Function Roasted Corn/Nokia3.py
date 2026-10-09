def phone_book_menu():
    while True:
        choice = input("""
    ====================================
    -----------PHONE BOOK---------------
    ====================================
    1.  Search
    2.  Service Nos.
    3.  Add Name
    4.  Erase
    5.  Edit
    6.  Copy
    7.  Assign tone
    8.  Send business card
    9.  Options
    10. Speed dials
    11. Voice tags
    ====================================
    -------TYPE 99 TO GO BACK-----------
    ====================================
    """)
        match choice:
            case "9":
                res = phone_book_options()
                if res == "EXIT":
                    return "EXIT"
            case "99":
                break
            case _:
                print("HINT: 9")



def phone_book_options():
    while True:
        choice = input("""
    ==================================
    -------------OPTIONS--------------
    ==================================
    1.  Memory in use
    2.  Type of view
    3.  Memory status
    ====================================
    -------TYPE 99 TO GO BACK-----------
    ====================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")




def message_settings_set():
    while True:
        choice = input("""
    =================================
    ---------------SET---------------
    =================================
    1.  Message centre number
    2.  Message sent as
    3.  Message validity
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def message_settings_common():
    while True:
        choice = input("""
    =================================
    ------------COMMON---------------
    =================================
    1.  Delivery reports
    2.  Reply via same route
    3.  Character support
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def message_settings_menu():
    while True:
        choice = input("""
    ================================
    --------MESSAGE SETTINGS--------
    ================================
    1.  Set
    2.  Common
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        match choice:
            case "1":
                res = message_settings_set()
                if res == "EXIT":
                    return "EXIT"
            case "2":
                res = message_settings_common()
                if res == "EXIT":
                    return "EXIT"
            case "99":
                break
            case "0":
                return "EXIT"
            case _:
                print("HINTS: 1 and 2")


def messages_menu():
    while True:
        choice = input("""
    =================================
    ------------MESSAGES-------------
    =================================
    1.  Write messages
    2.  Inbox
    3.  Outbox
    4.  Picture messages
    5.  Templates
    6.  Smileys
    7.  Message settings
    8.  Info service
    9.  Voice mailbox number
    10. Service command editor
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        match choice:
            case "7":
                res = message_settings_menu()
                if res == "EXIT":
                    return "EXIT"
            case "99":
                break
            case _:
                print("HINT: 7")


def show_call_duration():
    while True:
        choice = input("""
    ================================
    -------SHOW CALL DURATION-------
    ================================
    1.  Last call duration
    2.  All calls' duration
    3.  Received calls' duration
    4.  Dialled calls' duration
    5.  Clear timers
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def show_call_costs():
    while True:
        choice = input("""
    ================================
    ---------SHOW CALL COSTS--------
    ================================
    1.  Last call cost
    2.  All calls' cost
    3.  Clear counters
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def call_cost_settings():
    while True:
        choice = input("""
    ================================
    --------CALL COST SETTINGS------
    ================================
    1.  Call cost limit
    2.  Show costs in
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def call_register_menu():
    while True:
        choice = input("""
    =================================
    ---------CALL REGISTER-----------
    =================================
    1.  Missed calls
    2.  Received calls
    3.  Dialled numbers
    4.  Erase recent call lists
    5.  Show call duration
    6.  Show call costs
    7.  Call cost settings
    8.  Prepaid credit
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        match choice:
            case "5":
                res = show_call_duration()
                if res == "EXIT":
                    return "EXIT"
            case "6":
                res = show_call_costs()
                if res == "EXIT":
                    return "EXIT"
            case "7":
                res = call_cost_settings()
                if res == "EXIT":
                    return "EXIT"
            case "99":
                break
            case _:
                print("HINTS: 5, 6 and 7")


def tones_menu():
    while True:
        choice = input("""
    =================================
    -------------TONES---------------
    =================================
    1.  Ringing tone
    2.  Ringing volume
    3.  Incoming call alert
    4.  Message alert tone
    5.  Keypad tones
    6.  Warning tones
    7.  Vibrating alert
    8.  Screen saver
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        if choice == "99":
            break
        else:
            print("CANNOT NAVIGATE FURTHER")


def call_settings():
    while True:
        choice = input("""
    ================================
    ----------CALL SETTINGS---------
    ================================
    1.  Automatic redial
    2.  Speed dialling
    3.  Call waiting options
    4.  Own number sending
    5.  Phone line in use
    6.  Automatic answer
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def phone_settings():
    while True:
        choice = input("""
    ================================
    ----------PHONE SETTINGS--------
    ================================
    1.  Language
    2.  Cell info display
    3.  Welcome note
    4.  Network selection
    5.  Confirm SIM service actions
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def security_settings():
    while True:
        choice = input("""
    ================================
    --------SECURITY SETTINGS-------
    ================================
    1.  PIN code request
    2.  Call barring service
    3.  Fixed dialling
    4.  Closed user group
    5.  Security level
    6.  Change access codes
    ================================
    -------TYPE 99 TO GO BACK-----------
    ================================
    """)
        if choice == "99":
            break
        elif choice == "0":
            return "EXIT"
        else:
            print("CANNOT NAVIGATE FURTHER")


def settings_menu():
    while True:
        choice = input("""
    =================================
    ------------SETTINGS-------------
    =================================
    1.  Call settings
    2.  Phone settings
    3.  Security settings
    4.  Restore factory settings
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        match choice:
            case "1":
                res = call_settings()
                if res == "EXIT":
                    return "EXIT"
            case "2":
                res = phone_settings()
                if res == "EXIT":
                    return "EXIT"
            case "3":
                res = security_settings()
                if res == "EXIT":
                    return "EXIT"
            case "99":
                break
            case _:
                print("HINTS: 1, 2 and 3")


def music_menu():
    while True:
        choice = input("""
    =================================
    -------------MUSIC---------------
    =================================
    1.  Music player
    2.  Radio
    3.  Recorder
    4.  Track list
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        if choice == "99":
            break
        else:
            print("CANNOT NAVIGATE FURTHER")


def clock_menu():
    while True:
        choice = input("""
    =================================
    -------------CLOCK---------------
    =================================
    1.  Alarm clock
    2.  Clock settings
    3.  Date settings
    4.  Stopwatch
    5.  Countdown timer
    6.  Auto update of date and time
    =================================
    -------TYPE 99 TO GO BACK-----------
    =================================
    """)
        if choice == "99":
            break
        else:
            print("CANNOT NAVIGATE FURTHER")


def run_nokia_phone():
    phone = True
    while phone:
        main_menu = input("""
    ===========================================
    ----------------NOKIA MENU-----------------
    ===========================================
    1.  Phone book
    2.  Messages
    3.  Chat
    4.  Call register
    5.  Tones
    6.  Settings
    7.  Call divert
    8.  Music
    9.  Games
    10. Calculator
    11. Reminders
    12. Clock
    13. Profiles
    14. Services
    15. SIM services
    ===========================================
    --------TYPE THE NUMBER TO NAVIGATE--------
    --------------TYPE 0 TO EXIT---------------
    ===========================================
    """)

        match main_menu:
            case "1":
                if phone_book_menu() == "EXIT":
                    phone = False
            case "2":
                if messages_menu() == "EXIT":
                    phone = False
            case "3":
                print("CANNOT NAVIGATE FURTHER")
            case "4":
                if call_register_menu() == "EXIT":
                    phone = False
            case "5":
                tones_menu()
            case "6":
                if settings_menu() == "EXIT":
                    phone = False
            case "7":
                print("CANNOT NAVIGATE FURTHER")
            case "8":
                music_menu()
            case "9" | "10" | "11":
                print("CANNOT NAVIGATE FURTHER")
            case "12":
                clock_menu()
            case "13" | "14" | "15":
                print("CANNOT NAVIGATE FURTHER")
            case "0":
                print("EXITING................")
                phone = False
            case _:
                print("Invalid choice")



run_nokia_phone()
