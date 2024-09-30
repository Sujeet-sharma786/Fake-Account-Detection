let form = document.getElementById("AnalysisForm");
form.addEventListener('onsubmit',(e)=>{
    e.preventDefault();
    console.log(e.target.values);
})