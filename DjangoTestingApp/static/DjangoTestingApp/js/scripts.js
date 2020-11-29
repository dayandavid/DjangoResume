gsap.from('#username', {
    duration: 1,
    y: '-100%',
});

gsap.from('.img-profile', {
    duration: 1,
    y: '-100%'
});

gsap.from('.nav-item', {
    duration: 1,
    opacity: 0,
    stagger: 0.5
});

gsap.from('.profile-item', {
    duration: 1,
    opacity: 0,
    stagger: 0.5
});
