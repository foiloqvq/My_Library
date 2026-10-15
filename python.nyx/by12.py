#user_weight =  float( input("请输入您的体重 （单位: kg) : "))
#user_height = float(input("请输入您的身高 （单位: m) : "))
#user_BMI = user_weight / float(user_height) **2
#print("您的BMI值为："+str(user_BMI))
from warnings import catch_warnings


def calculate_BMI(height,weight):
    BMI =weight/(height*height)
    if BMI <= 18.5:
        category = "On the tihn side"
    elif BMI <= 25:
        category = "normal"
    elif  BMI <=30 :
        category = "Slightly overweight"
    else:
        category = "obesity"
    print(f"your BMI is{category}")
    return BMI
foillo = calculate_BMI(20,20)
print(foillo)

