document.documentElement.classList.add('js');

// Native dialog keeps Escape, focus containment and focus restoration available.
if (typeof HTMLDialogElement !== 'undefined') {
  const viewer = document.createElement('dialog');
  viewer.className = 'image-viewer';
  const close = document.createElement('button');
  close.type = 'button';
  close.textContent = document.documentElement.lang === 'zh-CN' ? '关闭截图' : 'Close image';
  const enlarged = document.createElement('img');
  viewer.append(close, enlarged);
  viewer.setAttribute('aria-label', document.documentElement.lang === 'zh-CN' ? '英文应用界面' : 'English app interface');
  document.body.append(viewer);
  close.addEventListener('click', () => viewer.close());
  for (const link of document.querySelectorAll('.screen-zoom')) {
    link.addEventListener('click', event => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      enlarged.src = link.href;
      enlarged.alt = link.querySelector('img').alt;
      viewer.showModal();
    });
  }
}

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
  if (video.error || video.networkState === HTMLMediaElement.NETWORK_NO_SOURCE) fail();
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
