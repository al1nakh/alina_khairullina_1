#1
f=open("shop_logs.txt","r")
unique_users=set()
total_buys=0
total_sum=0
user_spending={}
for line in f:
    line=line.strip()
    if not line:
        continue
    parts=line.split(";")
    if len(parts)<3:
        continue
    user_id=parts[1]
    action=parts[2]
    unique_users.add(user_id)
    if action == "BUY":
        if len(parts)<4:
            continue
        n=int(parts[3])
        total_buys+=1
        total_sum+=n
        if user_id not in user_spending:
            user_spending[user_id]=n
        else:
            user_spending[user_id]+=n
f.close()
max_user=""
max_spend=0
for user in user_spending:
    if user_spending[user]>max_spend:
        max_spend=user_spending[user]
        max_user=user
    if total_buys>0:
        u=total_sum/total_buys
    else:
        u=0
report = open("report.txt","w",encoding="utf-8")
report.write("Уникальных пользователей:"+ str(len(unique_users))+"\n")
report.write("Всего покупок:"+ str(total_buys)+"\n")
report.write("Общая сумма:"+ str(total_sum)+"\n")
report.write("Самый активный покупатель:"+max_user+"\n")
report.write("Средний чек:"+ str(u) +"\n")
report.close()
print("Отчет успешно создан!")



#2
import csv

employees=[]
dept_salaries={}
total_salary=0
with open("employees.csv","r") as f:
    reader=csv.DictReader(f)

    for row in reader:
        name=row["name"]
        department=row["department"]
        salary=int(float(row["salary"]))
        employee={
            "name": name,
            "department": department,
            "salary": salary
        }
    employees.append(employee)
    total_salary +=salary
    if department not in dept_salaries:
        dept_salaries[department]=[]
    dept_salaries[department].append(salary)

average_salary=total_salary/len(employees)
print("Средняя зарплата:",average_salary)

dept_avg={}
for department in dept_salaries:
    dept_avg[department]=sum(dept_salaries[department])/len(dept_salaries[department])
    print(f"Средняя зарплата в {department}: {dept_avg[department]}")

best_dept=max(dept_avg, key=dept_avg.get)
print("Отдел с самой высокой средней зарплатой:", best_dept)

highest_paid=employees[0]
for emp in employees:
    if emp["salary"] > highest_paid["salary"]:
        highest_paid=emp
print("Самый высокооплачиваемый сотрудник:", highest_paid)

high_paid_employees=[]
for emp in employees:
    if emp["salary"] >average_salary:
        high_paid_employees.append(emp)
print("Сотрудники с зарплатой выше средней:", high_paid_employees)

with open("high_aslary.csv","w",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_paid_employees)

# 3
import json

with open("orders.json", "r") as f:
    orders = json.load(f)
total_revenue = 0
item_count = {}
for order in orders:
    total_revenue += order["total"]

    for item in order["items"]:
        if item in item_count:
            item_count[item]+= 1
        else:
            item_count[item] = 1
highest_order = orders[0]
for order in orders:
    if order["total"] > highest_order["total"]:
        highest_order = order

most_popular_item = list(item_count.keys())[0]
for item in item_count:
    if item_count[item] > item_count[most_popular_item]:
        most_popular_item = item

summary = {
    "total_revenue": total_revenue,
    "top_user": highest_order["user"],
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)


#4
import csv
import json
import csv

data = [
    ["user_id", "amount"],
    ["user_1", 5000],
    ["user_2", 10000],
    ["user_1", 700000],
    ["user_3", 3000],
    ["user_2", 900000],
    ["user_4", 2000]
]

with open("transactions.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Файл transactions.csv успешно создан")
input_file = "transactions.csv"
txt_report = "fraud_report.txt"
json_report = "fraud_users.json"


transaction_count = {}
suspicious_transactions = []
suspicious_users = set()
total_suspicious_amount = 0


with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = row['user_id']
        amount = float(row['amount'])


        transaction_count[user] = transaction_count.get(user, 0) + 1


        if amount > 500000:
            suspicious_transactions.append({'user_id': user, 'amount': amount})
            suspicious_users.add(user)
            total_suspicious_amount += amount


for user, count in transaction_count.items():
    if count > 3:
        suspicious_users.add(user)

with open(txt_report, "w") as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users)}\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")

with open(json_report, "w") as f:
    json.dump(list(suspicious_users), f, ensure_ascii=False, indent=4)




