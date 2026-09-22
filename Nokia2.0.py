phone = True

while phone == True:
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
            phone_book_loop = True
            while phone_book_loop:
                phone_book = input("""
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
                
                match phone_book:
                    case "9":
                        phone_book_options_loop = True
                        while phone_book_options_loop:
                            phone_book_options = input("""
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
                            
                            match phone_book_options:
                                case "99":
                                    break
                                    
                                case "0":
                                    phone_book_loop = False
                                   
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")
                        
                    case "99":
                        phone_book_loop = False
                    
                    case _:
                        print("HINT: 9")
                        
        case "2":
            messages_loop = True
            while messages_loop:
                messages = input("""
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
                """)
                
                match messages:
                    case "7":
                        message_settings_loop = True
                        while message_settings_loop:
                            message_settings = input("""
                            ================================
                            --------MESSAGE SETTINGS--------
                            ================================
                            1.  Set
                            2.  Common
                            ================================
                            """)
                            
                            match message_settings:
                                case "1":
                                    message_settings_set_loop = True
                                    while message_settings_set_loop:
                                        message_settings_set = input("""
                                        =================================
                                        ---------------SET---------------
                                        =================================
                                        1.  Message centre number
                                        2.  Message sent as
                                        3.  Message validity
                                        =================================
                                        """)
                                        
                                        match message_settings_set:
                                            case "99":
                                                message_settings_set_loop = False
                            
                                            case "0":             
                                                messages_loop = False
                                        
                                            case _:
                                                print("CANNOT NAVIGATE FURTHER")
                                        
                                case "2":
                                    message_settings_common_loop = True
                                    while message_settings_common_loop:
                                        message_settings_common = input("""
                                        =================================
                                        ------------COMMON---------------
                                        =================================
                                        1.  Delivery reports
                                        2.  Reply via same route
                                        3.  Character support
                                        =================================
                                        """)
                                        
                                        match message_settings_common:
                                            case "99":
                                                break
                            
                                            case "0":             
                                                print("EXITING................")
                                                messages_loop = False
                                            
                                            case _:
                                                print("CANNOT NAVIGATE FURTHER")
                                    
                                case "99":
                                    messages_settings_loop = False
                    
                                case "0":             
                                    print("EXITING................")
                                    messages_loop = False
                                
                                case _:
                                    print("HINTS: 1 and 2") 
                    
                    case "99":
                        messages_loop = False
                    
                            
                    case _:     
                        print("HINT: 7")             

        case "3":
            print("CANNOT NAVIGATE FURTHER")

        case "4":
            call_register_loop = True
            while call_register_loop:
                call_register = input("""
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
                """)

                match call_register:
                    case "5":
                        show_call_duration_loop = True
                        while show_call_duration_loop:
                            show_call_duration = input("""
                            ================================
                            -------SHOW CALL DURATION-------
                            ================================
                            1.  Last call duration
                            2.  All calls' duration
                            3.  Received calls' duration
                            4.  Dialled calls' duration
                            5.  Clear timers
                            ================================
                            """)

                            match show_call_duration:
                                case "99":
                                    break
                                
                                case "0":
                                    call_register_loop = False
                                
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")

                    case "6":
                        show_call_costs_loop = True
                        while show_call_costs_loop:
                            show_call_costs = input("""
                            ================================
                            ---------SHOW CALL COSTS--------
                            ================================
                            1.  Last call cost
                            2.  All calls' cost
                            3.  Clear counters
                            ================================
                            """)

                            match show_call_costs:
                                case "99":
                                    break
                                    
                                case "0":
                                    call_register_loop = False
                            
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")

                    case "7":
                        call_cost_settings_loop = True
                        while call_cost_settings_loop:
                            call_cost_settings = input("""
                            ================================
                            --------CALL COST SETTINGS------
                            ================================
                            1.  Call cost limit
                            2.  Show costs in
                            ================================
                            """)

                            match call_cost_settings:
                                case "99":
                                    break
                                    
                                case "0":
                                    call_register_loop = False
                            
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")

                    case "99":
                        break

                    case _:
                        print("HINTS: 5, 6 and 7")

        case "5":
            tones_loop = True
            while tones_loop:
                tones = input("""
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
                """)

                match tones:
                    case "99":
                        break
                    
                    case _:
                        print("CANNOT NAVIGATE FURTHER")

        case "6":
            settings_loop = True
            while settings_loop:
                settings = input("""
                =================================
                ------------SETTINGS-------------
                =================================
                1.  Call settings
                2.  Phone settings
                3.  Security settings
                4.  Restore factory settings
                =================================
                """)

                match settings:
                    case "1":
                        call_settings_loop = True
                        while call_settings_loop:
                            call_settings = input("""
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
                            """)

                            match call_settings:
                                case "99":
                                    break
                            
                                case "0":
                                    settings_loop = False
                                
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")

                    case "2":
                        phone_settings_loop = True
                        while phone_settings_loop:
                            phone_settings = input("""
                            ================================
                            ----------PHONE SETTINGS--------
                            ================================
                            1.  Language
                            2.  Cell info display
                            3.  Welcome note
                            4.  Network selection
                            5.  Confirm SIM service actions
                            ================================
                            """)

                            match phone_settings:
                                case "99":
                                    break
                                
                                case "0":
                                    settings_loop = False
                                
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")

                    case "3":
                        security_settings_loop = True
                        while security_settings_loop:
                            security_settings = input("""
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
                            """)

                            match security_settings:
                                case "99":
                                    break
                                
                                case "0":
                                    settings_loop = False
                                
                                case _:
                                    print("CANNOT NAVIGATE FURTHER")
                        
                    case "99":
                        break
                    
                    case _:
                        print("HINTS: 1, 2 and 3")

        case "7":
            print("CANNOT NAVIGATE FURTHER")

        case "8":
            music_loop = True
            while music_loop:
                music = input("""
                =================================
                -------------MUSIC---------------
                =================================
                1.  Music player
                2.  Radio
                3.  Recorder
                4.  Track list
                =================================
                """)

                match music:
                    case "99":
                        break
                    
                    case _:
                        print("CANNOT NAVIGATE FURTHER")

        case "9":
            print("CANNOT NAVIGATE FURTHER")

        case "10":
            print("CANNOT NAVIGATE FURTHER")

        case "11":
            print("CANNOT NAVIGATE FURTHER")

        case "12":
            clock_loop = True
            while clock_loop:
                clock = input("""
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
                """)

                match clock:
                    case "99":
                        break
                    
                    case _:
                        print("CANNOT NAVIGATE FURTHER")

        case "13":
            print("CANNOT NAVIGATE FURTHER")

        case "14":
            print("CANNOT NAVIGATE FURTHER")

        case "15":
            print("CANNOT NAVIGATE FURTHER")

        case "0":
            print("EXITING................")
            phone = False

        case _:
            print("Invalid choice")
