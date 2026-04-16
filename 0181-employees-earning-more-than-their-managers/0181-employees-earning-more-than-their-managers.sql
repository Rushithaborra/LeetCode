SELECT T1.name As Employee
    FROM Employee AS T1
    JOIN Employee AS T2 ON T1.managerId = T2.id
    WHERE T1.salary > T2.salary;