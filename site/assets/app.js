document.documentElement.classList.add('js');

const header = document.querySelector('.site-header');
const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('#primary-navigation');
if (header && toggle && navigation) {
  const close = () => {
    header.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
  };
  toggle.addEventListener('click', () => {
    const open = header.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  header.addEventListener('keydown', event => {
    if (event.key === 'Escape' && header.classList.contains('nav-open')) {
      close();
      toggle.focus();
    }
  });
  navigation.addEventListener('click', event => {
    if (event.target.closest('a')) close();
  });
  const desktop = window.matchMedia('(min-width: 761px)');
  desktop.addEventListener('change', close);
}

for (const video of document.querySelectorAll('video')) {
  const status = video.parentElement.querySelector('.video-error');
  const fail = () => { if (status) status.hidden = false; };
  video.addEventListener('error', fail);
  for (const source of video.querySelectorAll('source')) source.addEventListener('error', fail);
  video.addEventListener('playing', () => { if (status) status.hidden = true; });
  // 手动播放也随时可暂停；减少动态模式不触发任何自动播放。
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  reduced.addEventListener('change', event => { if (event.matches) video.pause(); });
}

for (const link of document.querySelectorAll('a[href^="#"]')) {
  link.addEventListener('click', () => {
    const id = link.getAttribute('href').slice(1);
    const target = document.getElementById(id);
    if (!target) return;
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });
}
