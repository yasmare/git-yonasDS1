weight = input('please enter your Weight \n', )
print('your weigt is  '+str(weight)+'\n')
height = input('please enter your Height \n', )
print('your Heigt is  '+str(height)+'\n')
w=float(weight)
h=float(height)
bmi = w/(h*h)
print ('your BMI is  '+str(bmi)+'\n')

if(bmi <= 18):
    print('you are Under weight')
elif(18 < bmi < 25):
    print('you are normal')
else:
    print('you are over weight') 
print('you can rerun the code if you want.') 