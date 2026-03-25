import os
import re

files_to_fix = [
    'index.html', 'home-2.html', 'conditions.html', 
    'education.html', 'services.html', 'about.html', 
    'contact.html', 'signup.html'
]

# Base structure of the header
header_template = """    <!-- Header -->
    <header class="fixed w-full top-0 z-50 glass transition-colors duration-300 border-b border-gray-200 dark:border-gray-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center gap-2 group">
                        <i class="fas fa-lungs text-primary-600 text-3xl transition-transform group-hover:scale-110"></i>
                        <span class="font-heading font-bold text-2xl text-slate-900 dark:text-white">Allergy<span class="text-primary-600">Care</span></span>
                    </a>
                </div>
                <nav class="hidden xl:flex items-center space-x-1">
                    <a href="index.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_index} transition-colors">Home</a>
                    <a href="home-2.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_home_2} transition-colors">Home 2</a>
                    <a href="conditions.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_conditions} transition-colors">Conditions Treated</a>
                    <a href="education.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_education} transition-colors">Patient Education</a>
                    <a href="services.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_services} transition-colors">Services</a>
                    <a href="about.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_about} transition-colors">About</a>
                    <a href="contact.html" class="px-3 py-2 rounded-md text-sm font-medium {nav_contact} transition-colors">Contact</a>
                    <a href="dashboard.html" class="px-3 py-2 rounded-md text-sm font-medium text-slate-700 hover:text-primary-600 dark:text-slate-200 dark:hover:text-primary-400 transition-colors">Admin</a>
                </nav>
                <div class="hidden xl:flex items-center space-x-4">
                    <button id="theme-toggle" class="p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none" aria-label="Toggle Dark Mode">
                        <i id="theme-toggle-icon" class="fas fa-moon text-slate-700 dark:text-slate-300 text-xl"></i>
                    </button>
                    <a href="signup.html" class="text-sm font-medium {nav_signup} transition-colors">Sign Up</a>
                    <a href="contact.html" class="bg-primary-600 hover:bg-primary-700 text-white px-5 py-2.5 rounded-full font-medium transition-all transform hover:scale-105 shadow-lg shadow-primary-500/30">Book Appt</a>
                </div>
                <div class="flex xl:hidden items-center space-x-4">
                    <button id="mobile-menu-btn" class="text-slate-900 dark:text-white hover:text-primary-600 focus:outline-none p-2">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
    </header>"""

# Base structure of the mobile menu
mobile_menu_template = """    <!-- Mobile Slide-in Menu -->
    <div id="mobile-menu" class="fixed inset-y-0 right-0 w-80 bg-white dark:bg-darkCard shadow-2xl z-[60] flex flex-col h-screen transform transition-transform duration-300 border-l border-slate-100 dark:border-slate-800 translate-x-full">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-800">
            <span class="font-heading font-bold text-xl text-slate-900 dark:text-white">Allergy<span class="text-primary-600">Care</span></span>
            <button id="close-menu-btn" class="text-slate-500 hover:text-red-500 dark:text-slate-400 focus:outline-none p-2">
                <i class="fas fa-times text-2xl"></i>
            </button>
        </div>
        <div class="flex-1 overflow-y-auto py-4 px-5 flex flex-col gap-2">
            <a href="index.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_index} transition-colors">Home</a>
            <a href="home-2.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_home_2} transition-colors">Home 2</a>
            <a href="conditions.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_conditions} transition-colors">Conditions Treated</a>
            <a href="education.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_education} transition-colors">Patient Education</a>
            <a href="services.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_services} transition-colors">Services</a>
            <a href="about.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_about} transition-colors">About</a>
            <a href="contact.html" class="block px-4 py-3 rounded-xl text-base font-medium {mob_contact} transition-colors">Contact</a>
            <a href="dashboard.html" class="block px-4 py-3 rounded-xl text-base font-medium text-slate-800 hover:bg-primary-50 hover:text-primary-600 dark:text-slate-200 dark:hover:bg-slate-800 dark:hover:text-primary-400 transition-colors">Admin</a>
            
            <div class="mt-6 pt-6 border-t border-gray-100 dark:border-gray-800">
                <a href="signup.html" class="block w-full text-center px-4 py-3 rounded-xl text-base font-medium {mob_signup_btn} transition-colors mb-3">Sign Up</a>
                <a href="contact.html" class="block w-full text-center bg-primary-600 hover:bg-primary-700 text-white px-4 py-3 rounded-xl font-medium transition-colors shadow-lg shadow-primary-500/30">Book Appt</a>
            </div>
            
            <div class="mt-auto pt-6 flex justify-center pb-4">
                 <button id="theme-toggle-mobile" class="flex items-center gap-2 p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none" aria-label="Toggle Dark Mode">
                     <i id="theme-toggle-mobile-icon" class="fas fa-moon text-slate-700 dark:text-slate-300 text-xl"></i>
                     <span class="text-sm font-medium text-slate-700 dark:text-slate-300">Toggle Theme</span>
                 </button>
            </div>
        </div>
    </div>
    <!-- Mobile Overlay -->
    <div id="mobile-overlay" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-[55] hidden transition-opacity"></div>
"""

