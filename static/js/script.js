document.addEventListener('DOMContentLoaded', function() {
    const themeSwitcher = document.getElementById('theme-switcher');
    const body = document.body;

    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    body.setAttribute('data-theme', currentTheme);
    updateThemeButton(currentTheme);

    themeSwitcher.addEventListener('click', function() {
        const currentTheme = body.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeButton(newTheme);
    });

    function updateThemeButton(theme) {
        if (theme === 'dark') {
            themeSwitcher.textContent = '☀️ Light Mode';
        } else {
            themeSwitcher.textContent = '🌙 Dark Mode';
        }
    }

    // Show/hide voice ID input based on voice type selection
    const voiceTypeSelects = document.querySelectorAll('select[name="voice_type"]');
    const voiceIdInputs = document.querySelectorAll('input[name="voice_id"]');

    voiceTypeSelects.forEach((select, index) => {
        select.addEventListener('change', function() {
            const voiceIdInput = voiceIdInputs[index];
            if (this.value === 'elevenlabs') {
                voiceIdInput.style.display = 'block';
                voiceIdInput.required = true;
            } else {
                voiceIdInput.style.display = 'none';
                voiceIdInput.required = false;
            }
        });

        // Trigger change event on page load
        select.dispatchEvent(new Event('change'));
    });
});