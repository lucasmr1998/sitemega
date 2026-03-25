document.addEventListener('DOMContentLoaded', () => {
    const API_URL = '/api/lead/submit/';

    const handleFormSubmit = async (event, formSource) => {
        event.preventDefault();
        const form = event.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        data.submittedAt = new Date().toISOString();
        data.formSource = formSource;

        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Enviando...';
        }

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                alert('Recebemos seus dados com sucesso! Em breve entraremos em contato.');
                form.reset();
            } else {
                alert('Ocorreu um erro ao enviar. Por favor, tente novamente ou entre em contato pelo WhatsApp.');
                console.error('API error:', response.statusText);
            }
        } catch (error) {
            console.error('Submission error:', error);
            alert('Erro de conexão. Verifique sua internet e tente novamente.');
        } finally {
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        }
    };

    // Dynamic: bind all forms with id starting with "leadForm_"
    document.querySelectorAll('form[id^="leadForm_"]').forEach(form => {
        const source = form.dataset.source || form.id.replace('leadForm_', '') || 'geral';
        form.addEventListener('submit', (e) => handleFormSubmit(e, source));
    });

    // Legacy: keep backward compat for old form IDs
    const legacyForms = { leadFormTracking: 'rastreamento', leadFormEnergy: 'energia' };
    Object.entries(legacyForms).forEach(([id, source]) => {
        const form = document.getElementById(id);
        if (form && !form.id.startsWith('leadForm_')) {
            form.addEventListener('submit', (e) => handleFormSubmit(e, source));
        }
    });
});