nav_normal = "text-slate-700 hover:text-primary-600 dark:text-slate-200 dark:hover:text-primary-400"
nav_active = "bg-primary-50 text-primary-600 dark:bg-slate-800 dark:text-primary-400"

mob_normal = "text-slate-800 hover:bg-primary-50 hover:text-primary-600 dark:text-slate-200 dark:hover:bg-slate-800 dark:hover:text-primary-400"
mob_active = "bg-primary-50 text-primary-600 dark:bg-slate-800 dark:text-primary-400"

btn_normal = "bg-slate-100 text-slate-800 hover:bg-slate-200 dark:bg-slate-800 dark:text-white dark:hover:bg-slate-700"
btn_active = "bg-primary-600 text-white hover:bg-primary-700"

def get_header(filename):
    fname = filename.replace('.html', '').replace('-', '_')
    props = {
        'nav_index': nav_normal,
        'nav_home_2': nav_normal,
        'nav_conditions': nav_normal,
        'nav_education': nav_normal,
        'nav_services': nav_normal,
        'nav_about': nav_normal,
        'nav_contact': nav_normal,
        'nav_signup': nav_normal
    }
    key = f'nav_{fname}'
    if key in props:
        props[key] = nav_active
    return header_template.format(**props)

def get_mobile_menu(filename):
    fname = filename.replace('.html', '').replace('-', '_')
    props = {
        'mob_index': mob_normal,
        'mob_home_2': mob_normal,
        'mob_conditions': mob_normal,
        'mob_education': mob_normal,
        'mob_services': mob_normal,
        'mob_about': mob_normal,
        'mob_contact': mob_normal,
        'mob_signup_btn': btn_normal
    }
    key = f'mob_{fname}'
    if key in props:
        props[key] = mob_active
    # special case for signup btn
    if fname == 'signup':
        props['mob_signup_btn'] = btn_active
    return mobile_menu_template.format(**props)

import os

os.chdir(r"C:\Users\Dell\OneDrive\Desktop\Allergy & Immunology Clinic")

for file in files_to_fix:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace header
    # Some pages might have <!-- Header --> or <!-- Simple Header... -->
    # We will regex from <header class=... to </header>
    # Warning: signup.html has a special simple header initially, but we are replacing it anyway.
    new_header = get_header(file)
    content = re.sub(r'(<!--.*?Header.*?-->\s*)?<header.*?</header>', new_header, content, flags=re.DOTALL)

    # 2. Replace mobile menu
    new_mob = get_mobile_menu(file)
    # The simplest way to replace is from the end of the header until <main> or <!-- Main -->
    # First, let's remove any existing mobile menu sections if they exist
    # (some exist as <div id="mobile-menu">...</div> <div id="mobile-overlay"...</div>)
    
    # Let's cleanly inject it right before <main
    # We strip out everything between </header> and <main class=
    # This involves removing any old wrapper divs that were part of mobile menu.
    
    # Step A: find </header> and <main
    main_match = re.search(r'\s*(?:<!--.*?Main.*?-->\s*)?<main', content)
    if main_match:
        main_idx = main_match.start()
        header_end_idx = content.find('</header>') + 9
        
        # We replace the space between them with our new mobile menu
        prefix = content[:header_end_idx]
        suffix = content[main_idx:]
        content = prefix + "\n\n" + new_mob + "\n" + suffix

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
