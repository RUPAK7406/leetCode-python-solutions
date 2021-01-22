class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.remove(salary[0])
        salary.pop()
        no_of_items_in_sal  = len(salary)
        sum_of_sal = 0 
        for item in salary:
            sum_of_sal += item
        average_salary = sum_of_sal / no_of_items_in_sal 
        
        return average_salary
        
        