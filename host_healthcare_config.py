import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

AGENT_CONFIG_DICT = {
    'agent_name': 'Opus AI Assistant',
    'agent_role': 'Customer Service',
    'company_name': 'Host Healthcare',
    'company_introduction': 'Host Healthcare is a travel healthcare staffing agency specializing in travel nursing, allied and therapy jobs. An award-winning staffing company with thousands of jobs',
    'company_values': 'We are on a mission to help others live better by helping the healers of the world (our travel healthcare professionals, healthcare facilities, and internal team members) to be as comfortable as possible. Enabling the best care possible for healthcare patients.'
}


SERVICE_INFO_CONFIG = {
    'Host Healthcare': {
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
    'key_prefix': 'host_healthcare_', #prefix in redis key eg "host_healthcare:session_id"
    'url': 'redis://localhost:6379/0'
}

CHATBOT_VECTORSTORE_POSGRES_CONFIG = {
    'driver': 'psycopg2',
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user_name': os.environ.get("PGVECTOR_USER"),
    'password': os.environ.get("PGVECTOR_PASSWORD"),
    'collection_name': 'discuss_faq'
}