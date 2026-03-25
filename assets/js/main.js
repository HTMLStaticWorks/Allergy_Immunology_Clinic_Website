document.addEventListener('DOMContentLoaded', () => {
    // Theme setup based on localStorage or system preference
    const isDarkModePreferred = () => {
        if (localStorage.getItem('theme') === 'dark') return true;
        if (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches) return true;
        return false;
    };

    const applyTheme = (isDark) => {
        if (isDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        updateThemeIcons(isDark);
    };

    const updateThemeIcons = (isDark) => {
        const desktopIcon = document.getElementById('theme-toggle-icon');
        const mobileIcon = document.getElementById('theme-toggle-mobile-icon');
        
        const darkClass = 'fas fa-sun text-yellow-400 text-xl transition-transform hover:rotate-90';
        const lightClass = 'fas fa-moon text-slate-700 text-xl transition-transform hover:-rotate-12';
        
        if (desktopIcon) desktopIcon.className = isDark ? darkClass : lightClass;
        if (mobileIcon) mobileIcon.className = isDark ? darkClass : lightClass;
    };

    // Initialize Theme
    applyTheme(isDarkModePreferred());

    // Toggle Handlers
    const toggleTheme = () => {
        const willBeDark = !document.documentElement.classList.contains('dark');
        localStorage.setItem('theme', willBeDark ? 'dark' : 'light');
        applyTheme(willBeDark);
    };

    const themeToggleBtn = document.getElementById('theme-toggle');
    const mobileThemeToggleBtn = document.getElementById('theme-toggle-mobile');

    if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
    if (mobileThemeToggleBtn) mobileThemeToggleBtn.addEventListener('click', toggleTheme);

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMenuBtn = document.getElementById('close-menu-btn');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.add('open');
            document.body.style.overflow = 'hidden';
            
            // Add a weak overlay
            let overlay = document.getElementById('menu-overlay');
            if(!overlay) {
                overlay = document.createElement('div');
                overlay.id = 'menu-overlay';
                overlay.className = 'fixed inset-0 bg-black/20 dark:bg-black/40 z-50 transition-opacity backdrop-blur-sm';
                overlay.addEventListener('click', closeMenu);
                document.body.appendChild(overlay);
            }
        });
    }

    const closeMenu = () => {
        if(mobileMenu) mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
        const overlay = document.getElementById('menu-overlay');
        if(overlay) {
            overlay.remove();
        }
    };

    if (closeMenuBtn && mobileMenu) {
        closeMenuBtn.addEventListener('click', closeMenu);
    }
});
