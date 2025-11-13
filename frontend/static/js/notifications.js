// Globális üzenet értesítési rendszer
(function() {
    'use strict';
    
    let lastUnreadCount = 0;
    let notificationCheckInterval = null;
    
    // Ellenőrizzük hogy be van-e jelentkezve a felhasználó
    function isLoggedIn() {
        // Ellenőrizzük hogy van-e username a navbarban
        const userElement = document.querySelector('.navbar .nav-link');
        if (!userElement) return false;
        
        const userText = userElement.textContent || '';
        // Ha tartalmazza a person-circle ikont vagy van username szöveg
        return userText.trim().length > 0 && !userText.includes('Bejelentkezés');
    }
    
    // Toast notification megjelenítése
    function showNotificationToast(message, friendName, friendId) {
        console.log('Toast megjelenítése:', friendName, message);
        
        // Toast container létrehozása ha még nincs
        let container = document.querySelector('.notification-toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'notification-toast-container';
            document.body.appendChild(container);
        }
        
        const toastHtml = `
            <div class="toast align-items-center text-white bg-primary border-0" role="alert" data-friend-id="${friendId}">
                <div class="d-flex">
                    <div class="toast-body">
                        <i class="bi bi-chat-dots-fill"></i> <strong>${friendName}</strong> üzenetet küldött!
                        <br><small>${message}</small>
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            </div>
        `;
        
        container.insertAdjacentHTML('beforeend', toastHtml);
        const toastElement = container.lastElementChild;
        
        // Kattintásra navigáljon a barátok oldalra
        toastElement.addEventListener('click', (e) => {
            if (!e.target.classList.contains('btn-close')) {
                window.location.href = '/baratok';
            }
        });
        
        const toast = new bootstrap.Toast(toastElement, { delay: 5000 });
        toast.show();
        
        toastElement.addEventListener('hidden.bs.toast', () => toastElement.remove());
        
        // Böngésző értesítés ha engedélyezve van
        if (Notification.permission === 'granted') {
            new Notification('Új üzenet - Online Játékok', {
                body: `${friendName}: ${message}`,
                icon: '/static/favicon.ico',
                tag: 'chat-notification'
            });
        }
    }
    
    // Olvasatlan üzenetek ellenőrzése
    async function checkUnreadMessages() {
        try {
            const response = await fetch('/api/unread-messages');
            const data = await response.json();
            
            console.log('Olvasatlan üzenetek:', data);
            
            if (data.success) {
                // Ha van új üzenet (több mint az előző ellenőrzéskor)
                if (data.unread_count > lastUnreadCount && lastUnreadCount >= 0) {
                    // Értesítés megjelenítése
                    if (data.latest_message) {
                        showNotificationToast(
                            data.latest_message.message,
                            data.latest_message.sender_name,
                            data.latest_message.sender_id
                        );
                    }
                    
                    // Frissítjük a navbar badge-et
                    updateNavbarBadge(data.unread_count);
                } else if (data.unread_count !== lastUnreadCount) {
                    // Csak a badge frissítése
                    updateNavbarBadge(data.unread_count);
                }
                
                lastUnreadCount = data.unread_count;
            }
        } catch (error) {
            console.error('Hiba az olvasatlan üzenetek ellenőrzésekor:', error);
        }
    }
    
    // Navbar badge frissítése
    function updateNavbarBadge(count) {
        const baratomMenuItem = document.querySelector('a[href="/baratok"]');
        if (baratomMenuItem) {
            let badge = baratomMenuItem.querySelector('.badge');
            if (count > 0) {
                if (!badge) {
                    badge = document.createElement('span');
                    badge.className = 'badge bg-danger rounded-pill ms-1';
                    baratomMenuItem.appendChild(badge);
                }
                badge.textContent = count;
            } else if (badge) {
                badge.remove();
            }
        }
    }
    
    // Böngésző értesítések engedélyezése
    function requestNotificationPermission() {
        if ('Notification' in window && Notification.permission === 'default') {
            Notification.requestPermission();
        }
    }
    
    // Inicializálás oldal betöltésekor
    function init() {
        console.log('Notification system inicializálása...');
        console.log('Be van jelentkezve:', isLoggedIn());
        
        // Csak ha be van jelentkezve
        if (isLoggedIn()) {
            requestNotificationPermission();
            
            // Első ellenőrzés kis késleltetéssel
            setTimeout(() => {
                checkUnreadMessages();
                
                // Rendszeres ellenőrzés 5 másodpercenként
                notificationCheckInterval = setInterval(checkUnreadMessages, 5000);
            }, 1000);
        }
    }
    
    // Indítás amikor a DOM betöltődött
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Tisztítás amikor az oldal bezáródik
    window.addEventListener('beforeunload', () => {
        if (notificationCheckInterval) {
            clearInterval(notificationCheckInterval);
        }
    });
})();
