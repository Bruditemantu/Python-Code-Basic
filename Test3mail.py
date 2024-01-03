import smtplib


port=587
server= "smtp.gmail.com"
sender_mail="mantu.r.brudite@gmail.com"
sender_pass="pztuxjfmzusyozbw"
reciver_mail=["rahul.brudite@gmail.com","manturaj25122003@gmail.com","2020pcecsmantu105@poornima.org"]
reciver_mail_usingmap={{"name":"mantu", "email":"manturaj25122003@gmail.com"},
                       {"name":"mantupoornima", "email":"2020pcecsmantu105@poornima.org"},
                       {"name":"raja" ,"email":"mantuyadav00140013@gmail.com"}}


for reciver in reciver_mail:
    message="hello {get.name}"
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.starttls()
        smtp.login(sender_mail,sender_pass)
        smtp.sendmail(sender_mail,reciver,message)
    print(f"message send {reciver}")
    