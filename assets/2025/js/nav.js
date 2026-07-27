// Accessible mobile/desktop navigation interactions
(function(){
  const navToggle = document.getElementById('navToggle');
  const nav = document.getElementById('primary-nav');
  if(!navToggle || !nav) return;

  // Close all open submenus
  function closeSubmenus(except) {
    nav.querySelectorAll('.dropdown.open').forEach(li => {
      if(li !== except){
        li.classList.remove('open');
        const trigger = li.querySelector(':scope > a[aria-expanded]');
        if(trigger) trigger.setAttribute('aria-expanded','false');
      }
    });
  }

  // Toggle mobile menu
  navToggle.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!expanded));
    document.body.classList.toggle('nav-open', !expanded);
  });

  // Add toggles for items with children (mobile accordion behavior) including deeper nesting
  function bindAccordionLinks(){
    nav.querySelectorAll('li[data-has-children] > a').forEach(link => {
      if(link.dataset.bound) return; // avoid rebinding
      link.dataset.bound = 'true';
      const parentLi = link.parentElement;
      link.addEventListener('click', (e) => {
        const isDesktop = window.matchMedia('(min-width: 769px)').matches;
        if(!isDesktop){
          if(parentLi.dataset.hasChildren){
            e.preventDefault();
            const open = parentLi.classList.contains('open');
            if(open){
              parentLi.classList.remove('open');
              link.setAttribute('aria-expanded','false');
              // close all descendants
              parentLi.querySelectorAll('.dropdown.open').forEach(d => {
                d.classList.remove('open');
                const trig = d.querySelector(':scope > a[aria-expanded]');
                if(trig) trig.setAttribute('aria-expanded','false');
              });
            } else {
              // only close siblings at same level
              parentLi.parentElement.querySelectorAll(':scope > .dropdown.open').forEach(sib => {
                if(sib !== parentLi){
                  sib.classList.remove('open');
                  const trig = sib.querySelector(':scope > a[aria-expanded]');
                  if(trig) trig.setAttribute('aria-expanded','false');
                }
              });
              parentLi.classList.add('open');
              link.setAttribute('aria-expanded','true');
            }
          }
        }
      });
    });
  }
  bindAccordionLinks();

  // Close menu on outside click (mobile)
  document.addEventListener('click', (e) => {
    if(!nav.contains(e.target) && e.target !== navToggle){
      if(navToggle.getAttribute('aria-expanded') === 'true'){
        navToggle.click();
      }
    }
  });

  // Improve keyboard navigation
  nav.addEventListener('keydown', (e) => {
    if(e.key === 'Escape'){
      // Close open submenu or full menu
      const openSub = nav.querySelector('.dropdown.open:last-child');
      if(openSub){
        const trigger = openSub.querySelector(':scope > a');
        openSub.classList.remove('open');
        if(trigger) trigger.focus();
        return;
      }
      if(navToggle.getAttribute('aria-expanded') === 'true'){
        navToggle.click();
        navToggle.focus();
      }
    }
  });

  // Adjust on resize (clear inline states)
  window.addEventListener('resize', () => {
    const isDesktop = window.matchMedia('(min-width: 769px)').matches;
    if(isDesktop){
      document.body.classList.remove('nav-open');
      navToggle.setAttribute('aria-expanded','false');
      closeSubmenus();
      // ensure all open classes removed from deep levels
      nav.querySelectorAll('.dropdown.open').forEach(li=>li.classList.remove('open'));
    }
  });
})();
