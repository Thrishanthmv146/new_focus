class Shopping_Expense_Tracker:
    def __init__(self):
        self.expenses = {
                       "Food": 2500,
                       "Travel": 1500,
                       "Shopping": 4000,
                       "Education": 2000}
        self.exceed_expenses={}
    def total_expenses(self):
        total=0
        for expense in self.expenses.values():
            total+=expense
        print(f"Total Expenses is: {total}")
    def highest_expense(self):
        high_ex=0
        for category,expense in self.expenses.items():
            if expense>high_ex:
                cat=category
                high_ex=expense
        print(f"\nHighest Expense Category is:{cat}---{high_ex}")
    def expenses_exceed(self):
        for category,expense in self.expenses.items():
            if expense>2000:
                cat=category
                self.exceed_expenses[cat]=expense
        print(f"\nCategories greater than 2,000.\n{self.exceed_expenses}") 
    def average_expense(self):
        num_category=len(self.expenses)
        total=0
        for category,expense in self.expenses.items():
            total+=expense
        average_expense=total/num_category
        print(f"\nAverage Expense is:{average_expense}")
    def new_expense(self):
        cat=input("\nAdd any new category: ") 
        exps=int(input("Enter its expense: "))
        self.expenses[cat]=exps
        print(f"New Expense added:{cat}--{exps}")
    def warning_expense(self):
        total=0
        for expense in self.expenses.values():
            total+=expense
        if total>8000:
           print(f"\nTotal Expense exceeded:{total}\n'WARNING'")
shop=Shopping_Expense_Tracker()
shop.total_expenses()
shop.highest_expense()
shop.expenses_exceed()
shop.average_expense()
shop.new_expense()
shop.warning_expense()




