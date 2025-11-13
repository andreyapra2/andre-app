document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.desktop-nav');
    const navLinks = document.querySelectorAll('.desktop-nav a');

    // 1. Toggle Menu Navigasi di Mobile
    menuToggle.addEventListener('click', function() {
        nav.classList.toggle('active');
    });

    // 2. Tutup Menu Navigasi setelah Link diklik (untuk mobile)
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Hanya tutup jika navigasi sedang dalam mode aktif (mobile view)
            if (nav.classList.contains('active')) {
                nav.classList.remove('active');
            }
        });
    });

    // Opsional: Animasi Counter (memerlukan implementasi yang lebih detail)
    // Jika Anda ingin membuat angka statistik beranimasi:
    // const stats = document.querySelectorAll('.stat-item span');
    // ... (Implementasi animasi counter di sini)
});