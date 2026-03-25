document.addEventListener('DOMContentLoaded', () => {
    // Configuration - UPDATE THIS URL
    const WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE';

    // Helper to handle form submission
    const handleFormSubmit = async (event, formId) => {
        event.preventDefault();
        const form = event.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;

        // Gather data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Add timestamp
        data.submittedAt = new Date().toISOString();
        data.formSource = formId;

        // Visual feedback
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Enviando...';
        }

        try {
            // Check if Webhook URL is set
            if (WEBHOOK_URL === 'YOUR_WEBHOOK_URL_HERE') {
                alert('Configuração necessária: Por favor configure a URL do Webhook no arquivo assets/js/form-handler.js');
                console.error('Webhook URL not configured');
                throw new Error('Webhook missing');
            }

            const response = await fetch(WEBHOOK_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert('Recebemos seus dados com sucesso! Em breve entraremos em contato.');
                form.reset();
            } else {
                alert('Ocorreu um erro ao enviar. Por favor, tente novamente ou entre em contato pelo WhatsApp.');
                console.error('Webhook error:', response.statusText);
            }
        } catch (error) {
            console.error('Submission error:', error);
            if (error.message !== 'Webhook missing') {
                alert('Erro de conexão. Verifique sua internet e tente novamente.');
            }
        } finally {
            // Restore button
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        }
    };

    // Attach listeners
    const trackingForm = document.getElementById('leadFormTracking');
    if (trackingForm) {
        trackingForm.addEventListener('submit', (e) => handleFormSubmit(e, 'leads_rastreamento'));
    }

    const energyForm = document.getElementById('leadFormEnergy');
    if (energyForm) {
        energyForm.addEventListener('submit', (e) => handleFormSubmit(e, 'leads_energia'));
    }
});
