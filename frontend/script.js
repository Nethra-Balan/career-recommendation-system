async function getRecommendations(){

let skills = document.getElementById("skills").value;
let location = document.getElementById("location").value;
let level = document.getElementById("level").value;

let response = await fetch("http://127.0.0.1:5000/recommend", {

method:"POST",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
skills:skills,
location:location,
level:level
})

});

let data = await response.json();

let resultsDiv = document.getElementById("results");

resultsDiv.innerHTML = "";

data.forEach(job => {

resultsDiv.innerHTML += `
<div class="job-card">

<h3>${job.job_title}</h3>

<p><b>Company:</b> ${job.company}</p>

<p><b>Location:</b> ${job.job_location}</p>

<a href="${job.job_link}" target="_blank">Apply</a>

</div>
`;

});

}