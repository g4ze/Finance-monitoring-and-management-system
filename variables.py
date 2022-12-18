expenseList=['electricitybill','internet','rent','entertainment','groceries and food','fuel','investment','education','donation','other']
aro='---------------PLEASE WAIT WHILE I PROCESS THE TASK--------------'
div1='================================================================================================'
div2='------------------------------------------------------------------------------------------------'
import time
def animation1():
    animation = "|/-\\"
    idx = 0
    i=1
    while True:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        i+=1
        if i == 10*10:
            break
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]
def animation2():
    i=1
    while True:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
        if i == 7*10:
            break
