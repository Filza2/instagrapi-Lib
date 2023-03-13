from instagrapi import Client
import os


   ################################################################################
   #install via : pip install instagrapi or python -m pip install instagrapi     ##
   ################################################################################
   #The fastest and powerful Python library for Instagram Private API 2023       ##
   #instagrapi                                                                   ##
   ################################################################################
   #https://github.com/adw0rd/instagrapi                                         ##
   #https://adw0rd.github.io/instagrapi/getting-started.html                     ##
   #https://adw0rd.github.io/instagrapi/usage-guide/fundamentals.html            ##
   ################################################################################


os.system('cls' if os.name=='nt' else 'clear');print("\nBy @TweakPY - @vv1ck\n\n")

#E. g

cl=Client()

def get_target_info():
    username=input('- username : ')
    password=input('- password : ')
    target=input('- Target username : ')
    cl.login(username,password)
    target_info=cl.user_info_by_username(target)
    print(target_info)
    
def get_user_info():
    username=input('- username : ')
    password=input('- password : ')
    cl.login(username,password)
    user_info=cl.account_info()
    user_security_info=cl.account_security_info()
    print(user_info)
    print(user_security_info)
    
def from_username_to_user_id():
    username=input('- username : ')
    password=input('- password : ')
    target_username=input('- Target username : ')
    username=cl.user_id_from_username(target_username)
    print(username)

def from_user_id_to_username():
    username=input('- username : ')
    password=input('- password : ')
    user_id=input('- Target user id : ')
    username=cl.username_from_user_id(user_id)
    print(username)

def Side_comment():
    
    user_info_functions={
        cl.user_info,
        cl.user_info_by_username,
        cl.user_info_by_username_gql,
        cl.user_info_by_username_v1,
        cl.user_info_gql,
        cl.user_info_v1
    }
    
    generate_functions={
        #generate new 
        cl.generate_android_device_id,
        cl.generate_mutation_token,
        cl.generate_uuid,
        cl.gen_user_breadcrumb,
        
        #base settings
        cl.token,
        cl.advertising_id,
        cl.user_agent,
        cl.app_id,
        cl.base_headers,
        cl.client_session_id,
        cl.device,
        cl.device_settings
    }
    

    
#By @TweakPY - @vv1ck 