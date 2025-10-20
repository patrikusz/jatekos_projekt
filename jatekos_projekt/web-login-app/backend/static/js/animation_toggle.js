// alkalmazás azonnal
(function(){
  try{
    const saved = localStorage.getItem('siteAnim') || 'on';
    if(saved === 'off') document.documentElement.classList.add('no-anim');
    else document.documentElement.classList.remove('no-anim');
  }catch(e){}
})();

document.addEventListener('DOMContentLoaded', function () {
  const STORAGE_KEY = 'siteAnim';
  const toggle = document.getElementById('animations')
              || document.getElementById('animToggle')
              || document.querySelector('.setting-anim-toggle');

  if(!toggle) return;

  const saved = localStorage.getItem(STORAGE_KEY) || 'on';
  if (toggle.type === 'checkbox') toggle.checked = (saved === 'on');

  function apply(val){
    if (val === 'off') document.documentElement.classList.add('no-anim');
    else document.documentElement.classList.remove('no-anim');
  }

  toggle.addEventListener('change', function () {
    const val = (this.type === 'checkbox') ? (this.checked ? 'on' : 'off') : this.value;
    localStorage.setItem(STORAGE_KEY, val);
    apply(val);
  });
});