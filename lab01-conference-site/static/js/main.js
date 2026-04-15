document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const timetableItems = document.querySelectorAll('.timetable-item');
    const scheduleContainer = document.getElementById('schedule');

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        
        timetableItems.forEach(item => {
            const title = item.getAttribute('data-title') || '';
            const speakers = item.getAttribute('data-speakers') || '';
            const categories = item.getAttribute('data-categories') || '';

            const isMatch = title.includes(query) || 
                            speakers.includes(query) || 
                            categories.includes(query);

            if (isMatch) {
                item.style.display = 'grid';
                item.style.animation = 'none';
                item.offsetHeight; // trigger reflow
                item.style.animation = 'fadeInUp 0.3s ease forwards';
            } else {
                item.style.display = 'none';
            }
        });

        // Hide lunch break if everything else is hidden
        const visibleItems = Array.from(timetableItems).filter(i => i.style.display !== 'none');
        const breakItem = document.querySelector('.break-item');
        if (breakItem) {
            breakItem.style.display = (visibleItems.length === 0 && query !== '') ? 'none' : 'block';
        }
    });

    // Add some visual polish: staggering entry animations
    timetableItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });
});
