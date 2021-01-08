student_name='Jeffrey Dier'
import csv
sum_cty=0
n=0
sum_hwy=0
sum_ford_hwy=0
n_ford_hwy=0
sum_suv_city=0
n_suv_city=0
firstLine=True
with open('mpg.csv','r') as file:
    for line in file:
        if firstLine:
            firstLine=False
        else:
            data=line.split(',')
            sum_cty+=int(data[8])
            sum_hwy+=int(data[9])
            n=n+1
            if data[1].lower()=='ford':
                sum_ford_hwy+=int(data[9])
                n_ford_hwy+=1
            if data[-1].strip().lower()=='suv':
                sum_suv_city+=int(data[8])
                n_suv_city+=1
avg_city=sum_cty/n
avg_hwy=sum_hwy/n
ford_hwy=sum_ford_hwy/n_ford_hwy
suv_city=sum_suv_city/n_suv_city
print("The avg city milage is" + str(avg_city))
print("The avg highway milage is" + str(avg_hwy))
print("The avg ford milage is" + str(ford_hwy))
print("The avg suv milage is" + str(suv_city))
with open('jdier3_assignment4.txt', 'w') as out_file:
    out_file.write("The average city milage is \n" + str(avg_city))
    out_file.write("The average highway milage is \n" + str(avg_hwy))
    out_file.write("The average ford milage is \n" + str(ford_hwy))
    out_file.write("The average suv milage is \n" + str(suv_city))
    file.close()