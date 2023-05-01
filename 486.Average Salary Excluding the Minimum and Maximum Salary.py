# Average Salary Excluding the Minimum and Maximum Salary

salary = [4000,3000,1000,2000]

def average(salary):
    salMax = float("-inf")
    salMin = float("inf")
    ans = 0
    for sal in salary:
        ans+=sal
        if sal > salMax:
            salMax = sal
        if sal<salMin:
            salMin = sal
    ans -= (salMax+salMin)
    return ans/(len(salary)-2)


def average2(salary):
    ans = sum(salary)-(max(salary)+min(salary))
    return ans/(len(salary)-2)
  
print(average(salary))
print(average2(salary))
