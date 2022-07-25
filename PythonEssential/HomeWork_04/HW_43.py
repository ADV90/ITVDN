class Employee:

    def __init__(self, first_name, second_name, department, year):
        if type(first_name) == str:
            if str(first_name)[0].isupper():
                self.first_name = first_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('First name cannot contain any digits')

        if type(second_name) == str:
            if str(second_name)[0].isupper():
                self.second_name = second_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('Second name cannot contain any digits')
        self.department = department
        if type(int(year)) == int:
            if int(year) > 1990:
                self.year = int(year)
            else:
                raise ValueError('Company establishing date is 1990')
        else:
            raise ValueError('Year should be type of int')

    def __str__(self):
        return '{} {} from {} department. Employed at {}'.format(self.first_name, self.second_name, self.department,
                                                             self.year)

if __name__ == '__main__':
    e_list =[]
    for i in range(2):
        print('Enter new employee')
        f_name = input('First Name: ')
        s_name = input('Second Name: ')
        dept = input('Dept: ')
        year = input('Year: ')
        emp = Employee(f_name, s_name, dept, year)
        e_list.append(emp)

    for e in e_list:
        try:
            if e.year > 2002:
                print(e)
        except AttributeError as e:
            print(e.__str__())
