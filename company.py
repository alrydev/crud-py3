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


def get_list_company():
  return company_name_list


def get_company_detail(company_name):
  return company_detail_list[company_name]


def get_list_employee():
  return employee_name_list


def get_employee_detail(employee_name):
  return employee_detail_list[employee_name]


def create_new_company(company_dict):
  assert 'name' in company_dict
  assert 'domain' in company_dict

  company_detail_list[company_dict['name']] = {
      'name': company_dict['name'],
      'domain': company_dict['domain']
  }

  company_name_list.append({'name': company_dict['name']})


def delete_company(company_name):
  assert company_name in company_detail_list
  company_detail_list.pop(company_name, None)
  new_company_name_list = [
      x for x in get_list_company() if x['name'] != company_name]
  global company_name_list
  company_name_list = new_company_name_list
