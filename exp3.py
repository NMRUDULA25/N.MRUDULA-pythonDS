#charts in python 
import matplotlib.pyplot as plt
# plt.plot([1,2,3],[2,4,6]) #Line plot
# plt.title("Line Plot Chart")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)
# plt.show()

# Bar Chart
# labels=["A","B","C","D","E"]
# sales=[100,200,500,1500,1200]
# plt.bar(labels,sales,color="violet")
# plt.title("Sales Report")
# plt.ylabel("Values of sales")
# plt.xlabel("Brands")
# plt.show()

#Pie Chart
# labels=["A","B","C"]
# sizes=[120,130,150]
# plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90)
# plt.title("Product Pie Report")
# plt.show()

#histogram
gender=['m','f','m','f','f']
plt.hist(gender,bins=2,color="orange",edgecolor="black")
plt.title("Gender Report")
plt.xlabel("Gender")
plt.ylabel("count")
plt.show()