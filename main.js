document.addEventListener('DOMContentLoaded', () => {

    // =========================================================
    // THEME
    // =========================================================
    const isDarkModePreferred = () => {
        if (localStorage.getItem('theme') === 'dark') return true;
        if (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches) return true;
        return false;
    };

    const applyTheme = (isDark) => {
        document.documentElement.classList.toggle('dark', isDark);
        updateThemeIcons(isDark);
    };

    const updateThemeIcons = (isDark) => {
        const desktopIcon = document.getElementById('theme-toggle-icon');
        const mobileIcon  = document.getElementById('theme-toggle-mobile-icon');
        const darkClass  = 'fas fa-sun text-yellow-400 text-xl transition-transform hover:rotate-90';
        const lightClass = 'fas fa-moon text-slate-700 text-xl transition-transform hover:-rotate-12';
        if (desktopIcon) desktopIcon.className = isDark ? darkClass : lightClass;
        if (mobileIcon)  mobileIcon.className  = isDark ? darkClass : lightClass;
    };

    applyTheme(isDarkModePreferred());

    const toggleTheme = () => {
        const willBeDark = !document.documentElement.classList.contains('dark');
        localStorage.setItem('theme', willBeDark ? 'dark' : 'light');
        applyTheme(willBeDark);
    };

    const themeToggleBtn       = document.getElementById('theme-toggle');
    const mobileThemeToggleBtn = document.getElementById('theme-toggle-mobile');
    if (themeToggleBtn)       themeToggleBtn.addEventListener('click', toggleTheme);
    if (mobileThemeToggleBtn) mobileThemeToggleBtn.addEventListener('click', toggleTheme);

    // =========================================================
    // RTL TOGGLE
    // =========================================================
    const applyRTL = (isRTL) => {
        document.documentElement.setAttribute('dir', isRTL ? 'rtl' : 'ltr');
        updateRTLIcons(isRTL);
    };

    const updateRTLIcons = (isRTL) => {
        const btn       = document.getElementById('rtl-toggle');
        const mobileBtn = document.getElementById('rtl-toggle-mobile');
        const title     = isRTL ? 'Switch to LTR' : 'Switch to RTL';
        [btn, mobileBtn].forEach(el => {
            if (!el) return;
            el.title = title;
            el.setAttribute('aria-label', title);
            const icon = el.querySelector('i');
            if (icon) {
                icon.className = isRTL
                    ? 'fas fa-arrow-right-arrow-left text-primary-500'
                    : 'fas fa-arrow-right-arrow-left text-slate-500 dark:text-slate-400';
            }
        });
    };

    const isRTLPreferred = () => localStorage.getItem('dir') === 'rtl';
    applyRTL(isRTLPreferred());

    const toggleRTL = () => {
        const willBeRTL = document.documentElement.getAttribute('dir') !== 'rtl';
        localStorage.setItem('dir', willBeRTL ? 'rtl' : 'ltr');
        applyRTL(willBeRTL);
    };

    const rtlBtn       = document.getElementById('rtl-toggle');
    const rtlBtnMobile = document.getElementById('rtl-toggle-mobile');
    if (rtlBtn)       rtlBtn.addEventListener('click', toggleRTL);
    if (rtlBtnMobile) rtlBtnMobile.addEventListener('click', toggleRTL);

    // =========================================================
    // MOBILE MENU
    // =========================================================
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu    = document.getElementById('mobile-menu');
    const closeMenuBtn  = document.getElementById('close-menu-btn');
    const mobileOverlay = document.getElementById('mobile-overlay');

    const toggleMobileMenu = (isOpen) => {
        if (!mobileMenu) return;
        
        if (isOpen) {
            mobileMenu.classList.add('open');
            document.body.style.overflow = 'hidden';
            if (mobileOverlay) mobileOverlay.classList.remove('hidden');
        } else {
            mobileMenu.classList.remove('open');
            document.body.style.overflow = '';
            if (mobileOverlay) mobileOverlay.classList.add('hidden');
        }
    };

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', () => toggleMobileMenu(true));
    if (closeMenuBtn)  closeMenuBtn.addEventListener('click', () => toggleMobileMenu(false));
    if (mobileOverlay) mobileOverlay.addEventListener('click', () => toggleMobileMenu(false));

    // =========================================================
    // BACK TO TOP BUTTON  (injected dynamically — works on every page)
    // =========================================================
    const backToTopBtn = document.createElement('button');
    backToTopBtn.id = 'back-to-top';
    backToTopBtn.setAttribute('aria-label', 'Back to top');
    backToTopBtn.title = 'Back to top';
    backToTopBtn.innerHTML = '<i class="fas fa-chevron-up text-lg"></i>';
    document.body.appendChild(backToTopBtn);

    const handleScroll = () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

});
