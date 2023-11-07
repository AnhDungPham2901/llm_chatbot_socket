from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

AGENT_CONFIG_DICT = {
    'agent_name': 'Your Agent Name',
    'agent_role': 'Customer Service',
    'company_name': 'Your Company Name',
    'company_introduction': 'Your Company Introduction',
    'company_values': 'Your Company Values'
}


SERVICE_INFO_CONFIG = {
    'Your Company Name': {
        'Search Job': ['preferred working location', 'specialty', 'discipline'],
        'Register Account': ['discipline', 'specialty', 'year of experience', 'how did you here about us', 'first name', 'last name', 'phone number'],
        'FAQ': ['Applications', 'TRAVEL & ASSIGNMENT', 'PAY & SALARY', 'BENIFITS']
    }
}


SERVICE_OVERVIEW_CONFIG = {
    'Search Job': 'Help you find the best fit jobs between hundred jobs available in our database. In order to help finding jobs please provide me your preferences such as {search_job_service_infor_config}'.format(search_job_service_infor_config=SERVICE_INFO_CONFIG[AGENT_CONFIG_DICT['company_name']]['Search Job']),
    'Register Account': 'Help you quick register an account. In order to support please provide {register_account_service_infor_config}'.format(register_account_service_infor_config=SERVICE_INFO_CONFIG[AGENT_CONFIG_DICT['company_name']]['Register Account']),
    'FAQ': 'Here to help answer any questions you might have related to {faq_service_infor_config}'.format(faq_service_infor_config=SERVICE_INFO_CONFIG[AGENT_CONFIG_DICT['company_name']]['FAQ'])
}

CHATBOT_MEMORY_CONFIG = {
    'key_prefix': 'YOUR_KEY_PREFIX', #prefix in redis key eg "YOUR_KEY_PREFIX:session_id"
    'url': 'redis://localhost:6379/0' # adjust the url as your config
}