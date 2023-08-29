### **Pre-Requisites:**

>### *If You are using Windows OS*
   Make sure you have installed **[Python 3.10 or Newer](https://www.python.org/downloads/release/python-3100/)** installed on your machine.

   Open **CMD** or **Windows Power Shell** as administrator in the Project-Friday-on-Python directory or wherever you've stored the cloned files of this repo, Type `pip install -r pre-requisites.txt` and it will install all the required packages to run FRIDAY. 
   
>### *If you are using Linux OS*
   Open your Terminal in the directory where you've stored the cloned files of this repo and type following commands:
   1. `sudo apt update` 
   2. `sudo apt-get install python3 python3-pip`
   3. `sudo pip3 install -r pre-requisites.txt`

### **Configurations for `.env` file:**

1. Open `.env` file with your desired editor and enter your details in place of `<INPUT>`
2. Save the `.env` file 
3. **NOTE:** You don't have to edit any api keys stored in the `.env` file until you are a dev and want to input your own api keys 

### **Configuration of your email account to use send email function:**

#### *If you're using Gmail as your email provider.*

1. If you have enabled 2FA authentication for your email account you must set an app password for your account in order to login with **FRIDAY**
2. After setting app password for your account, you must paste your app password in place of `<INPUT>` under the `PASSWORD` in the `.env` file
3. If you don't have 2FA enabled for your account, You must ignore above 2 steps and proceed as usual by entering your normal password in place of `<INPUT>`
 
**Guide to How to set an app password for your Gmail account: https://support.google.com/accounts/answer/185833**
> **NOTE:** If you're using any other email providers, you might have to hop on google and run some searches to set app password if you have 2FA enabled in your account  

### **Configuration of paths to your programs in your PC you want to open with FRIDAY:**

1. Open `paths.py` file with your desirable editor and paste paths of the program in place of `<PATH>`
2. > **NOTE:** Remember to use `\\` instead of `\` while entering path. 


### **For any kind of bugs and suggestions to improve **FRIDAY**, Please let us know in [Issues](https://github.com/realdarkstar/Project-Friday-on-Python/issues)**.
### **Also, Since FRIDAY is in it's early stage the functions you can implement with FRIDAY is limited. If you have any Ideas about adding more functions in FRIDAY then please do let us know in [Issues](https://github.com/realdarkstar/Project-Friday-on-Python/issues).**

### **If you're a DEV and you appreciate what we've made then feel free to contribute.**

