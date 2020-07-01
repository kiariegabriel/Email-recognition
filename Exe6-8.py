count1=0
count2=0
num=eval(input('Enter the number of emails: '))
for i in range(num):
	email=input('Enter an email: \n')
	if email[-16:-12]=='prof':
		count1=1
	elif email[-16:-12]=='dent':
		count2=1
if count1==1 and count2==1:
	print('There\'re professors and students emails')
elif count1==1 and count2==0:
	print('Only professors emails')
elif count1==0 and count2==1:
	print('Only students email')