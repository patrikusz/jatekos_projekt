// azonnal alkalmazzuk a mentett témát (megelőzi a "villanást")
(function(){
  try{
    const t = localStorage.getItem('siteTheme') || 'colorful';
    if(t === 'dark') document.documentElement.classList.add('theme-dark');
    else if(t === 'light') document.documentElement.classList.add('theme-light');
    // 'colorful' = alapértelmezett, nem kell osztály
  }catch(e){}
})();

document.addEventListener('DOMContentLoaded', function(){
  const KEY = 'siteTheme';
  const select = document.getElementById('themeSelect') || document.querySelector('.setting-select');
  function apply(name){
    document.documentElement.classList.remove('theme-dark','theme-light');
    if(name === 'dark') document.documentElement.classList.add('theme-dark');
    else if(name === 'light') document.documentElement.classList.add('theme-light');
  }
  const saved = localStorage.getItem(KEY) || 'colorful';
  apply(saved);
  if(select){
    // biztosítsuk hogy az optionok értékei rendben legyenek
    Array.from(select.options).forEach(opt => {
      if(!opt.value) {
        const txt = (opt.textContent || '').toLowerCase();
        if(txt.includes('sötét')||txt.includes('dark')) opt.value = 'dark';
        else if(txt.includes('világos')||txt.includes('light')) opt.value = 'light';
        else opt.value = 'colorful';
      }
    });
    select.value = saved;
    select.addEventListener('change', function(){
      const v = select.value || 'colorful';
      localStorage.setItem(KEY, v);
      apply(v);
    });
  }
  // dropdown toggle safety (ha a beallitasok oldalon van)
  const userIcon = document.getElementById('userIcon');
  const dropdownMenu = document.getElementById('dropdownMenu');
  if(userIcon && dropdownMenu){
    userIcon.addEventListener('click', function(e){
      e.stopPropagation();
      const open = dropdownMenu.classList.toggle('open');
      dropdownMenu.style.display = open ? 'block' : 'none';
    });
    document.addEventListener('click', function(){ dropdownMenu.style.display = 'none'; dropdownMenu.classList.remove('open'); });
  }
});