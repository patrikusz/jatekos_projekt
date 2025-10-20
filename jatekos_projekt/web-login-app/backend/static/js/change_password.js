document.addEventListener('DOMContentLoaded', function(){
  // próbáljuk megtalálni az űrlapot
  const form = document.getElementById('changePwdForm')
             || document.querySelector('form[action*="beallitasok"]')
             || document.querySelector('form');
  if(!form) return;

  const newPwd = form.querySelector('#new_password') || form.querySelector('input[name="new_password"]');
  const confirm = form.querySelector('#confirm_password') || form.querySelector('input[name="confirm_password"]');
  const btn = form.querySelector('#changeBtn') || form.querySelector('button[type="submit"], input[type="submit"]');

  if(!newPwd || !confirm || !btn) return; // nincs mit tenni

  // pw-req lista megtalálása vagy dinamikus létrehozása (ha nincs)
  let pwReqs = document.getElementById('pwReqs') || form.querySelector('.pw-req-list');
  if(!pwReqs){
    pwReqs = document.createElement('ul');
    pwReqs.id = 'pwReqs';
    pwReqs.className = 'pw-req-list';
    pwReqs.innerHTML = `
      <li id="req-length"><span class="check">✕</span> legalább 6 karakter</li>
      <li id="req-upper"><span class="check">✕</span> legalább egy nagybetű (A-Z)</li>
      <li id="req-digit"><span class="check">✕</span> legalább egy szám (0-9)</li>
      <li id="req-special"><span class="check">✕</span> legalább egy speciális karakter (!@#...)</li>
    `;
    // beszúrás: ha van newPwd, akkor utána, különben form végére
    if(newPwd.parentNode) newPwd.parentNode.insertBefore(pwReqs, newPwd.nextSibling);
    else form.appendChild(pwReqs);
  }

  const reqLength = pwReqs.querySelector('#req-length');
  const reqUpper = pwReqs.querySelector('#req-upper');
  const reqDigit = pwReqs.querySelector('#req-digit');
  const reqSpecial = pwReqs.querySelector('#req-special');

  function toggle(li, ok){
    if(!li) return;
    const check = li.querySelector('.check') || li.insertBefore(document.createElement('span'), li.firstChild);
    if(!check.classList) check.classList = { add: ()=>{}, remove: ()=>{} };
    if(ok){
      li.classList.add('met');
      check.textContent = '✔';
    } else {
      li.classList.remove('met');
      check.textContent = '✕';
    }
  }

  function checkAll(p){
    const okLength = p.length >= 6;
    const okUpper = /[A-ZÁÉÍÓÖŐÚÜŰ]/.test(p);
    const okDigit = /\d/.test(p);
    const okSpecial = /[^A-Za-zÁÉÍÓÖŐÚÜŰa-z0-9]/.test(p);
    toggle(reqLength, okLength);
    toggle(reqUpper, okUpper);
    toggle(reqDigit, okDigit);
    toggle(reqSpecial, okSpecial);
    return okLength && okUpper && okDigit && okSpecial;
  }

  function update(){
    const ok = checkAll(newPwd.value || '');
    const match = newPwd.value && newPwd.value === confirm.value;
    // ha btn egy input, használjuk disabled attribútumot
    try { btn.disabled = !(ok && match); } catch(e){ btn.setAttribute('disabled', !(ok && match)); }
  }

  newPwd.addEventListener('input', update);
  confirm.addEventListener('input', update);

  form.addEventListener('submit', function(e){
    if(!checkAll(newPwd.value || '') || newPwd.value !== confirm.value){
      e.preventDefault();
      alert('Ellenőrizd az új jelszót és az egyezést.');
    }
  });

  // init
  update();
});