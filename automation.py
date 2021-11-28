import webbrowser
print("1.Youtube\n2.Google\n3.Sololearn")
user_option=int(input("Enter your option: "))
if user_option == 1:
    webbrowser.open("http://youtube.com", new=1)
elif user_option ==2:
    webbrowser.open("https://google.com",new=1)
elif user_option==3:
     webbrowser.open("https://apkdone.com/sololearn-apk/download#google_vignette",new=1)