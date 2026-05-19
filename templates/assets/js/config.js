
const CONFIG = {
    API_BASE_URL: 'https://skillconnect-backend-jcn0.onrender.com/api',
    
};

if (typeof window !== 'undefined') {
    window.API_BASE_URL = CONFIG.API_BASE_URL;
}
