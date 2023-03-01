company_name_list = [{'name': 'Company 1'},
                     {'name': 'Company 2'},
                     {'name': 'Company 3'}]

employee_name_list = [{'name': 'John Doe'},
                      {'name': 'Tom Smith'},
                      {'name': 'Andrew Sebastian'}]

company_detail_list = {
    'Company 1': {
        'name': 'Company 1',
        'domain': 'Retail'
    },
    'Company 2': {
        'name': 'Company 2',
        'domain': 'Construction'
    },
    'Company 3': {
        'name': 'Company 3',
        'domain': 'Healthcare'
    }
}

employee_detail_list = {
    'John Doe': {
        'name': 'EMP-0001',
        'first_name': 'John',
        'last_name': 'Doe',
        'full_name': 'John Doe',
        'company': 'Company 1'
    },
    'Tom Smith': {
        'name': 'EMP-0002',
        'first_name': 'Tom',
        'last_name': 'Smith',
        'full_name': 'Tom Smith',
        'company': 'Company 2'
    },
    'Andrew Sebastian': {
        'name': 'EMP-0003',
        'first_name': 'Andrew',
        'last_name': 'Sebastian',
        'full_name': 'Andrew Sebastian',
        'company': 'Company 2'
    },
}

# GET EMPLOYEE


def get_list_employee():
  return employee_name_list

# FIND EMPLOYEE


def get_employee_detail(employee_name):
  return employee_detail_list[employee_name]

# CREATE EMPLOYEE


def create_new_employee(employee_dict):
    assert 'name' in employee_dict
    assert 'first_name' in employee_dict
    assert 'last_name' in employee_dict
    assert 'full_name' in employee_dict
    assert 'company' in employee_dict
    assert employee_dict['company'] in company_detail_list

    employee_detail_list[employee_dict['name']] = {
        'name': employee_dict['name'],
        'first_name': employee_dict['first_name'],
        'last_name': employee_dict['last_name'],
        'full_name': employee_dict['full_name'],
        'company': employee_dict['company']
    }

    employee_name_list.append({'name': employee_dict['name']})

# DELETE EMPLOYEE


def delete_employee(employee_name):
    assert employee_name in employee_detail_list
    employee_detail_list.pop(employee_name, None)
    new_employee_name_list = [
        x for x in get_list_employee() if x['name'] != employee_name]
    global employee_name_list
    employee_name_list = new_employee_name_list

# UPDATE EMPLOYEE


def update_employee(employee_name, new_employee_dict):
    assert employee_name in employee_detail_list
    assert 'name' in new_employee_dict
    assert 'first_name' in new_employee_dict
    assert 'last_name' in new_employee_dict
    assert 'full_name' in new_employee_dict
    assert 'company' in new_employee_dict
    assert new_employee_dict['company'] in company_detail_list

    employee_detail_list[employee_name] = {
        'name': new_employee_dict['name'],
        'first_name': new_employee_dict['first_name'],
        'last_name': new_employee_dict['last_name'],
        'full_name': new_employee_dict['full_name'],
        'company': new_employee_dict['company']
    }

    for employee in employee_name_list:
        if employee['name'] == employee_name:
            employee['name'] = new_employee_dict['name']
            break


# how to use the function update
update_employee('John Doe', {
    'name': 'John Doe 2',
    'first_name': 'Johnny',
    'last_name': 'Doe',
    'full_name': 'Johnny Doe',
    'company': 'Company 1'
})

# how to use the function delete
delete_employee('Tom Smith')

# how to create employee
create_new_employee({
    'name': 'Alri',
    'first_name': 'Alri',
    'last_name': 'Tjen',
    'full_name': 'Alri Tjen',
    'company': 'Company 3'
})

get_list_employee()
