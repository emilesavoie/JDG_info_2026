document.addEventListener('DOMContentLoaded',()=>{
  const form=document.getElementById('inspection-form')
  const countEl=document.getElementById('count')
  const issuesEl=document.getElementById('issues')
  const rateEl=document.getElementById('rate')
  const lastEl=document.getElementById('last')
  const recoList=document.getElementById('reco-list')

  let inspections=[]

  form.addEventListener('submit',e=>{
    e.preventDefault()
    const id=document.getElementById('inspect-id').value.trim()
    const material=document.getElementById('material').value
    const location=document.getElementById('location').value.trim()
    const notes=document.getElementById('notes').value.trim()
    const hasAnomaly=document.getElementById('has-anomaly').checked
    if(!id || !material || !location){
      alert('Mauvaise entrée(s)...')
      return
    }
    const record={id,material,location,notes,hasAnomaly,ts:Date.now()}
    inspections.push(record)
    updateMetrics()
    generateRecommendations(record)
    // no persistence by design
    form.reset()
    document.getElementById('has-anomaly').checked=true
  })

  document.getElementById('cancel').addEventListener('click',()=>{
      document.getElementById('inspection-form').reset()
      document.getElementById('has-anomaly').checked=true
  })

  function updateMetrics(){
    countEl.textContent=inspections.length
    const anomalies=inspections.filter(i=>i.hasAnomaly).length
    issuesEl.textContent=anomalies
    rateEl.textContent=inspections.length? Math.round(((inspections.length-anomalies)/inspections.length)*100)+'%':'100%'
    lastEl.textContent=inspections.length? new Date(inspections[inspections.length-1].ts).toLocaleString() : '-'
  }

function generateRecommendations(record){
    const ul = recoList;
    ul.innerHTML = '';

    if (record.material === 'Acier' && record.notes.length < 10) {
        const li = document.createElement('li');
        li.textContent = 'Pour l\'acier, ajoutez des mesures plus détaillées (plus que 10 caractères).';
        ul.appendChild(li);
    }
    if(record.hasAnomaly){
        const li = document.createElement('li');
        li.textContent = 'Une anomalie a été détectée. Veuillez suivre le protocole de sécurité.';
        ul.appendChild(li);
    }

    const extraRecommendations = [
        "Vérifiez l'équipement de sécurité avant chaque inspection.",
        "Consultez le manuel d'entretien régulièrement.",
        "Planifiez une formation annuelle pour le personnel.",
        "Assurez-vous que les outils sont calibrés.",
        "Documentez toute anomalie détectée.",
        "Nettoyez la zone d'inspection après usage.",
        "Gardez une trace des inspections précédentes.",
        "Signalez immédiatement tout danger potentiel.",
        "Révisez les procédures d'urgence.",
        "Effectuez une vérification croisée avec un collègue."
    ];
    const randomRec = extraRecommendations[Math.floor(Math.random() * extraRecommendations.length)];
    const extraLi = document.createElement('li');
    extraLi.textContent = randomRec;
    ul.appendChild(extraLi);
}

})
